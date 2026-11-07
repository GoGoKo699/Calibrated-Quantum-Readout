#!/usr/bin/env node
"use strict";

// Collect actual GitHub DOM and geometry for later, separate verification.
// This program does not compare formulas or certify a rendering result.
const fs = require("node:fs");
const path = require("node:path");
const crypto = require("node:crypto");
const { execFileSync } = require("node:child_process");

const SIZES = [
  { width: 1440, height: 1000 },
  { width: 760, height: 1000 },
];
const digest = (data) => crypto.createHash("sha256").update(data).digest("hex");

function options(argv) {
  if (argv.length === 1 && argv[0] === "--help") return null;
  const allowed = new Set(["--root", "--repository", "--revision", "--output"]);
  const result = {};
  for (let i = 0; i < argv.length; i += 2) {
    const flag = argv[i];
    if (!allowed.has(flag) || !argv[i + 1] || Object.hasOwn(result, flag.slice(2))) {
      throw new Error("Expected each of --root, --repository, --revision and --output exactly once");
    }
    result[flag.slice(2)] = argv[i + 1];
  }
  if (Object.keys(result).length !== 4) throw new Error("Four named arguments are required");
  if (!/^[0-9a-f]{40}$/.test(result.revision)) throw new Error("Revision must be a full lowercase commit SHA");
  const pieces = result.repository.split("/");
  if (pieces.length !== 2 || pieces.some((p) => !/^[A-Za-z0-9_.-]+$/.test(p) || p === "." || p === "..")) {
    throw new Error("Repository must be an exact owner/name identity");
  }
  result.root = fs.realpathSync(result.root);
  result.output = path.resolve(result.output);
  return result;
}

function gitBytes(root, args) {
  return execFileSync("git", ["--no-replace-objects", ...args], {
    cwd: root,
    maxBuffer: 128 * 1024 * 1024,
  });
}

