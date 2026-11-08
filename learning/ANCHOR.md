# Educational anchor and notation

The sole educational anchor is **DDG20**: Rafał Demkowicz-Dobrzański, Wojciech Górecki, and Mădălin Guţă, *Multi-parameter estimation beyond quantum Fisher information*, J. Phys. A: Math. Theor. **53**, 363001 (2020), [DOI: 10.1088/1751-8121/ab8ef3](https://doi.org/10.1088/1751-8121/ab8ef3).

The selected text is **arXiv:2001.11742v2, 1 September 2020**: [version record](https://arxiv.org/abs/2001.11742v2), [open HTML](https://arxiv.org/html/2001.11742v2), and [open PDF](https://arxiv.org/pdf/2001.11742v2). Section and equation references below refer to this version. Its bibliography entry is [DDG20](../references/RELATED_WORK.md#ddg20).

The review supplies the estimation language used by the project. The [bridge](README.md) develops a concrete readout experiment, and the [thirty-milestone map](MILESTONES.md) orders the project's concepts. The section map supports those milestones without requiring a complete reading of the review.

## Section map

| DDG20 v2 section | Use in this project | Milestones |
| --- | --- | --- |
| [1.2](https://arxiv.org/html/2001.11742v2#S1.SS2) | States, measurement probabilities, estimators, and the local model | [M01](MILESTONES.md#m01)–[M03](MILESTONES.md#m03), [M06](MILESTONES.md#m06), [M12](MILESTONES.md#m12) |
| [2.1](https://arxiv.org/html/2001.11742v2#S2.SS1), especially Eqs. (7)–(9) | Scores, Fisher matrices, and the nominal-point score estimator | [M04](MILESTONES.md#m04)–[M06](MILESTONES.md#m06), [M25](MILESTONES.md#m25) |
| [2.2](https://arxiv.org/html/2001.11742v2#S2.SS2) | SLD normalization and the quantum benchmark | [M07](MILESTONES.md#m07), [M10](MILESTONES.md#m10) |
| [2.3](https://arxiv.org/html/2001.11742v2#S2.SS3), [2.6](https://arxiv.org/html/2001.11742v2#S2.SS6), [2.11](https://arxiv.org/html/2001.11742v2#S2.SS11) | Incompatibility, Holevo comparisons, and attainment questions | [M08](MILESTONES.md#m08), [M12](MILESTONES.md#m12), [M15](MILESTONES.md#m15), [M30](MILESTONES.md#m30) |
| [2.7](https://arxiv.org/html/2001.11742v2#S2.SS7), [2.12](https://arxiv.org/html/2001.11742v2#S2.SS12) | Nuisance parameters, parameter changes, and functionals | [M05](MILESTONES.md#m05), [M25](MILESTONES.md#m25) |
| [3.1](https://arxiv.org/html/2001.11742v2#S3.SS1), including [3.1.2](https://arxiv.org/html/2001.11742v2#S3.SS1.SSS2) | Qubit context for the qutrit example and information tradeoffs | [M09](MILESTONES.md#m09), [M13](MILESTONES.md#m13), [M22](MILESTONES.md#m22) |
| [4.5](https://arxiv.org/html/2001.11742v2#S4.SS5) | Localization and the distinction between supplied and learned calibration | [M11](MILESTONES.md#m11), [M26](MILESTONES.md#m26), [M27](MILESTONES.md#m27), [M28](MILESTONES.md#m28) |
| [4.6.3](https://arxiv.org/html/2001.11742v2#S4.SS6.SSS3) | Scope boundary for importing asymptotic results | [M11](MILESTONES.md#m11), [M26](MILESTONES.md#m26) |
| [2.10](https://arxiv.org/html/2001.11742v2#S2.SS10), [4.6.4](https://arxiv.org/html/2001.11742v2#S4.SS6.SSS4), [5.5](https://arxiv.org/html/2001.11742v2#S5.SS5) | Multiple-copy bounds, local minimax risk, geometric calibration and the FI/risk distinction | [M25](MILESTONES.md#m25), [M28](MILESTONES.md#m28), [M29](MILESTONES.md#m29) |
| [1.3](https://arxiv.org/html/2001.11742v2#S1.SS3) | Context for separating calibration, local FI, risk and verification | [M29](MILESTONES.md#m29) |

For [M14](MILESTONES.md#m14)–[M24](MILESTONES.md#m24), the mathematical development is in [construction](../science/construction.md), [optimality](../science/optimality.md), and the [qutrit example](../science/examples.md). DDG20 provides their measurement and statistical vocabulary. The explicit Fourier allocation, full fixed-rank Fisher identity, and attaining measurement are established in those project pages.

## Notation translation

| DDG20 notation | Repository notation | Meaning |
| --- | --- | --- |
| $`F`$ | $`I_M`$ or $`I`$ | Classical Fisher matrix of the selected measurement |
| $`F_Q`$ | $`J`$ | SLD quantum Fisher matrix, with the same normalization |
| $`C`$ | $`W`$ | Positive semidefinite weight in quadratic estimation loss |
| $`\Sigma`$ | $`\mathrm{Cov}(\widehat\theta)`$ or the stated MSE matrix | Estimation error matrix; the bias convention must be retained |
| $`M_m`$ | $`E_z`$ | A POVM effect; $`m`$ and $`z`$ label outcomes |
| $`\mathfrak p`$ | $`p`$ | Number of real parameters |
| $`\widetilde{\boldsymbol\theta}`$ | $`\widehat\theta`$ | Generic estimator; here $`\widetilde\theta`$ is reserved for the pilot |
| $`L_i`$ | $`L_i`$ or directional $`L_X`$ | SLD for a coordinate derivative or specified tangent |

Three symbol collisions require care. DDG20's operator tuple $`\mathbf X=(X_i)`$ in the Holevo problem is different from the project's density-matrix tangent $`X`$. Its $`J`$ in Section 2.12 is a Jacobian; the project uses $`G`$ for a functional's Jacobian and reserves $`J`$ for quantum Fisher information. Its $`r`$ in the qubit examples is a Bloch radius; the project's $`r`$ is the integer rank. The spaces on which traces act should be identified from their operands: effects act on Hilbert space, while Fisher matrices and weights act on parameter coordinates.

## Scope of the bridge

DDG20 [Section 4.6.3](https://arxiv.org/html/2001.11742v2#S4.SS6.SSS3) explicitly restricts its general quantum local asymptotic normality treatment to full-rank states. That treatment does not establish the present moving-support rank-deficient pilot result. The [project's estimator argument](../science/estimation.md#learning-the-calibration-with-a-pilot-sample) supplies its own smoothness, localization, moment, and occupied-eigenvalue assumptions. The [collective lower bound](../science/estimation.md#collective-lower-bound-without-an-unbiasedness-assumption) uses the SLD bound and a local Bayesian Cramér–Rao argument; it does not require a rank-deficient Holevo-attainment theorem.

The [source register](../references/RELATED_WORK.md) separately credits the pure-state measurement of Li16, the support-pair ingredient of Pereira20, and the refined converse of ZC26. These are research attributions for the construction and proof. DDG20 remains the single educational anchor.

## Paid calibration and the sister comparison

DDG20 Sections 2.1–2.2 provide the score and quantum-information language; Section 2.7 explains why unknown eigenvectors belong in the full information matrix; Sections 2.10–2.11 distinguish multiple-copy bounds and attainment; Section 4.5 supplies fixed-model localization context. The [paid-calibration account](../science/paid-calibration.md) supplies its own complete-record identity, exact strong/weak qutrit formulas, two-point geometric obstruction and finite binomial pilot. The adaptive ceiling uses the separately attributed support budget and chain rule. The exact continuous-Haar pair calculation is owned by [Quantum Readout Rank Threshold](https://github.com/GoGoKo699/Quantum-Readout-Rank-Threshold/blob/555c543e9928c1206b0aca1c538d1e5b812d964c/science/haar-pair-readout.md). Neither the anchor's full-rank asymptotic theory nor an ideal calibrated fraction proves a uniform shrinking-spectrum crossover.
