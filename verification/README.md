# Reproducible calculations

The scripts evaluate the finite POVM and its Fisher information directly from Born probabilities. They check the algebraic constants and the concrete examples in the [scientific account](../science/README.md). The analytic construction and converse prove the general theorem; finite numerical cases do not establish universal validity, bibliographic priority, or pilot-sample asymptotics.

## Run

Tested with Python **3.12.14**, NumPy **2.3.5**, and Matplotlib **3.10.8**. NumPy is the only dependency for the checks; Matplotlib generates the figure.

```bash
python -m pip install -r verification/requirements.txt
python verification/check_readout.py
python verification/check_paid_calibration.py
python verification/check_readout.py --output verification/results.json
python verification/plot_calibration.py
```

Run these commands from the repository root. The second check invocation additionally writes the detailed report; it is not a separate scientific test. [results.json](results.json) records the observed environment, all cases, and SHA-256 hashes of the two numerical source files. Floating-point residuals can vary slightly across numerical libraries.

## What is checked

| Calculation | Cases and criterion |
| --- | --- |
| Explicit measurement | Seven dimension/rank pairs, each at spectral exponents 0, 4, and 8; 21 cases in total. Check the outcome count, strict nominal probability positivity, completeness, the full exact Fisher identity, and the minimum normalized Fisher eigenvalue. |
| Information budgets | The same cases check total Gill–Massar trace. Rank-deficient cases also check the support-rotation trace equals $`d-r`$. |
| Qutrit example | Directly recover both seven-dimensional Fisher matrices at spectrum $`(0.17,0.83,0)`$ and the achieved SLD-weighted cost $`26`$. |
| Exact score estimator | Sum over the ten qutrit outcomes to check zero mean, identity derivative of the mean, and covariance $`I^{-1}`$ for one copy. Independence supplies the factor $`1/n`$. |
| Calibration formula | Twelve comparisons across rank-two qutrit and rank-three seven-dimensional states, two weak eigenvalues, and three basis-error angles. Evaluate the entire miscalibrated POVM, including its pair effects. |
| General-measurement converse | Random rank-one frames, their coarse-grainings, and eigenbasis projective measurements at three dimension/rank pairs. Include exact zero-probability kernel outcomes under the ordinary-score convention. |
| Basis invariance | Apply a common deterministic random unitary to the state, tangents, and effects at three dimension/rank pairs, then compare the resulting FI with the original matrix. |

The construction pairs are $`(d,r)=(3,1),(3,2),(4,2),(7,3),(7,6),(6,6),(16,3)`$. The $`(6,6)`$ cases are **full-rank construction controls**: the displayed POVM still exists there, but the rank-deficient optimality theorem does not apply. For $`r\gt 1`$, the occupied eigenvalues are proportional to a geometric progression with largest-to-smallest ratio $`10^q`$, where $`q\in\{0,4,8\}`$. The pure-state case has only one occupied eigenvalue.

## Recorded result

The complete check passed. The largest residuals in the 21 construction cases were:

| Quantity | Observed maximum | Required tolerance |
| --- | ---: | ---: |
| Maximum entrywise completeness error | $`2.13\times10^{-15}`$ | $`10^{-12}`$ |
| Fisher-identity Frobenius error divided by $`\lVert J\rVert_F`$ | $`5.11\times10^{-16}`$ | $`10^{-12}`$ |
| Minimum normalized-Fisher eigenvalue error | $`1.47\times10^{-15}`$ | $`10^{-10}`$ |

The report provides the remaining residuals and calibration fractions. Large absolute entries of $`J`$ arise when an occupied eigenvalue is small, so the identity check uses a relative matrix residual. The minimum-eigenvalue check uses a Cholesky congruence with the same eigenvalues as $`J^{-1/2}IJ^{-1/2}`$.

## Paid calibration checks

[check_paid_calibration.py](check_paid_calibration.py) constructs the ten effects through the existing calibrated readout, rotates their nominal basis, and evaluates all seven Born-rule derivatives directly. The analytical formulas are in [paid calibration](../science/paid-calibration.md), not inferred from the finite suite.

