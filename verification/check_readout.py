"""Direct numerical checks supporting the analytic account; no novelty claim.

Run from the repository root: python verification/check_readout.py
Optional: --output verification/results.json
"""

import argparse
import hashlib
import json
from pathlib import Path
import platform

import numpy as np

from readout import (calibrated_effects, calibration_fraction, classical_fisher,
                     diagonal_surplus, normalized_fisher, probability_derivatives,
                     quantum_fisher, tangent_basis)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def construction_case(d, r, exponent):
    lam = np.logspace(0, -exponent, r)
    lam /= lam.sum()
    eigenvalues = np.r_[lam, np.zeros(d - r)]
    rho = np.diag(eigenvalues)
    effects = calibrated_effects(d, r)
    tangents, cross = tangent_basis(d, r)
    p, _ = probability_derivatives(effects, rho, tangents)
    classical = classical_fisher(effects, rho, tangents)
    quantum = quantum_fisher(eigenvalues, tangents)
    surplus = diagonal_surplus(lam, tangents)
    relative = normalized_fisher(classical, quantum)
    values = np.linalg.eigvalsh(relative)
    completeness = float(np.max(np.abs(effects.sum(0) - np.eye(d))))
    formula = float(np.linalg.norm(classical - quantum / (2 * r) - surplus)
                    / np.linalg.norm(quantum))
    minimum_error = float(abs(values[0] - 1 / (2 * r)))
    trace_error = float(abs(values.sum() - (d - 1)))
    cross_error = 0.0
    if len(cross):
        ix = np.ix_(cross, cross)
        cross_error = float(abs(np.trace(np.linalg.solve(quantum[ix], classical[ix])) - (d - r)))
    require(len(tangents) == r * (2 * d - r) - 1, "Tangent dimension")
    require(len(effects) == 2 * r * d - r, "Outcome count")
    require(p.min() > 0, "Strictly positive nominal probabilities")
    require(completeness < 1e-12, "POVM completeness")
    require(formula < 1e-12, "Exact Fisher identity")
    require(minimum_error < 1e-10, "Minimum normalized Fisher eigenvalue")
    require(trace_error < 1e-7, "Full Gill--Massar trace")
    require(cross_error < 1e-10, "Support-rotation trace")
    return dict(d=d, r=r, spectral_exponent=exponent,
                role="full_rank_construction_control" if d == r else "rank_deficient_theorem",
                outcomes=len(effects), minimum_probability=float(p.min()),
                completeness_error=completeness, relative_identity_error=formula,
                minimum_eigenvalue_error=minimum_error, full_trace_error=trace_error,
                cross_trace_error=cross_error)


def qutrit_and_score():
    p = 0.17
    eigenvalues = np.array([p, 1 - p, 0.0])
    tangents, _ = tangent_basis(3, 2)
    # Use the unnormalized off-diagonal coordinates of science/examples.md.
    tangents[1:] *= np.sqrt(2)
    effects = calibrated_effects(3, 2)
    classical = classical_fisher(effects, np.diag(eigenvalues), tangents)
    quantum = quantum_fisher(eigenvalues, tangents)
    expected_j = np.diag([1 / (p * (1 - p)), 4, 4, 4 / p, 4 / p,
                          4 / (1 - p), 4 / (1 - p)])
    expected_i = np.diag([1 / (2 * p * (1 - p)), 1, 1, 1 / p, 1 / p,
                          1 / (1 - p), 1 / (1 - p)])
    qutrit_error = float(max(np.max(np.abs(quantum - expected_j)),
                             np.max(np.abs(classical - expected_i))))
    require(qutrit_error < 1e-12, "Qutrit closed forms")
    cost = float(np.trace(quantum @ np.linalg.inv(classical)))
    require(abs(cost - 26) < 1e-12, "Qutrit achieved SLD-weighted cost")
    probabilities, derivatives = probability_derivatives(effects, np.diag(eigenvalues), tangents)
    scores = derivatives / probabilities[:, None]
    increments = np.linalg.solve(classical, scores.T).T
    mean = probabilities @ increments
    derivative = increments.T @ derivatives
    covariance = increments.T @ (probabilities[:, None] * increments) - np.outer(mean, mean)
    errors = [np.max(np.abs(mean)), np.max(np.abs(derivative - np.eye(7))),
              np.max(np.abs(covariance - np.linalg.inv(classical)))]
    score_error = float(max(errors))
    require(score_error < 1e-12, "Exact local score estimator moments")
    return dict(spectrum=eigenvalues.tolist(), closed_form_error=qutrit_error,
                achieved_cost=cost, score_moment_error=score_error)


