# Reproducible calculations

The scripts evaluate the finite POVM and its Fisher information directly from Born probabilities. They check the algebraic constants and the concrete examples in the [scientific account](../science/README.md). The analytic construction and converse prove the general theorem; finite numerical cases do not establish universal validity, bibliographic priority, or pilot-sample asymptotics.

## Run

Tested with Python **3.12.14**, NumPy **2.3.5**, and Matplotlib **3.10.8**. NumPy is the only dependency for the checks; Matplotlib generates the figure.

```bash
python -m pip install -r verification/requirements.txt
python verification/check_readout.py
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

The construction pairs are $`(d,r)=(3,1),(3,2),(4,2),(7,3),(7,6),(6,6),(16,3)`$. The $`(6,6)`$ cases are **full-rank construction controls**: the displayed POVM still exists there, but the rank-deficient optimality theorem does not apply. For $`r>1`$, the occupied eigenvalues are proportional to a geometric progression with largest-to-smallest ratio $`10^q`$, where $`q\in\{0,4,8\}`$. The pure-state case has only one occupied eigenvalue.

## Recorded result

The complete check passed. The largest residuals in the 21 construction cases were:

| Quantity | Observed maximum | Required tolerance |
| --- | ---: | ---: |
| Maximum entrywise completeness error | $`2.13\times10^{-15}`$ | $`10^{-12}`$ |
| Fisher-identity Frobenius error divided by $`\lVert J\rVert_F`$ | $`5.11\times10^{-16}`$ | $`10^{-12}`$ |
| Minimum normalized-Fisher eigenvalue error | $`1.47\times10^{-15}`$ | $`10^{-10}`$ |

The report provides the remaining residuals and calibration fractions. Large absolute entries of $`J`$ arise when an occupied eigenvalue is small, so the identity check uses a relative matrix residual. The minimum-eigenvalue check uses a Cholesky congruence with the same eigenvalues as $`J^{-1/2}IJ^{-1/2}`$.

## Figure

[plot_calibration.py](plot_calibration.py) produces [calibration.svg](../science/figures/calibration.svg) from the exact formula implemented in [readout.py](readout.py). The plotted model has rank two, dimension three, eigenvalues $`(1-\varepsilon,\varepsilon,0)`$, and a fixed error mixing the strongly occupied eigenvector with the kernel. Its comparison with direct POVM probabilities is part of the check above.

The plot illustrates sensitivity of this specified readout to calibration error. It does not claim an optimal lower bound on the samples needed to calibrate an arbitrary measurement.
