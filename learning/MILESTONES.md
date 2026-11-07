# Thirty milestones for calibrated quantum readout

A source produces a state near a calibrated operating point. One measurement must retain useful information about every allowed small change of that state. These thirty milestones connect the physical setting, the finite measurement construction, its sharp information bound, and its estimation consequences.

The map has **12 background/preliminary milestones and 18 narrative/innovation milestones**. The background develops the objects needed to state the optimization precisely: states, measurements, local statistical information, the quantum metric, and allowed perturbations. The longer narrative follows the two measurement families through completeness and Fisher information, combines them with the converse, and establishes what the result means for calibration and estimation. This allocation reflects a project built around one exact construction and its consequences.

Both phases move from local objects to an integrated account. [M12](#m12) assembles the complete design problem. [M30](#m30) assembles the theorem, its mechanism, the resources it uses, and its boundaries. Detailed derivations remain in the authoritative [scientific account](../science/README.md).

## Selected educational anchor

The single educational anchor is **DDG20**: Rafał Demkowicz-Dobrzański, Wojciech Górecki, and Mădălin Guţă, *Multi-parameter estimation beyond Quantum Fisher Information*, [arXiv:2001.11742v2](https://arxiv.org/abs/2001.11742v2), 1 September 2020; J. Phys. A: Math. Theor. **53**, 363001 (2020). The [versioned HTML](https://arxiv.org/html/2001.11742v2) and [PDF](https://arxiv.org/pdf/2001.11742v2) contain the sections cited below.

The [section map](ANCHOR.md#section-map) and [notation translation](ANCHOR.md#notation-translation) connect this review to the repository. DDG20 supplies the estimation framework. The fixed-rank construction, its general-outcome converse, and the specific calibration analysis have their authoritative statements in the project pages. Research references such as Li16, Pereira20, and ZC26 identify imported ingredients; they are not additional educational anchors.

## Phase I: background and preliminaries

| ID | Target |
| --- | --- |
| [M01](#m01) | States and occupied support |
| [M02](#m02) | POVMs and probability records |
| [M03](#m03) | Local changes with a fixed apparatus |
| [M04](#m04) | Scores and classical sensitivity |
| [M05](#m05) | Fisher matrices and coordinates |
| [M06](#m06) | Local unbiasedness and weighted covariance |
| [M07](#m07) | The SLD quantum benchmark |
| [M08](#m08) | Incompatibility and measurement classes |
| [M09](#m09) | Fixed-rank tangent geometry |
| [M10](#m10) | Matrix order and worst-direction design |
| [M11](#m11) | Local statistical regimes and calibration |
| [M12](#m12) | The complete calibrated design problem |

### M01

**States and occupied support** · Background/preliminaries

- **Central question:** What do the eigenvalues and eigenvectors of a density matrix describe, and what does its rank count?
- **Understanding target:** Interpret a density matrix as a positive operator with unit trace. Distinguish the occupied support, spanned by eigenvectors with positive eigenvalues, from the kernel. Explain how a state can have few occupied directions inside a much larger physical Hilbert space.
- **Dependencies and story role:** Starting point. Establishes the state and the two subspaces on which the measurement will act.
- **Conceptual connection:** The spectral description turns rank into a physical feature of the source, while retaining the possibility that its occupied subspace may be uncertain.
- **Source pointers:** DDG20 [Section 1.2](https://arxiv.org/html/2001.11742v2#S1.SS2), for parameterized states; [Model: states and local perturbations](../science/model.md#1-states-and-local-perturbations), for support, kernel, and the exact-rank promise.

### M02

**POVMs and probability records** · Background/preliminaries

- **Central question:** How does a quantum measurement turn one specimen into a classical outcome?
- **Understanding target:** Explain a POVM as positive effects that sum to the identity, with outcome probability $`p_z=\mathrm{tr}(\rho E_z)`$. Distinguish an effect from its probability and distinguish the number of possible labels from the number of specimens consumed.
- **Dependencies and story role:** Uses [M01](#m01). Adds the operational object that will be optimized.
- **Conceptual connection:** Completeness makes the outcome probabilities sum to one. General single-copy controls and an ancillary realization can be represented by the same POVM.
- **Source pointers:** DDG20 [Section 1.2](https://arxiv.org/html/2001.11742v2#S1.SS2), Eq. (1); [Model: measurement resources](../science/model.md#3-measurement-resources-and-quantifiers); [Resources: accounting](../science/resources.md#resource-accounting).

### M03

**Local changes with a fixed apparatus** · Background/preliminaries

- **Central question:** What is held fixed when the sensitivity of a calibrated measurement is evaluated?
- **Understanding target:** Interpret a tangent as the first derivative of a physical state curve through a nominal state. Explain why differentiating $`\mathrm{tr}(\rho_\theta E_z)`$ changes the state while leaving the selected effects fixed. Distinguish calibration from knowledge of the subsequent unknown perturbation.
- **Dependencies and story role:** Uses [M01](#m01) and [M02](#m02). Separates apparatus selection from the local experiment.
- **Conceptual connection:** This distinction prevents information about the unknown parameter from entering through an illicit change of the measurement during differentiation.
- **Source pointers:** DDG20 [Section 1.2](https://arxiv.org/html/2001.11742v2#S1.SS2); [Construction: fixed calibration](../science/construction.md#state-tangent-space-and-fixed-calibration); [Model: quantifiers](../science/model.md#3-measurement-resources-and-quantifiers).

### M04

**Scores and classical sensitivity** · Background/preliminaries

- **Central question:** What feature of the probability distribution measures its response to a small parameter change?
- **Understanding target:** Interpret a score as the derivative of a log probability and Fisher information as its mean squared size. Explain the role of both the probability derivative and the outcome probability, including why a rare outcome can carry substantial relative information.
- **Dependencies and story role:** Uses [M02](#m02) and [M03](#m03). Introduces the classical sensitivity that the constructed apparatus will supply.
- **Conceptual connection:** The score connects observable outcome frequencies to first-order parameter sensitivity. It later provides an explicit estimator.
- **Source pointers:** DDG20 [Section 2.1](https://arxiv.org/html/2001.11742v2#S2.SS1), Eqs. (7)–(9); [Model: information conventions](../science/model.md#2-information-conventions); [Estimation: regular local models](../science/estimation.md#regular-local-parameter-models).

### M05

**Fisher matrices and coordinates** · Background/preliminaries

- **Central question:** How is sensitivity represented when several parameters can vary together?
- **Understanding target:** Interpret the Fisher matrix as a quadratic form assigning information to a specified parameter direction. Distinguish changing coordinates from changing the physical model. Explain why raw matrix eigenvalues depend on the units and coordinates used for parameters.
- **Dependencies and story role:** Uses [M03](#m03) and [M04](#m04). Extends one-direction sensitivity into a geometric comparison.
- **Conceptual connection:** A common physical metric is needed before information in different directions can be compared fairly.
- **Source pointers:** DDG20 [Section 2.1](https://arxiv.org/html/2001.11742v2#S2.SS1) and [Section 2.12](https://arxiv.org/html/2001.11742v2#S2.SS12); [Model: information conventions](../science/model.md#2-information-conventions); [Anchor: notation translation](ANCHOR.md#notation-translation).

### M06

**Local unbiasedness and weighted covariance** · Background/preliminaries

- **Central question:** When does inverse Fisher information bound estimation error, and how is a chosen loss represented?
- **Understanding target:** Distinguish local unbiasedness from global unbiasedness and from arbitrary pointwise performance. Interpret a covariance matrix, a positive semidefinite weight, and the scalar cost obtained by weighting covariance. Explain the inverse-sample-size scaling for repeated independent outcomes.
- **Dependencies and story role:** Uses [M04](#m04) and [M05](#m05). Connects sensitivity to an operational error criterion.
- **Conceptual connection:** Information is useful because it controls an estimator's covariance under specified conditions. A measurement guarantee and an attained cost are separate statements.
- **Source pointers:** DDG20 [Section 1.2](https://arxiv.org/html/2001.11742v2#S1.SS2), Eqs. (3)–(5), and [Section 2.1](https://arxiv.org/html/2001.11742v2#S2.SS1); [Estimation: exact local score estimator](../science/estimation.md#exact-local-score-estimator-at-a-known-nominal-point).

### M07

**The SLD quantum benchmark** · Background/preliminaries

- **Central question:** What scale compares a measurement's information with the sensitivity available in the quantum state?
- **Understanding target:** Explain the symmetric logarithmic derivative as an operator representing a state derivative through $`2X=\rho L_X+L_X\rho`$. Interpret the associated quantum Fisher form as the optimal sensitivity for an individually specified direction, and explain why every measurement's Fisher form is bounded by it.
- **Dependencies and story role:** Uses [M01](#m01), [M03](#m03), and [M05](#m05). Supplies the reference metric for the optimization.
- **Conceptual connection:** The SLD metric compares directions according to the state and the allowed perturbation, giving a coordinate-independent scale.
- **Source pointers:** DDG20 [Section 2.2](https://arxiv.org/html/2001.11742v2#S2.SS2); [Model: SLD convention](../science/model.md#2-information-conventions); [Construction: spectral metric](../science/construction.md#state-tangent-space-and-fixed-calibration).

### M08

**Incompatibility and measurement classes** · Background/preliminaries

- **Central question:** Why can measurements optimal for separate parameters fail to form one jointly optimal readout?
- **Understanding target:** Distinguish a direction-specific optimal measurement, one common measurement for several directions, individual measurements with classical adaptation, and joint measurements on several copies. Explain why the SLD cost can be smaller than the attainable multiparameter cost and why the Holevo bound addresses a different optimization.
- **Dependencies and story role:** Uses [M06](#m06) and [M07](#m07). Identifies the tradeoff that makes a common readout nontrivial.
- **Conceptual connection:** A quantum metric gives a benchmark, while measurement incompatibility determines how much of that benchmark can be realized simultaneously.
- **Source pointers:** DDG20 [Section 2.3](https://arxiv.org/html/2001.11742v2#S2.SS3), [Section 2.6](https://arxiv.org/html/2001.11742v2#S2.SS6), and [Section 2.11](https://arxiv.org/html/2001.11742v2#S2.SS11); [Estimation: individual and collective costs](../science/estimation.md#individual-and-collective-cost-comparison).

### M09

**Fixed-rank tangent geometry** · Background/preliminaries

- **Central question:** Which infinitesimal changes preserve the rank while allowing the occupied support to move?
- **Understanding target:** Explain the conditions $`X=X^\dagger`$, $`\mathrm{tr}\,X=0`$, and $`QXQ=0`$. Separate population changes, coherences within the support, and rotations from support into kernel. Explain why a zero first-order kernel block does not force the support to remain fixed.
- **Dependencies and story role:** Uses [M01](#m01), [M03](#m03), and [M07](#m07). Specifies the complete family of directions the measurement must protect.
- **Conceptual connection:** Rank is preserved by curved state paths whose support rotates. This geometry introduces directions missed by tomography confined to the occupied subspace.
- **Source pointers:** DDG20 [Section 3.1](https://arxiv.org/html/2001.11742v2#S3.SS1), as context for spectral and angular parameters; [Model: tangent space and physical paths](../science/model.md#1-states-and-local-perturbations); [Optimality: support rotations](../science/optimality.md#information-budget-for-support-rotations).

### M10

**Matrix order and worst-direction design** · Background/preliminaries

- **Central question:** How can one mathematical statement protect every local direction without choosing a loss first?
- **Understanding target:** Interpret $`I_M\succeq cJ`$ as an inequality between quadratic forms valid for every tangent. Explain why the smallest eigenvalue of $`J^{-1/2}I_MJ^{-1/2}`$ is the retained fraction in the least favorable direction, and why maximizing it is normalized E-optimal design.
- **Dependencies and story role:** Uses [M05](#m05), [M07](#m07), and [M09](#m09). Turns the common-readout task into a precise optimization.
- **Conceptual connection:** Positive matrix order compares all directional sensitivities at once. Normalization by the quantum metric makes that comparison coordinate invariant.
- **Source pointers:** DDG20 [Section 2.1](https://arxiv.org/html/2001.11742v2#S2.SS1) and [Section 2.2](https://arxiv.org/html/2001.11742v2#S2.SS2), for matrix bounds; [Model: optimization and quantifiers](../science/model.md#3-measurement-resources-and-quantifiers); [Suzuki20](../references/RELATED_WORK.md#suzuki20), for the design criterion.

### M11

**Local statistical regimes and calibration** · Background/preliminaries

- **Central question:** What separates performance at a calibrated point from learning an unknown state and controlling nearby risks?
- **Understanding target:** Distinguish nominal-point local unbiasedness, a pilot followed by a conditional fixed readout, and local asymptotic minimax risk over shrinking parameter neighborhoods. Explain why positive outcome probabilities and a fixed local positive lower bound on occupied eigenvalues support regular score calculations, while a rank-changing boundary can behave differently.
- **Dependencies and story role:** Uses [M03](#m03), [M06](#m06), [M08](#m08), and [M09](#m09). Establishes the statistical conditions needed for later operational claims.
- **Conceptual connection:** A local information theorem becomes an estimation statement only after the estimator, allowed prior information, and risk convention are specified.
- **Source pointers:** DDG20 [Section 1.2](https://arxiv.org/html/2001.11742v2#S1.SS2), [Section 4.5](https://arxiv.org/html/2001.11742v2#S4.SS5), and [Section 4.6.4](https://arxiv.org/html/2001.11742v2#S4.SS6.SSS4); [Estimation: pilot calibration](../science/estimation.md#learning-the-calibration-with-a-pilot-sample); [Resources: neighboring models](../science/resources.md#exact-rank-and-neighboring-statistical-models). DDG20's general rank-deficient QLAN limitation in [Section 4.6.3](https://arxiv.org/html/2001.11742v2#S4.SS6.SSS3) is retained; the project supplies its own pilot argument.

### M12

**The complete calibrated design problem** · Background/preliminaries

- **Central question:** What is optimized, over which directions, using which physical and statistical resources?
- **Understanding target:** State the optimization in its correct order: fix a rank-deficient nominal state, choose one single-copy POVM using its calibration, then evaluate its least retained fraction over the full fixed-rank tangent. Identify the role of known rank, eigenbasis calibration, ordinary score information, and a later choice of cost.
- **Dependencies and story role:** Integrates [M07](#m07)–[M11](#m11), together with the state and measurement objects from the start of the phase. Completes the background framework.
- **Conceptual connection:** The model's quantifiers distinguish this problem from a fixed state-independent apparatus, a direction-specific readout, and a collective measurement.
- **Source pointers:** DDG20 [Section 1.2](https://arxiv.org/html/2001.11742v2#S1.SS2) and [Section 2.11](https://arxiv.org/html/2001.11742v2#S2.SS11), for the estimation framework; [Model: resources, theorem, and boundaries](../science/model.md#3-measurement-resources-and-quantifiers); [Scientific overview](../science/README.md).

## Phase II: narrative and innovation

| ID | Target |
| --- | --- |
| [M13](#m13) | Rank-two qutrit as a physical model |
| [M14](#m14) | Resolving occupied coherences |
| [M15](#m15) | Fourier measurements against the kernel |
| [M16](#m16) | Sharing the completeness budget |
| [M17](#m17) | A finite regular measurement |
| [M18](#m18) | Fourier balance and cross-term cancellation |
| [M19](#m19) | Information from support pairs |
| [M20](#m20) | The exact Fisher identity |
| [M21](#m21) | General outcome spaces and zero probabilities |
| [M22](#m22) | The support-rotation information budget |
| [M23](#m23) | The attained rank law |
| [M24](#m24) | How model restrictions change the optimum |
| [M25](#m25) | A score estimator for every quadratic cost |
| [M26](#m26) | Learning calibration without an eigenbasis limit |
| [M27](#m27) | Rare directions and calibration error |
| [M28](#m28) | Individual versus collective local costs |
| [M29](#m29) | Attribution and verification of the contribution |
| [M30](#m30) | Synthesis: rank, calibration, and accessible information |

### M13

**Rank-two qutrit as a physical model** · Narrative/innovation

- **Central question:** What must a readout learn when two occupied levels can move inside a three-level system?
- **Understanding target:** Resolve the seven local directions of $`\mathrm{diag}(p,1-p,0)`$ into one population, two occupied-coherence, and four support-motion directions. Explain why a small occupation changes the quantum information scale without changing the dimension of this fixed-rank tangent.
- **Dependencies and story role:** Uses [M09](#m09) and [M12](#m12). Starts the narrative with the smallest mixed-state example before the general construction.
- **Conceptual connection:** A single empty level already creates a measurement requirement absent from known-support qubit tomography.
- **Source pointers:** DDG20 [Section 3.1](https://arxiv.org/html/2001.11742v2#S3.SS1), for the qubit comparison; [Example: seven local directions](../science/examples.md#1-seven-local-directions) and [information in each direction](../science/examples.md#3-information-in-each-direction).

### M14

**Resolving occupied coherences** · Narrative/innovation

- **Central question:** How can a measurement distinguish the real and imaginary coherence between two occupied eigenvectors?
- **Understanding target:** Interpret the four pair superpositions with relative phases $`1,-1,i,-i`$. Explain how their outcome changes separate two real coherence components and how their positive rank-one effects contribute to the support part of completeness.
- **Dependencies and story role:** Uses [M02](#m02), [M04](#m04), and [M13](#m13). Introduces the first measurement family and its physical role.
- **Conceptual connection:** Phase-sensitive interference converts off-diagonal state entries into changes of observable probabilities. The same pair readout is an inherited tomography ingredient.
- **Source pointers:** DDG20 [Section 1.2](https://arxiv.org/html/2001.11742v2#S1.SS2), for probability formation; [Construction: support-pair effects](../science/construction.md#support-pair-effects); [Pereira20](../references/RELATED_WORK.md#pereira20).

### M15

**Fourier measurements against the kernel** · Narrative/innovation

- **Central question:** How can one occupied vector be compared coherently with every kernel direction in one finite effect family?
- **Understanding target:** Explain the vectors formed from one occupied eigenvector and phase-weighted kernel vectors. Introduce the needed root-of-unity fact: averaging over $`N`$ equally spaced phases cancels every discrete frequency not divisible by $`N`$. Identify why $`N=2(d-r)+1`$ phases are chosen and why the vectors are unnormalized.
- **Dependencies and story role:** Uses [M01](#m01), [M02](#m02), [M09](#m09), and [M14](#m14). Introduces the second family and the Fourier prerequisite at its point of use.
- **Conceptual connection:** A pure-state Fisher-symmetric measurement can be placed in the subspace containing one occupied vector and the full kernel.
- **Source pointers:** DDG20 [Section 2.11](https://arxiv.org/html/2001.11742v2#S2.SS11), for pure-state estimation context; [Construction: Fourier effects](../science/construction.md#fourier-effects-on-one-support-vector-and-the-kernel) and [completeness](../science/construction.md#completeness); [Li16](../references/RELATED_WORK.md#li16).

### M16

**Sharing the completeness budget** · Narrative/innovation

- **Central question:** How can the pair and Fourier families coexist in one complete POVM?
- **Understanding target:** Follow the operator weights on support and kernel separately. Explain how all Fourier families sum to $`P/r+Q`$, while the pair effects supply $`(r-1)P/r`$. Identify why the common kernel can be shared among the occupied vectors without introducing an ambient-dimension loss in the retained fraction.
- **Dependencies and story role:** Uses [M14](#m14) and [M15](#m15). Assembles the local measurement ingredients into a physically valid apparatus.
- **Conceptual connection:** The completeness allocation is the mechanism that joins the two inherited ingredients. Summing the complete effects on each subspace determines the correct normalization.
- **Source pointers:** DDG20 [Section 1.2](https://arxiv.org/html/2001.11742v2#S1.SS2), for POVM normalization; [Construction: completeness](../science/construction.md#completeness) and [physical mechanism](../science/construction.md#why-the-ambient-dimension-does-not-set-the-fraction).

### M17

**A finite regular measurement** · Narrative/innovation

- **Central question:** What ensures that the complete apparatus has ordinary local scores and an explicit resource count?
- **Understanding target:** Relate its strictly positive nominal probabilities to positive occupied eigenvalues. Account for $`2rd-r`$ labeled outcomes and one specimen per readout. Distinguish this explicit size from a minimum-outcome theorem, and distinguish an ancillary POVM realization from efficient gate synthesis.
- **Dependencies and story role:** Uses [M06](#m06), [M11](#m11), and [M16](#m16). Establishes the regularity and resource conditions before evaluating the information.
- **Conceptual connection:** Positive probabilities make the subsequent Fisher and score-estimator calculations conventional. The outcome count describes the constructed apparatus without assigning an unproved computational cost.
- **Source pointers:** DDG20 [Section 2.1](https://arxiv.org/html/2001.11742v2#S2.SS1); [Construction: probabilities and outcome count](../science/construction.md#probabilities-and-outcome-count); [Resources: accounting](../science/resources.md#resource-accounting).

### M18

**Fourier balance and cross-term cancellation** · Narrative/innovation

- **Central question:** Why do the Fourier outcomes keep different support-motion components from interfering in the Fisher form?
- **Understanding target:** Connect the first and second phase averages to cancellation of diagonal–coherence and distinct-coordinate cross terms. Explain why frequencies $`a+b`$ remain below $`N=2(d-r)+1`$, and how this gives the exact contribution from each occupied-vector-plus-kernel family.
- **Dependencies and story role:** Uses [M04](#m04), [M05](#m05), [M15](#m15), and [M17](#m17). Converts the phase design into a quantitative information statement.
- **Conceptual connection:** The root-of-unity identities used for completeness also control quadratic score averages, with the extra frequency range needed for two real coherence components.
- **Source pointers:** DDG20 [Section 2.1](https://arxiv.org/html/2001.11742v2#S2.SS1), for Fisher information from probabilities; [Construction: Fisher information of the Fourier effects](../science/construction.md#fisher-information-of-the-fourier-effects).

### M19

**Information from support pairs** · Narrative/innovation

- **Central question:** What information do the four phases contribute inside the occupied block?
- **Understanding target:** Explain the pair Fisher contribution as the sum of a coherence term and a nonnegative term involving the two diagonal variations. Track the normalization by the summed occupied probabilities and distinguish this information calculation from the earlier completeness calculation.
- **Dependencies and story role:** Uses [M04](#m04), [M14](#m14), and [M17](#m17). Completes the second quantitative component needed for the full Fisher identity.
- **Conceptual connection:** A readout designed to resolve coherence can also supply population information. This additional information is why the final optimal measurement need not be isotropic.
- **Source pointers:** DDG20 [Section 2.1](https://arxiv.org/html/2001.11742v2#S2.SS1); [Construction: Fisher information of the support pairs](../science/construction.md#fisher-information-of-the-support-pairs); [Pereira20](../references/RELATED_WORK.md#pereira20), for the inherited pair-readout setting.

### M20

**The exact Fisher identity** · Narrative/innovation

- **Central question:** How do the two effect families protect the entire fixed-rank tangent simultaneously?
- **Understanding target:** Combine their contributions into $`I_M=J/(2r)`$ plus explicit nonnegative diagonal quadratic forms. Explain the all-direction lower bound, identify equality for tangents with zero occupied diagonal, and show why restriction to a smooth submodel preserves the inequality.
- **Dependencies and story role:** Uses [M07](#m07), [M09](#m09), [M10](#m10), [M18](#m18), and [M19](#m19). Integrates the construction into its central attainable guarantee.
- **Conceptual connection:** A complete measurement and two exact information calculations produce one spectrum-independent matrix inequality. The excess terms connect mixed-state anisotropy with worst-direction optimality.
- **Source pointers:** DDG20 [Section 2.2](https://arxiv.org/html/2001.11742v2#S2.SS2) and [Section 2.12](https://arxiv.org/html/2001.11742v2#S2.SS12), for metric and coordinate context; [Construction: exact Fisher identity](../science/construction.md#exact-fisher-identity); [Example: normalized information](../science/examples.md#3-information-in-each-direction).

### M21

**General outcome spaces and zero probabilities** · Narrative/innovation

- **Central question:** What measurement class must the converse cover, and how is ordinary Fisher information defined at zero probabilities?
- **Understanding target:** Explain how the trace of a POVM supplies a scalar measure and its positive operator density turns outcome sums into integrals. Use positivity to understand why a zero-probability effect has zero first derivative on the fixed-rank tangent. Distinguish the ordinary score convention from direction-dependent limiting prescriptions.
- **Dependencies and story role:** Uses [M02](#m02), [M04](#m04), [M09](#m09), and [M17](#m17). Broadens the comparison beyond the finite attaining construction.
- **Conceptual connection:** The same probability and positivity structure controls finite, countable, and continuous outcomes. General outcome spaces do not create an exception to the information budget.
- **Source pointers:** DDG20 [Section 1.2](https://arxiv.org/html/2001.11742v2#S1.SS2) and [Section 2.1](https://arxiv.org/html/2001.11742v2#S2.SS1), for the statistical framework; [Optimality: general POVMs and the score convention](../science/optimality.md#general-povms-and-the-score-convention), for the supplied extension and boundary convention.

### M22

**The support-rotation information budget** · Narrative/innovation

- **Central question:** What limits the total normalized information about rotations from support into kernel?
- **Understanding target:** Introduce the positive-matrix entry inequality $`|E_{ja}|^2\le E_{jj}E_{aa}`$ through the nonnegativity of a two-by-two principal minor. Explain how it bounds the normalized Fisher trace on the $`2r(d-r)`$ support-rotation directions by the kernel dimension $`d-r`$.
- **Dependencies and story role:** Uses [M07](#m07), [M09](#m09), [M10](#m10), and [M21](#m21). Establishes the converse's load-bearing inequality for arbitrary outcomes.
- **Conceptual connection:** Positivity constrains how much an effect can couple an occupied vector to a kernel vector. Summing those local constraints uses POVM completeness to produce a global information budget.
- **Source pointers:** DDG20 [Section 3.1.2](https://arxiv.org/html/2001.11742v2#S3.SS1.SSS2), for Gill–Massar tradeoff context; [Optimality: information budget](../science/optimality.md#information-budget-for-support-rotations); [ZC26](../references/RELATED_WORK.md#zc26), Eq. (76) and Appendix D, Eq. (172), for the inherited refined bound.

### M23

**The attained rank law** · Narrative/innovation

- **Central question:** Why is $`1/(2r)`$ the exact optimum at every rank-deficient nominal state?
- **Understanding target:** Divide the support-rotation budget by its number of real directions to bound every uniform retained fraction. Combine that converse with the explicit lower guarantee to obtain $`c_*(\rho)=1/(2r)`$. Explain why equality holds at each positive spectrum and why the pure-state case is inherited.
- **Dependencies and story role:** Uses [M12](#m12), [M20](#m20), and [M22](#m22). Closes the construction-and-converse argument.
- **Conceptual connection:** The kernel dimension appears in both the number of directions and their information budget, so it cancels. Rank remains as the number of occupied components sharing that budget.
- **Source pointers:** DDG20 [Section 2.11](https://arxiv.org/html/2001.11742v2#S2.SS11), for the distinction between a bound and attainment; [Optimality: sharp fraction](../science/optimality.md#sharp-fraction-on-the-full-tangent-space); [Model: exact rank law](../science/model.md#4-exact-rank-law); [Li16](../references/RELATED_WORK.md#li16) and [ZC26](../references/RELATED_WORK.md#zc26).

### M24

**How model restrictions change the optimum** · Narrative/innovation

- **Central question:** Why can the same nonzero spectrum lead to a different optimum when the allowed directions change?
- **Understanding target:** Compare the moving-support rank-two qutrit optimum $`1/4`$ with the known-support qubit optimum $`1/3`$. Explain why restricting a model may improve its optimum and why the support-rotation converse disappears at full rank. Keep the inherited submodel guarantee separate from equality for the full tangent.
- **Dependencies and story role:** Uses [M08](#m08), [M09](#m09), [M13](#m13), and [M23](#m23). Establishes the theorem's model dependence before interpreting its statistical consequences.
- **Conceptual connection:** An empty physical level matters when unknown motion into it is allowed. The tangent model, as well as the state, determines the design task.
- **Source pointers:** DDG20 [Section 3.1](https://arxiv.org/html/2001.11742v2#S3.SS1); [Example: why an empty level matters](../science/examples.md#4-why-an-empty-level-matters); [Model: consequences and boundaries](../science/model.md#5-consequences-and-boundaries); [Suzuki20](../references/RELATED_WORK.md#suzuki20).

### M25

**A score estimator for every quadratic cost** · Narrative/innovation

- **Central question:** How does the Fisher guarantee become an attained local covariance statement?
- **Understanding target:** Explain how averaging nominal scores and multiplying by the inverse Fisher matrix gives an exactly locally unbiased estimator with covariance $`I^{-1}/n`$. Use inverse matrix order to obtain the common factor-$`2r`$ bound for any positive semidefinite weight, including functionals and unknown nuisance coordinates. Distinguish this guarantee from separate optimality for each loss.
- **Dependencies and story role:** Uses [M04](#m04), [M06](#m06), [M10](#m10), [M17](#m17), and [M20](#m20). Gives the information theorem an explicit estimation implementation.
- **Conceptual connection:** The classical score construction is established machinery; the new readout supplies its controlled Fisher matrix. Retaining nuisance parameters in the full inverse preserves the intended statistical task.
- **Source pointers:** DDG20 [Section 2.1](https://arxiv.org/html/2001.11742v2#S2.SS1), Eq. (9), [Section 2.7](https://arxiv.org/html/2001.11742v2#S2.SS7), and [Section 2.12](https://arxiv.org/html/2001.11742v2#S2.SS12); [Estimation: exact score estimator](../science/estimation.md#exact-local-score-estimator-at-a-known-nominal-point) and [weighted losses](../science/estimation.md#weighted-losses-functionals-and-nuisance-parameters).

### M26

**Learning calibration without an eigenbasis limit** · Narrative/innovation

- **Central question:** Can a pilot estimate select a useful apparatus when positive eigenvalues are degenerate?
- **Understanding target:** Explain the two-stage protocol with all pilot copies counted. Condition on the pilot so the second-stage effects are fixed, and connect uniform probability and inverse-Fisher bounds to the one-step risk estimate. Identify the fourth-moment requirement, the choice $`1/2\lt\alpha\lt1`$ for a pilot of size $`n^\alpha`$, and the fixed-state spectral conditions.
- **Dependencies and story role:** Uses [M11](#m11), [M17](#m17), and [M25](#m25). Replaces supplied calibration by a justified pointwise implementation.
- **Conceptual connection:** The proof differentiates the state model while keeping the realized apparatus fixed. Uniform conditional bounds permit arbitrary measurable eigenbasis choices at degeneracy and establish local risk control without asserting a limiting estimator distribution.
- **Source pointers:** DDG20 [Section 4.5](https://arxiv.org/html/2001.11742v2#S4.SS5), for localization context, with the scope limit in [Section 4.6.3](https://arxiv.org/html/2001.11742v2#S4.SS6.SSS3); [Estimation: pilot argument](../science/estimation.md#learning-the-calibration-with-a-pilot-sample) and [degenerate eigenvalues](../science/estimation.md#degenerate-positive-eigenvalues). The fixed-rank proof is supplied locally.

### M27

**Rare directions and calibration error** · Narrative/innovation

- **Central question:** Why can a small basis error spoil a guarantee that is independent of the nominal spectrum?
- **Understanding target:** Follow the stated error that rotates a strongly occupied vector toward the kernel. Explain how background of order $`\Lambda\delta^2`$ enters outcomes intended to resolve a weak occupation $`\varepsilon`$, and identify $`\Lambda\delta^2/\varepsilon`$ as the relevant leakage ratio. Keep this readout calculation separate from a lower bound on calibration sample complexity.
- **Dependencies and story role:** Uses [M04](#m04), [M13](#m13), [M17](#m17), and [M26](#m26). Exposes the material limitation of exact calibration.
- **Conceptual connection:** Spectrum-independent measurement coefficients do not make the apparatus insensitive to eigenvector error. Rare-outcome information and finite calibration accuracy interact.
- **Source pointers:** DDG20 [Section 4.5](https://arxiv.org/html/2001.11742v2#S4.SS5), for local applicability context; [Resources: exact calibration-error calculation](../science/resources.md#calibration-sensitivity-for-a-weakly-occupied-direction); [Example: calibration and verification](../science/examples.md#5-calibration-and-verification).

### M28

**Individual versus collective local costs** · Narrative/innovation

- **Central question:** What does the sharp Fisher fraction imply about the actual benefit of collective measurements?
- **Understanding target:** Explain the local asymptotic minimax risk convention and the inequalities relating individual, collective, and SLD costs. Connect the individual upper bound to the score estimator and the collective lower bound to a local Bayesian Cramér–Rao argument. Distinguish the sharp Fisher constant from the upper factor $`2r`$ for true costs and from the attributed known-support advantage $`r+1`$.
- **Dependencies and story role:** Uses [M08](#m08), [M11](#m11), [M23](#m23), [M25](#m25), and [M26](#m26). Integrates the readout theorem with the broader multiparameter estimation problem.
- **Conceptual connection:** A universal covariance guarantee gives a controlled individual strategy, while a lower bound on every collective strategy supplies the comparison. These two optimizations need not have the same sharp constant.
- **Source pointers:** DDG20 [Section 2.10](https://arxiv.org/html/2001.11742v2#S2.SS10), [Section 4.6.4](https://arxiv.org/html/2001.11742v2#S4.SS6.SSS4), and [Section 5.5](https://arxiv.org/html/2001.11742v2#S5.SS5); [Estimation: cost comparison](../science/estimation.md#individual-and-collective-cost-comparison) and its final known-support example; [Das25](../references/RELATED_WORK.md#das25).

### M29

**Attribution and verification of the contribution** · Narrative/innovation

- **Central question:** Which parts of the result are inherited, which are established by the assembled construction, and what do finite checks verify?
- **Understanding target:** Identify the pure-state, pair-readout, refined-converse, and local-estimation inputs. State the specific all-spectrum calibrated attainment supplied by their assembly. Compare its quantifiers and loss with state-independent randomized readout and global tomography. Explain what direct POVM and Fisher calculations check without treating a finite suite as the universal proof.
- **Dependencies and story role:** Uses [M20](#m20), [M22](#m22), [M23](#m23), [M27](#m27), and [M28](#m28). Places the complete result within its evidence and prior-work context.
- **Conceptual connection:** Scientific attribution and reproduction depend on identifying the exact question, assumptions, and output of each result. Similar rank scaling does not by itself identify the same theorem.
- **Source pointers:** DDG20 [Section 1.3](https://arxiv.org/html/2001.11742v2#S1.SS3), for the distinction among estimation approaches; [Related work](../references/RELATED_WORK.md), especially Li16, Pereira20, ZC26, and NZ26; [Verification guide](../verification/README.md); [Scientific overview: attribution](../science/README.md#attribution-and-verification).

### M30

**Synthesis: rank, calibration, and accessible information** · Narrative/innovation

- **Central question:** What can one calibrated single-copy apparatus establish about every small fixed-rank change of a quantum state?
- **Understanding target:** Give one connected account of the allowed tangent model, the two measurement families and their shared completeness budget, the exact fraction $`1/(2r)`$, and the matching support-rotation converse. Relate the finite outcome count and common cost guarantee to the required calibration, the conditional pilot result, and the separate collective-cost question.
- **Dependencies and story role:** Integrates [M12](#m12), [M23](#m23), and [M24](#m24)–[M29](#m29). Completes the narrative at the level of the whole scientific contribution.
- **Conceptual connection:** Rank controls how the occupied vectors share access to kernel directions. Calibration makes the attainable fraction spectrum-independent at the operating point, while model restrictions and finite calibration accuracy determine the boundaries of that conclusion.
- **Source pointers:** DDG20 [Section 1.2](https://arxiv.org/html/2001.11742v2#S1.SS2) and [Section 2.11](https://arxiv.org/html/2001.11742v2#S2.SS11), for the overall estimation and attainment framework; [Scientific overview](../science/README.md); [Model: theorem and scope](../science/model.md#4-exact-rank-law); [Estimation](../science/estimation.md); [Resources](../science/resources.md).