The script checks both weak-angle quadratures, the strong-error real and imaginary invariant-block spectra, the exact-calibration full matrix, and the small-occupation weak-error full-matrix limit. It also enumerates every possible complete record for a two-copy pilot and two subsequent one-copy outcomes: 900 possible records per operating spectrum. The full seven-dimensional joint-score Fisher matrix is compared with the pilot matrix plus the expected conditional matrix. Some conditional settings have exactly dark outcomes; ordinary zero-score contributions are checked before numerical floating-point remnants are omitted. No successful-shot conditioning is used.

The displayed pilot is orientation consistent: positive $`\widehat\alpha`$ selects $`\cos\widehat\alpha e_1+\sin\widehat\alpha f`$, corresponding to $`\delta=-\widehat\alpha`$ in the strong-error formula. A separate count enumeration checks the exact binomial mixture, including its even/odd fixed-pilot limits. A positive-definite IC pilot illustrates, without claiming optimality, the different strong and weak angular FI scales.

The output is [paid-calibration-results.json](paid-calibration-results.json). Formula cases use $`b=10^{-10},10^{-6},0.01,0.3`$ and angles $`0,\pm0.01,\pm0.1,\pm0.4`$. Full-record cases use $`b=0.01,0.2`$. The checks use tolerances appropriate to the rare-event denominators; their results are finite diagnostics, not proofs of uniform calibration complexity, a Gaussian approximation, the two-copy separation, or finite-sample risk. The authoritative exact Haar calculation and its integral checks are in [Quantum Readout Rank Threshold](https://github.com/GoGoKo699/Quantum-Readout-Rank-Threshold/blob/c4356840cb334f93b3e8367870b79fee45f937c2/science/haar-pair-readout.md).

## Figure

[plot_calibration.py](plot_calibration.py) produces [calibration.svg](../science/figures/calibration.svg) from the exact formula implemented in [readout.py](readout.py). The plotted model has rank two, dimension three, eigenvalues $`(1-\varepsilon,\varepsilon,0)`$, and a fixed error mixing the strongly occupied eigenvector with the kernel. Its comparison with direct POVM probabilities is part of the check above.

The plot illustrates sensitivity of this specified readout to calibration error. It does not claim an optimal lower bound on the samples needed to calibrate an arbitrary measurement.

## Hosted page verification

The [verification workflow](../.github/workflows/verify.yml) runs the numerical checks and verifies every tracked Markdown page from its exact GitHub commit. The [comparison collector](capture_hosted_math.cjs) uses anonymous Chromium at widths 1440 and 760 pixels. It compares every hosted mathematical expression with MathJax's source-derived MathML, preserving fractions, subscripts, superscripts, and table cells. The [source checker](check_rendered_math.py) also checks page identities, source hashes, expression counts, relations, labels, and renderer errors. Display geometry checks detect missing, overflowing, or collapsed equations.

The collector saves actual page HTML and screenshots, source inventories, captured MathML, per-viewport check results, and a hashed `hosted-report.json`. The workflow uses read-only repository access. Its `readout-hosted` artifact is retained for seven days; a transient artifact link is not permanent preservation.

To reproduce the comparison, install Playwright 1.56.1, MathJax 3.2.1, and Chromium in a temporary dependency directory, then run:

```bash
NODE_PATH=/absolute/temporary/dependencies/node_modules \
node verification/capture_hosted_math.cjs \
  --root "$PWD" \
  --repository GoGoKo699/Calibrated-Quantum-Readout \
  --revision "$(git rev-parse HEAD)" \
  --output /absolute/new-empty-capture-directory
```

A passing report covers the captured revision and pages. Inspecting equation bodies, tables, navigation, and narrow-screen layout remains a separate visual review. The automated comparison does not establish scientific correctness, priority, arbitrary TeX equivalence, future host behavior, or other browsers.

The earlier [raw capture script](capture_github.cjs) remains available when recorded DOM and measured element rectangles are useful for diagnostics. Its successful collection alone does not assert that source-to-host comparison passed.