def calibration_cases():
    reports = []
    for d, r in ((3, 2), (7, 3)):
        for epsilon in (1e-3, 1e-6):
            lam = np.array([1 - epsilon, epsilon]) if r == 2 else np.array([0.8, epsilon, 0.2 - epsilon])
            rho = np.diag(np.r_[lam, np.zeros(d - r)])
            x = np.zeros((d, d), complex)
            x[1, r] = x[r, 1] = epsilon
            for delta in (0.0, 1e-3, 0.1):
                unitary = np.eye(d, dtype=complex)
                c, s = np.cos(delta), np.sin(delta)
                unitary[0, 0] = unitary[r, r] = c
                unitary[0, r], unitary[r, 0] = s, -s
                effects = unitary @ calibrated_effects(d, r) @ unitary.conj().T
                direct = float(classical_fisher(effects, rho, np.array([x]))[0, 0] / (4 * epsilon))
                formula = float(calibration_fraction(epsilon, lam[0], delta, r))
                error = abs(direct - formula)
                require(error < 1e-12, "Miscalibration formula against entire POVM")
                reports.append(dict(d=d, r=r, epsilon=epsilon, delta=delta,
                                    direct_fraction=direct, formula_error=error))
    return reports


def general_measurement_checks():
    rng = np.random.default_rng(699)
    reports = []
    for d, r in ((3, 1), (4, 2), (7, 3)):
        lam = np.logspace(0, -3, r)
        lam /= lam.sum()
        eigenvalues = np.r_[lam, np.zeros(d - r)]
        rho = np.diag(eigenvalues)
        tangents, cross = tangent_basis(d, r)
        quantum = quantum_fisher(eigenvalues, tangents)
        a = rng.normal(size=(3 * d, d)) + 1j * rng.normal(size=(3 * d, d))
        values, vectors = np.linalg.eigh(a.conj().T @ a)
        frame = a @ ((vectors * (values ** -0.5)) @ vectors.conj().T)
        fine = np.einsum("zi,zj->zij", frame.conj(), frame)
        coarse = fine.reshape(d, 3, d, d).sum(axis=1)
        pvm = np.asarray([np.diag(np.eye(d)[j]) for j in range(d)])
        for name, effects in (("rank_one_frame", fine), ("coarse_grained_frame", coarse), ("eigenbasis_with_zero_outcomes", pvm)):
            require(np.max(np.abs(effects.sum(0) - np.eye(d))) < 1e-12, "Test POVM completeness")
            classical = classical_fisher(effects, rho, tangents)
            ix = np.ix_(cross, cross)
            trace = float(np.trace(np.linalg.solve(quantum[ix], classical[ix])))
            require(trace <= d - r + 1e-10, "General support-rotation converse")
            if name == "rank_one_frame":
                require(abs(trace - (d - r)) < 1e-10, "Rank-one converse saturation")
            reports.append(dict(d=d, r=r, measurement=name, cross_trace=trace, budget=d - r))
        # A common physical change of basis leaves all probabilities and FI unchanged.
        u, _ = np.linalg.qr(rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d)))
        effects = calibrated_effects(d, r)
        original = classical_fisher(effects, rho, tangents)
        rotated = classical_fisher(u @ effects @ u.conj().T, u @ rho @ u.conj().T,
                                   u @ tangents @ u.conj().T)
        error = float(np.linalg.norm(original - rotated) / np.linalg.norm(original))
        require(error < 1e-10, "Unitary-coordinate invariance")
        reports.append(dict(d=d, r=r, measurement="common_unitary_rotation", relative_error=error))
    return reports


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    cases = [construction_case(d, r, exponent)
             for d, r in ((3, 1), (3, 2), (4, 2), (7, 3), (7, 6), (6, 6), (16, 3))
             for exponent in (0, 4, 8)]
    report = dict(status="pass", python=platform.python_version(), numpy=np.__version__,
                  rng_seed=699, construction=cases, qutrit_and_score=qutrit_and_score(),
                  calibration=calibration_cases(), general_measurements=general_measurement_checks())
    root = Path(__file__).resolve().parent
    report["source_sha256"] = {name: hashlib.sha256((root / name).read_bytes()).hexdigest()
                               for name in ("check_readout.py", "readout.py")}
    if args.output:
        args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(f"PASS: {len(cases)} construction cases (including 3 full-rank controls).")
    print("PASS: qutrit closed forms and exact local-score mean, derivative, covariance.")
    print(f"PASS: {len(report['calibration'])} full-POVM calibration comparisons.")
    print("PASS: general-POVM converse, zero-probability convention, unitary invariance.")
    for key in ("completeness_error", "relative_identity_error", "minimum_eigenvalue_error"):
        print(f"Maximum {key}: {max(case[key] for case in cases):.3g}")


if __name__ == "__main__":
    main()
