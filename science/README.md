# Scientific overview

Quantum Fisher information describes the local sensitivity available in a quantum state. A measurement converts that state into ordinary outcome probabilities. When several parameters matter at once, one measurement can lose information in some directions even if another measurement would be optimal for each direction separately. This project asks for the largest common fraction that can be preserved throughout the full local model of a rank-deficient mixed state.

The [model](model.md) makes that question precise as an SLD-normalized minimum-eigenvalue design problem. At a fixed nominal rank-$`r`$ state in dimension $`d\gt r`$, the exact optimum is $`1/(2r)`$. The result includes arbitrary positive occupied spectra and all motions of the occupied subspace into the kernel.

## Why rank enters

There are $`2r(d-r)`$ real support-rotation directions. The known support-rotation refinement of Gill–Massar bounds their total normalized classical information by $`d-r`$. Their average therefore cannot exceed $`1/(2r)`$. This argument supplies a necessary upper bound, but alone does not show that one measurement can attain it while still measuring all variations inside the occupied support. [Optimality](optimality.md) states the inherited bound and gives a proof for arbitrary outcome spaces.

The [construction](construction.md) fills that gap using two effect families. Fourier phases measure each occupied vector against the whole kernel, assigning exactly the fraction $`1/(2r)`$ to every support-rotation direction. Four-phase pair measurements fill the remaining completeness weight inside the occupied subspace. The two families form one finite POVM. Their Fisher cross terms cancel, leaving the target fraction of the full SLD metric plus an explicitly positive diagonal surplus.

Adding empty dimensions increases the number of outcomes needed by this construction. It also increases the support-rotation information budget in the same proportion as the number of those directions. The optimal retained fraction consequently depends on the number of occupied vectors sharing that budget.

## Proof and interpretation route

| Read | Purpose |
| --- | --- |
| [Model](model.md) | Fix the optimization, ordinary-score convention, smooth rank stratum, and quantifiers. |
| [Construction](construction.md) | Verify positivity, completeness, all outcome probabilities, and the exact Fisher identity. |
| [Optimality](optimality.md) | Apply the support-rotation budget to arbitrary POVMs and obtain equality of the lower and upper bounds. |
| [Examples](examples.md) | Work through ten effects and seven tangent coordinates for a rank-two qutrit. |
| [Estimation](estimation.md) | Build the local score estimator, account for pilot calibration, and derive weighted-risk comparisons. |
| [Resources](resources.md) | Separate physical readout control from calibration and statistical model inputs. |
| [Paid calibration](paid-calibration.md) | Compare strong/weak errors, complete adaptive records, and a fixed two-copy readout near a rank boundary. |

The [qutrit example](examples.md) illustrates a consequential model distinction. Within a known two-dimensional support, a qubit readout can retain one third of the SLD information in every direction. Allowing that support to move into an empty third level enlarges the local model and lowers the sharp common fraction to one quarter. The occupied spectrum can remain unchanged throughout this comparison.

## Calibration is part of the model

The POVM is built in an eigenbasis of the nominal state and frozen when the probabilities are differentiated. Its coefficients require no occupied-eigenvalue values. The statistical estimator still needs nominal probabilities and model derivatives; a pilot can supply an estimated local operating point.

The [pilot argument](estimation.md#learning-the-calibration-with-a-pilot-sample) is pointwise at a fixed state with its positive spectrum bounded away from zero locally. It permits degenerate occupied eigenvalues because it never differentiates the selected eigenbasis. The [calibration calculation](resources.md#calibration-sensitivity-for-a-weakly-occupied-direction) shows why the finite-sample constants cannot be read off from the rank alone: a small basis error can leak a strongly occupied component into an outcome intended to resolve a much weaker one.

## Complete records near a shrinking occupied eigenvalue

The [paid-calibration account](paid-calibration.md) replaces an uncharged basis-error estimate by its full statistical experiment. With all copies counted, its Fisher matrix is the pilot matrix plus the expected conditional second-stage matrix. The strong and weak occupied eigenvectors have different sensitivity to misalignment; nuisance coupling also prevents a scalar target fraction from certifying a full-matrix guarantee.

The account proves a necessary $`mb\to\infty`$ condition for explicitly stated geometric calibration-consistency tasks and evaluates one paid real-angle pilot exactly. Neither statement is a universal total-information crossover. The same conditional information budget bounds the full-model fraction of every adaptive one-copy protocol by $`1/4`$.

[Quantum Readout Rank Threshold](https://github.com/GoGoKo699/Quantum-Readout-Rank-Threshold) studies the complementary coherent resource. Its [exact Haar pair calculation](https://github.com/GoGoKo699/Quantum-Readout-Rank-Threshold/blob/c4356840cb334f93b3e8367870b79fee45f937c2/science/haar-pair-readout.md) gives a state-independent readout with a strictly higher full-model minimum fraction for sufficiently small positive $`b`$. Both experiments use ordinary local FI on the rank-two tangent stratum, with every copy counted. This comparison does not identify a finite-sample risk ordering or a sharp finite-design constant.

## Attribution and verification

The pure-state Fisher-symmetric ingredient, occupied-pair construction, and optimality bound come from established work. The [source comparison](../references/RELATED_WORK.md) places their finite calibrated combination on the full intermediate-rank tangent against the closest measurement and tomography results. It also distinguishes this local design problem from global tomography risk and from state-independent measurement apparatuses.

The [reproducible checks](../verification/README.md) evaluate the Born-rule probabilities directly and compare them with the analytic formulas. They include equal and unequal spectra, full-rank construction controls, zero-probability outcomes in other measurements, and a deliberately miscalibrated example. These checks guard the constants and conventions; the general theorem is supplied by the analytic proofs above.
