# Paid calibration near a rank boundary

An exact eigenbasis makes the calibrated rank-two qutrit readout retain one quarter of the SLD information in every direction. Learning that basis uses specimens and produces a random apparatus. To compare it with a fixed two-copy readout, keep the complete calibration record and count all specimens. Strong and weak eigenvector errors then have different consequences; one calibration mean squared error cannot determine a universal information crossover.

The [general theorem](model.md) and [fixed-state pilot argument](estimation.md#learning-the-calibration-with-a-pilot-sample) remain unchanged. This page studies a shrinking occupied eigenvalue in the smallest moving-support model. [Quantum Readout Rank Threshold](https://github.com/GoGoKo699/Quantum-Readout-Rank-Threshold) supplies the complementary fixed two-copy apparatus; its [exact continuous-Haar comparison](https://github.com/GoGoKo699/Quantum-Readout-Rank-Threshold/blob/main/science/haar-pair-readout.md) is the authoritative home of the pair calculation.

## Model and complete-record information

Use the basis $`(e_1,e_2,f)`$ and write

```math
\rho_b=\operatorname{diag}(a,b,0),\qquad a=1-b,\qquad 0\lt b\lt\tfrac12.
```

The full exact-rank-two tangent has seven real coordinates: population redistribution, the real and imaginary occupied coherence, and both quadratures of each occupied-to-empty coherence. In that order its SLD matrix is

```math
J=\operatorname{diag}\left(\frac1{ab},4,4,\frac4a,\frac4a,\frac4b,\frac4b\right).
```

Every derivative acts on the true state with the realized apparatus fixed. All limits below approach $`b=0`$ through $`b\gt0`$ on this seven-dimensional tangent stratum. The pure-state tangent at the endpoint is a different model.

Let $`Y`$ be the complete record from $`m`$ pilot copies. Conditional on $`Y`$, measure $`n=N-m`$ fresh copies with the selected one-copy POVM $`M_Y`$. Retain all pilot outcomes and randomized settings. The exact matrix identity is

```math
\boxed{I_{\rm total}=I_Y+n\,\mathbb E_Y[I_{M_Y}(\rho_b)].}
```

The joint score is the pilot score plus the sum of conditional readout scores. Each latter score has conditional mean zero, so its cross terms with the pilot score and other copies vanish. The derivative conditions on the observed $`Y`$; it never differentiates the estimated basis. This is the standard adaptive Fisher chain rule [NZ26, Section 4.3, Lemma 4.6](../references/RELATED_WORK.md#nz26).

Normalize all consumed copies by

```math
c_N=\lambda_{\min}\!\left[(NJ)^{-1/2}I_{\rm total}(NJ)^{-1/2}\right].
```

For even $`N`$, repeated pair readout has $`I_{\rm total}=(N/2)I_{\rm pair}`$ and the same fraction as $`I_{\rm pair}`$ relative to $`2J`$. If eigenvectors are unknown nuisance parameters, use the full matrix or its relevant Schur complement after summing the records. A target's scalar diagonal, an average of conditional Schur complements, and the total experiment's efficient information are generally different quantities.

## Strong-eigenvector error and nuisance coupling

Set $`c=\cos\delta`$, $`s=\sin\delta`$, and build the ten effects in the nominal basis

```math
\widetilde e_1=c e_1-s f,\qquad \widetilde f=s e_1+c f,
\qquad \widetilde e_2=e_2.
```

Consider the true weak angular tangent $`X_R=b(|e_2\rangle\langle f|+|f\rangle\langle e_2|)`$, whose quantum information is $`J_\phi=4b`$. Its imaginary quadrature has the same quantum information. The [general strong-leakage calculation](resources.md#calibration-sensitivity-for-a-weakly-occupied-direction) gives, for either quadrature,

```math
R_s(\delta)=\frac{I_\delta}{J_\phi}
=\frac b4\left[\frac{c^2}{b+a s^2}+\frac{s^2}{b+a c^2}\right].
```

Perfect calibration gives $`1/4`$. For small deterministic error, recovering this ideal fraction as $`b\downarrow0`$ requires $`\delta^2=o(b)`$. If $`b\ll\delta^2\ll1`$, the fraction is asymptotic to $`b/(4\delta^2)`$. Strong population of order $`a\delta^2`$ enters outcomes that ideally have probability of order $`b`$.

Scalar retention does not certify a simultaneous guarantee. Put $`A=b+a c^2`$ and $`B=b+a s^2`$. In $`H=J^{-1/2}I_\delta J^{-1/2}`$, the real internal/weak-coherence coordinates form the block

```math
H_{12,23}=\frac14 D
\left[\frac{u u^{\mathsf T}}A+\frac{v v^{\mathsf T}}B\right]D,
\quad D=\operatorname{diag}(1,\sqrt b),\quad
u=\begin{pmatrix}c\\-s\end{pmatrix},\quad
v=\begin{pmatrix}s\\c\end{pmatrix}.
```

The pair effects supply the first rank-one term and the weak Fourier family supplies the second. The imaginary block has the same eigenvalues. Its determinant is $`b/(16AB)`$. In the hierarchy above its trace tends to $`1/2`$, so its smaller eigenvalue is asymptotic to $`b/(8\delta^2)`$. The full model therefore has a direction less well protected than the weak scalar diagonal alone suggests.

## Weak-eigenvector error has a different limit

Instead leave $`e_1`$ fixed and use

```math
\widetilde e_2=c e_2-s f,\qquad
\widetilde f=s e_2+c f,\qquad u=\sin(2\delta).
```

This error introduces no strongly occupied population into the weak Fourier family. With $`\theta_t=2\pi t/3`$, that family's probabilities and real weak-angle derivatives are

```math
p_{2t}=\frac b6(1+u\cos\theta_t),\qquad
\partial_Rp_{2t}=\frac b3\cos(2\delta)\cos\theta_t.
```

The imaginary derivatives have magnitude $`b\sin\theta_t/3`$. Summing their squared responses and the other effect families gives, for $`|\delta|\lt\pi/4`$,

```math
\begin{aligned}
R_{w,R}
&=\frac{\cos^2(2\delta)}{4(1+u)(1-u/2)}
+\frac{b c^2s^2}{2}
\left(\frac1{a+b c^2}+\frac1{a+b s^2}\right),\\
R_{w,I}&=\frac1{4(1-u/2)}.
\end{aligned}
```

The Fisher cross term between these quadratures vanishes. Their difference away from perfect calibration reflects the three Fourier phases, rather than a rotationally symmetric continuous phase readout.

This robustness also holds for the full matrix. Separate the three weak-family outcomes, with probabilities of order $`b`$, from the seven outcomes of order one. After QFI normalization the population-to-weak cross terms vanish, the four internal/strong coordinates tend to $`\mathbb I_4/4`$, and the weak block is diagonal. Consequently the eigenvalues of $`H`$ tend to

```math
\left\{\frac12,\frac14,\frac14,\frac14,\frac14,
\frac{1-u}{4(1-u/2)},\frac1{4(1-u/2)}\right\}.
```

The convergence is uniform on compact small-angle intervals. Thus small fixed weak-only errors retain a positive fraction uniformly as $`b\downarrow0`$; they need not be $`o(\sqrt b)`$. For example, $`\delta=0.1`$ has limiting minimum approximately $`0.222427`$. The small-angle restriction matters: at $`\delta=\pi/4`$, the real weak Fourier derivative vanishes, leaving only an order-$`b`$ retained fraction from other effects. The result does not cover arbitrary errors or simultaneous strong and weak misalignment.

## Geometric calibration requirements

A calibration task must specify the accuracy it requires. There is a quantum necessary condition for attaining either strong angular error $`o(\sqrt b)`$ or weak angular error $`o(1)`$, in probability uniformly over the following alternatives.

Take two states of the same spectrum whose eigenvectors differ only by a strong-null angle $`\alpha`$ or a weak-null angle $`\beta`$. Their root fidelities are respectively

```math
f_s=b+a|\cos\alpha|,\qquad f_w=a+b|\cos\beta|.
```

For $`m`$ copies the root fidelity is $`f^m`$, and their half-trace-distance distinguishability is at most $`\sqrt{1-f^{2m}}`$ by the Fuchs–van de Graaf bound [FvG98, Theorem 1, Eq. (46)](../references/RELATED_WORK.md#fvg98). Choose $`\alpha=h\sqrt b`$ with fixed $`h\ne0`$, or a fixed small nonzero $`\beta=h`$. If $`mb`$ remains bounded, the distinguishability stays bounded away from one. The proposed uniform geometric accuracies would distinguish the respective alternatives with error tending to zero, a contradiction. Hence

```math
mb\longrightarrow\infty
```

is necessary for these calibration-consistency tasks, even allowing a collective pilot. This is not a necessary condition for retaining a constant total-record Fisher fraction: a useful readout need not produce a consistent basis estimate.

A fixed positive-definite informationally complete pilot illustrates the dependence on design. Its outcome probabilities are bounded below, while weak-angle derivatives are proportional to $`b`$, giving per-copy weak-angle FI $`\Theta(b^2)`$ and strong-angle FI $`\Theta(1)`$. A regular operator-norm state estimate of error $`O_P(m^{-1/2})`$ recovers the weak eigenvector consistently when $`mb^2\to\infty`$, because its eigengap is $`b`$. That sufficient condition belongs to this pilot, not to quantum calibration universally. No matching minimax sufficiency theorem for the complete unknown basis is asserted.

## An exact paid real-angle pilot

An explicit local example makes the nonlinear average inspectable. Suppose $`e_2`$ is known and the strong vector is $`\cos\alpha\,e_1+\sin\alpha\,f`$. The pilot measures the three laboratory projectors onto $`(e_1+f)/\sqrt2`$, $`(e_1-f)/\sqrt2`$, and $`e_2`$. Their probabilities are

```math
p_+=\frac a2(1+\sin2\alpha),\qquad
p_-=\frac a2(1-\sin2\alpha),\qquad p_2=b.
```

At the operating point $`\alpha=\phi=0`$, the pilot has strong-angle FI $`4ma`$, spectral FI $`m/(ab)`$, and zero ordinary weak-angle FI. The latter is a pointwise score statement; second-order dependence is not a uniform finite-sample impossibility result.

Let $`K_+,K_-,K_2`$ be its counts and define

```math
L=K_++K_-,\qquad D=\frac{K_+-K_-}L,\qquad
\widehat\alpha=\tfrac12\arcsin D,
```

using $`D=0`$ when $`L=0`$. Select the eigenbasis with strong vector $`\cos\widehat\alpha\,e_1+\sin\widehat\alpha\,f`$. Relative to the strong-error convention above its error at the operating point is $`\delta=-\widehat\alpha`$. Since $`R_s`$ is even,

```math
R_s(\widehat\alpha)=\frac b4\frac{1-aD^2/2}{b+a^2D^2/4},\qquad
I_{{\rm total},\phi\phi}=4b(N-m)\,\mathbb E[R_s(\widehat\alpha)].
```

Here $`L\sim\operatorname{Bin}(m,a)`$ and, conditional on $`L`$, $`K_+\sim\operatorname{Bin}(L,1/2)`$. Define $`D_{\ell k}=(2k-\ell)/\ell`$ for $`\ell\gt0`$ and $`D_{00}=0`$. The exact expectation is the finite sum

```math
\mathbb E R_s
=\sum_{\ell=0}^m\binom m\ell a^\ell b^{m-\ell}
\sum_{k=0}^{\ell}\frac{\binom\ell k}{2^\ell}
\frac b4\frac{1-aD_{\ell k}^2/2}{b+a^2D_{\ell k}^2/4}.
```

Every pilot copy and every later outcome is counted. This partially supplied-basis example does not implement a uniform full unknown-basis protocol.

The exact finite sum already rules out a universal smooth law inferred from calibration MSE. For fixed even $`m`$ and $`b\downarrow0`$, the tie event has $`D=0`$ with limiting probability $`\binom m{m/2}/2^m`$, and

```math
\mathbb E R_s\longrightarrow\frac{\binom m{m/2}}{4\,2^m}.
```

For fixed odd $`m`$ the limit is zero. These exact-calibration atoms occur at the specified operating angle and disappear under generic shifts of that angle; they do not yield a uniform unknown-basis guarantee.

For comparison only, impose a continuous Gaussian error model $`\delta=Z/\sqrt{4ma}`$ with standard normal $`Z`$. In the small-error approximation, putting $`q=1/(4mb)`$ gives

```math
\mathbb E R_s\simeq\frac14g(q),\qquad
g(q)=\sqrt{\frac\pi{2q}}\,e^{1/(2q)}
\operatorname{erfc}\!\left(\frac1{\sqrt{2q}}\right).
```

The Gaussian integral has $`g(q)\sim\sqrt{\pi/(2q)}`$ for large $`q`$, whereas substituting mean squared error into the reciprocal predicts an order-$`mb`$ fraction. For the discrete pilot, the window $`m^{-2}\ll b\ll m^{-1}`$ resolves the narrow useful-error interval with many lattice points and motivates this continuous approximation; no uniform replacement outside that window is claimed. The finite sum, not this illustrative Gaussian model, is the exact paid-pilot result.

## Adaptive ceiling and two-copy comparison

The support-rotation budget in [optimality](optimality.md#information-budget-for-support-rotations) gives $`\operatorname{tr}(J_{\mathcal C}^{-1}I_{M,\mathcal C})\le1`$ on the four-dimensional occupied-to-empty tangent subspace $`\mathcal C`$. Apply that bound to every fixed conditional apparatus along a classical adaptive history. The transcript identity then yields

```math
\operatorname{tr}(J_{\mathcal C}^{-1}I_{{\rm total},\mathcal C})\le N,
\qquad \boxed{c_N^{\rm adaptive\ one\ copy}\le\tfrac14.}
```

This includes pilot copies and arbitrary classical adaptation on fresh specimens. It excludes coherent memory joining different inputs or a multi-copy pilot. The inequality is a corollary of the inherited support budget and the chain rule, not a new budget theorem.

The sister repository gives two distinct comparisons. Its fixed finite-design apparatus guarantees at least $`1/12`$ of pair QFI uniformly over rank-two states. Its exact continuous-Haar parity-pair calculation proves

```math
c_{\rm Haar}(b)\gt\tfrac14\quad
\text{for all sufficiently small }b\gt0,
\qquad c_{\rm Haar}(b)\longrightarrow\tfrac14.
```

Both normalize by all consumed copies. Haar covariance makes the pair fraction independent of the true basis. The [authoritative proof](https://github.com/GoGoKo699/Quantum-Readout-Rank-Threshold/blob/main/science/haar-pair-readout.md) uses all four tangent classes, not just the weak scalar response. This gives a strict local full-model information separation from every adaptive one-copy protocol near the boundary without a state-dependent calibration stage. It establishes neither the finite Clifford constant, an explicit threshold, an all-spectrum ordering, an optimal pair constant, nor finite-sample risk dominance.

Thus a calibration cost, a specified pilot's total-record information, and a coherent-readout advantage are different questions. The exact formulas settle the displayed experiments and geometric task; they do not assume or establish a universal calibration-budget crossover. The [verification guide](../verification/README.md#paid-calibration-checks) reproduces the direct probabilities, full tangent matrices and finite-record identity.