function quotedPath(value) {
  return value.split("/").map((part) => encodeURIComponent(part).replace(/[!'()*]/g,
    (character) => "%" + character.charCodeAt(0).toString(16).toUpperCase())).join("/");
}

function sources(config) {
  const commit = gitBytes(config.root, ["rev-parse", "--verify", config.revision + "^{commit}"]).toString().trim();
  if (commit !== config.revision) throw new Error("Requested object is not the exact commit");
  const tree = gitBytes(config.root, ["rev-parse", config.revision + "^{tree}"]).toString().trim();
  const entries = gitBytes(config.root, ["ls-tree", "--full-tree", "-r", "-z", config.revision])
    .toString("utf8").split("\0").filter(Boolean);
  const pages = [];
  for (const entry of entries) {
    const tab = entry.indexOf("\t");
    if (tab < 0) throw new Error("Unexpected Git tree record");
    const [mode, type] = entry.slice(0, tab).split(" ");
    const file = entry.slice(tab + 1);
    if (!/\.(?:md|markdown|mdown|mkdn|mkd)$/i.test(file)) continue;
    if (type !== "blob" || !["100644", "100755"].includes(mode)) {
      throw new Error("Markdown source must be a regular Git blob: " + file);
    }
    if (file.startsWith("/") || file.includes("\\") || file.split("/").some((p) => !p || p === "." || p === "..")) {
      throw new Error("Unsupported source path: " + file);
    }
    pages.push({
      path: file,
      url: "https://github.com/" + config.repository + "/blob/" + config.revision + "/" + quotedPath(file),
      source_sha256: digest(gitBytes(config.root, ["show", config.revision + ":" + file])),
    });
  }
  if (!pages.length) throw new Error("Pinned commit contains no supported Markdown pages");
  return { tree, pages };
}

function saveJSON(filename, value) {
  fs.writeFileSync(filename, JSON.stringify(value, null, 2) + "\n");
}

function registerArtifact(output, name, kind, manifest) {
  const bytes = fs.readFileSync(path.join(output, name));
  manifest.artifacts.push({ path: name, size_bytes: bytes.length, sha256: digest(bytes), kind });
}

function failureCategory(error) {
  const message = error instanceof Error ? error.message : String(error);
  if (message.includes("ERR_BLOCKED_BY_ADMINISTRATOR") || message.includes("URLBlocklist")) return "policy_denial";
  if (message.startsWith("HTTP 401") || message.startsWith("HTTP 403")) return "access_failure";
  if (message.startsWith("Unexpected final URL")) return "unexpected_destination";
  return "capture_failure";
}

async function settleArticle(page) {
  const articles = page.locator("article.markdown-body");
  await articles.first().waitFor({ state: "visible", timeout: 30000 });
  if (await articles.count() !== 1) throw new Error("Expected one rendered Markdown article");

  // Visit the entire page so lazy rendering can occur, without changing its DOM.
  let y = 0;
  let traversed = false;
  for (let step = 0; step < 300; step++) {
    const height = await page.evaluate(() => document.documentElement.scrollHeight);
    if (y >= height) { traversed = true; break; }
    await page.evaluate((position) => window.scrollTo(0, position), y);
    await page.waitForTimeout(60);
    y += 700;
  }
  if (!traversed) throw new Error("Page exceeded the bounded scroll traversal");
  await page.evaluate(() => window.scrollTo(0, 0));

  await page.waitForFunction(() => {
    const article = document.querySelector("article.markdown-body");
    return article && Array.from(article.querySelectorAll("math-renderer"))
      .every((element) => element.querySelector("math") !== null);
  }, null, { timeout: 30000 });
  await page.evaluate(async () => {
    if (document.fonts) {
      let timer;
      try {
        await Promise.race([
          document.fonts.ready,
          new Promise((_, reject) => { timer = setTimeout(() => reject(new Error("Font loading timed out")), 15000); }),
        ]);
      } finally { clearTimeout(timer); }
    }
  });

  // Demand several unchanged samples before taking the atomic DOM snapshot.
  let previous = null;
  let identical = 0;
  for (let attempt = 0; attempt < 40; attempt++) {
    const signature = digest(await articles.first().evaluate((article) => article.outerHTML));
    identical = signature === previous ? identical + 1 : 0;
    previous = signature;
    if (identical >= 3) return articles.first();
    await page.waitForTimeout(250);
  }
  throw new Error("Rendered article did not settle");
}

async function recordPage(article) {
  // All HTML and rectangles below are read in one browser evaluation. Rectangles
  // are the measured values, including zeros for elements without layout boxes.
  return article.evaluate((root) => {
    const rectangle = (element) => {
      const box = element.getBoundingClientRect();
      return { x: box.x, y: box.y, left: box.left, right: box.right,
        top: box.top, bottom: box.bottom, width: box.width, height: box.height };
    };
    return {
      captured_at: new Date().toISOString(),
      observed_url: location.href,
      observed_viewport: { width: innerWidth, height: innerHeight },
      article_html: root.outerHTML,
      client_width: root.clientWidth,
      root_rect: rectangle(root),
      elements: Array.from(root.querySelectorAll("*")).map((element) => ({
        tag: element.localName,
        namespace_uri: element.namespaceURI,
        outer_html: element.outerHTML,
        rect: rectangle(element),
      })),
      document_html: (document.doctype ? "<!DOCTYPE " + document.doctype.name + ">\n" : "")
        + document.documentElement.outerHTML,
    };
  });
}

async function capture(config) {
  const pinned = sources(config);
  if (fs.existsSync(config.output) && fs.readdirSync(config.output).length !== 0) {
    throw new Error("Output must be a new or empty directory; previous evidence is retained");
  }
  fs.mkdirSync(config.output, { recursive: true });
  const manifest = {
    schema_version: 1,
    repository: config.repository,
    revision: config.revision,
    tree: pinned.tree,
    captured_at: new Date().toISOString(),
    runtime: { node: process.version, playwright: null, browser: null },
    status: "collecting",
    pages: pinned.pages,
    viewports: [],
    artifacts: [],
    failures: [],
    limits: "Raw hosted DOM, measured geometry and screenshots only; mathematical and visual verification are separate.",
  };
  const manifestFile = path.join(config.output, "capture-manifest.json");
  const checkpoint = () => saveJSON(manifestFile, manifest);
  checkpoint();
  let browser;
  let activePage = null;
  try {
    const playwright = require("playwright");
    manifest.runtime.playwright = require("playwright/package.json").version;
    browser = await playwright.chromium.launch({ headless: true });
    manifest.runtime.browser = browser.version();
    for (const viewport of SIZES) {
      const view = { ...viewport, status: "collecting", pages: [] };
      manifest.viewports.push(view);
      // No saved session, account state, custom credentials or browser overrides.
      const context = await browser.newContext({ viewport, deviceScaleFactor: 1, colorScheme: "light" });
      try {
        for (let index = 0; index < pinned.pages.length; index++) {
          const source = pinned.pages[index];
          const entry = { ...source, revision: config.revision, errors: [], artifacts: {} };
          view.pages.push(entry);
          activePage = entry;
          checkpoint();
          const page = await context.newPage();
          try {
            const response = await page.goto(source.url, { waitUntil: "domcontentloaded", timeout: 60000 });
            entry.http_status = response ? response.status() : null;
            if (entry.http_status !== 200) throw new Error("HTTP " + entry.http_status + " at " + source.url);
            if (page.url() !== source.url) throw new Error("Unexpected final URL: " + page.url());
            const article = await settleArticle(page);
            const observed = await recordPage(article);
            if (observed.observed_url !== source.url) throw new Error("Unexpected final URL: " + observed.observed_url);
            const stem = "page-" + String(index + 1).padStart(4, "0") + "-" + viewport.width;
            const htmlName = stem + ".html";
            fs.writeFileSync(path.join(config.output, htmlName), observed.document_html);
            entry.artifacts.html = htmlName;
            registerArtifact(config.output, htmlName, "hosted_html", manifest);
            delete observed.document_html;
            for (const element of observed.elements) {
              element.outer_html_sha256 = digest(element.outer_html);
              delete element.outer_html;
            }
            const domName = stem + ".dom.json";
            saveJSON(path.join(config.output, domName), {
              schema_version: 1, repository: config.repository, revision: config.revision,
              tree: pinned.tree, path: source.path, url: source.url,
              source_sha256: source.source_sha256, viewport, ...observed,
            });
            entry.artifacts.dom = domName;
            registerArtifact(config.output, domName, "hosted_dom_geometry", manifest);
            const screenshotName = stem + ".png";
            await page.screenshot({ path: path.join(config.output, screenshotName), fullPage: true, timeout: 30000 });
            entry.artifacts.screenshot = screenshotName;
            registerArtifact(config.output, screenshotName, "screenshot", manifest);
            entry.captured_at = observed.captured_at;
          } finally {
            await page.close();
          }
          activePage = null;
          checkpoint();
        }
        view.status = "captured";
      } finally {
        await context.close();
      }
    }
    manifest.status = "captured";
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    if (activePage) activePage.errors.push(message);
    const current = manifest.viewports.at(-1);
    if (current && current.status === "collecting") current.status = "failed";
    manifest.failures.push({ category: failureCategory(error), message });
    manifest.status = "failed";
    // Every capture error terminates this attempt, including access/policy errors.
    // There is no alternate host, retry, authentication or security-setting path.
  } finally {
    if (browser) {
      try { await browser.close(); }
      catch (error) {
        manifest.failures.push({ category: "browser_cleanup_failure", message: String(error) });
        manifest.status = "failed";
      }
    }
    manifest.finished_at = new Date().toISOString();
    checkpoint();
  }
  console.log(JSON.stringify({ status: manifest.status, manifest: manifestFile,
    sha256: digest(fs.readFileSync(manifestFile)), source_pages: pinned.pages.length,
    recorded_pages: manifest.viewports.reduce((n, view) => n + view.pages.length, 0) }));
  return manifest.status === "captured" ? 0 : 1;
}

if (require.main === module) {
  (async () => {
    const config = options(process.argv.slice(2));
    if (!config) {
      console.log("capture_github.cjs --root REPO --repository OWNER/NAME --revision FULL_SHA --output EMPTY_DIRECTORY");
      return;
    }
    process.exitCode = await capture(config);
  })().catch((error) => { console.error(error instanceof Error ? error.message : String(error)); process.exitCode = 2; });
}
