# Estimation with the calibrated measurement

The [explicit measurement](construction.md) gives an attainable local estimation cost, because its outcome probabilities are strictly positive and its Fisher matrix is nonsingular on every identifiable parameter model. At a known nominal state, a score estimator attains its classical Cramér–Rao covariance exactly. At an unknown but fixed regular state, a vanishing fraction of copies can provide the calibration under the local conditions stated below.

The exact theorem in [optimality](optimality.md) concerns the best uniform fraction of SLD Fisher information retained by one readout. Its estimation consequence is an upper factor of $`2r`$ relative to the SLD cost, and hence relative to the optimal local asymptotic minimax collective cost defined below. Sharpness of the Fisher fraction does not assert sharpness of that collective-cost factor.

See [the model](model.md) for the fixed-rank tangent space and Fisher convention, [resources](resources.md) for measurement and calibration accounting, and [related work](../references/RELATED_WORK.md) for attribution.

## Regular local parameter models

Let $`\theta\mapsto\rho_\theta`$ be a smooth model on an open subset of $`\mathbb R^p`$, with an interior operating point $`\theta_0`$. Assume that the rank is exactly $`r`$ in a neighborhood of $`\theta_0`$ and that its identifiable tangent map is injective there. Thus the pulled-back SLD Fisher matrix $`J_0`$ is positive definite. The main setting is $`2\le r\lt d`$.

Construct $`M_{\rho_{\theta_0}}=\{E_z\}`$ in an eigenbasis of the nominal state, and hold every effect fixed as $`\theta`$ varies. Define

```math
p_z(\theta)=\operatorname{tr}(\rho_\theta E_z),
\qquad
s_z=\left.\nabla_\theta\log p_z(\theta)\right|_{\theta=\theta_0},
\qquad
I_0=\sum_z p_z(\theta_0)s_zs_z^{\mathsf T}.
```

All $`p_z(\theta_0)`$ are positive. Since there are finitely many outcomes, the probabilities remain positive in a sufficiently small neighborhood; smoothness of the state model then gives ordinary smooth classical scores. Pulling back the quadratic identity in [construction](construction.md#exact-fisher-identity) gives

```math
I_0\succeq\frac1{2r}J_0\succ0.
```

Any parameterization with redundant directions should first be reduced to identifiable coordinates. The formulas below use inverses on that identifiable space.

## Exact local score estimator at a known nominal point

The score-estimator construction is standard; see [DDG20, Section 2.1, Eq. (9)](../references/RELATED_WORK.md#ddg20). Applying it to the positive-probability readout gives the following explicit covariance guarantee.

Measure $`n`$ independent copies with the same fixed POVM and let $`Z_1,\ldots,Z_n`$ be their outcomes. The estimator

```math
\widehat\theta_n
=\theta_0+I_0^{-1}\frac1n\sum_{i=1}^{n}s_{Z_i}
```

is locally unbiased at $`\theta_0`$ and has covariance

```math
\boxed{
\operatorname{Cov}_{\theta_0}(\widehat\theta_n)
=\frac1n I_0^{-1}
\preceq\frac{2r}{n}J_0^{-1}.
}
```

Here local unbiasedness means

```math
\mathbb E_{\theta_0}\widehat\theta_n=\theta_0,
\qquad
\left.\frac{\partial}{\partial\theta_b}
\mathbb E_\theta[\widehat\theta_{n,a}]
\right|_{\theta=\theta_0}
=\delta_{ab}.
```

To verify these statements, normalization gives

```math
\sum_z p_z(\theta_0)s_z=0.
```

Differentiation of the expected score, with its evaluation point and the measurement still fixed at $`\theta_0`$, gives

```math
\left.\frac{\partial}{\partial\theta_b}
\sum_zp_z(\theta)s_{z,a}\right|_{\theta=\theta_0}
=\sum_z p_z(\theta_0)s_{z,b}s_{z,a}
=(I_0)_{ab}.
```

Finally, the score has covariance $`I_0`$ at the nominal point, and the copies are independent. The covariance formula follows directly. No asymptotic attainability assumption is needed for this calibrated, locally unbiased statement.

The estimator returns local coordinates. It need not lie inside the physical parameter domain on every finite record; a localized or constrained estimator can instead be used for asymptotic state estimation. The local calculation also does not make it a globally unbiased estimator away from $`\theta_0`$.

## Weighted losses, functionals, and nuisance parameters

For any real positive semidefinite quadratic weight $`W`$, inverse-matrix monotonicity gives

```math
\operatorname{tr}(W I_0^{-1})
\le 2r\operatorname{tr}(W J_0^{-1}).
```

This includes singular weights. If $`\theta=(\psi,\eta)`$ contains parameters of interest $`\psi`$ and nuisance parameters $`\eta`$, use the Fisher matrices for the complete identifiable vector. A weight

```math
W=
\begin{pmatrix}
W_\psi&0\\
0&0
\end{pmatrix}
```

selects the relevant block of the inverse without treating the nuisance coordinates as known. Equivalently, writing the efficient Fisher matrices as Schur complements,

```math
I_{\psi\cdot\eta}
=I_{\psi\psi}-I_{\psi\eta}I_{\eta\eta}^{-1}I_{\eta\psi},
\qquad
J_{\psi\cdot\eta}
=J_{\psi\psi}-J_{\psi\eta}J_{\eta\eta}^{-1}J_{\eta\psi},
```

one has

```math
I_{\psi\cdot\eta}^{-1}
\preceq 2rJ_{\psi\cdot\eta}^{-1}.
```

For a differentiable estimable functional $`g(\theta)`$ with Jacobian $`G`$ at the nominal point, the same conclusion follows by replacing the coordinate weight with $`G^{\mathsf T}W_gG`$.

The common measurement is therefore valid for every such loss or restriction of the model. It need not minimize the cost of an individual restricted problem; for example, a single-parameter model has its own SLD-optimal readout.

## Learning the calibration with a pilot sample

A precise pointwise asymptotic implementation can be given without requiring nondegenerate occupied eigenvalues. The following conditions specify the statistical scope of this implementation.

- The dimension, rank, model, and true point are fixed as the sample size grows.
- The model is $`C^3`$ on a neighborhood of a compact identifiable parameter region containing $`\theta_0`$ in its interior. On that neighborhood, the rank is exactly $`r`$, the smallest occupied eigenvalue is bounded below by a positive constant, and the pulled-back SLD matrix is positive definite.
- The region provides localization to the intended parameter branch. A preliminary estimator $`\widetilde\theta`$ based on $`n_0`$ copies has fourth moment $`\mathbb E_{\theta_0}\|\widetilde\theta-\theta_0\|^4=O(n_0^{-2})`$, with a probability of failed localization that is $`o(n^{-1})`$. These conditions can be supplied by regular classical estimation from a finite informationally complete pilot measurement on a compact identifiable local model.

The positive constants in these assumptions are local analysis constants, not promises uniform over all rank-$`r`$ states.

### A regular pilot measurement

One can choose the pilot POVM with positive definite effects. Starting from any finite informationally complete POVM $`\{H_a\}`$ with nonzero effects, set, for a fixed $`0<\eta<1`$,

```math
\widetilde H_a
=(1-\eta)H_a
+\eta\frac{\operatorname{tr}H_a}{d}\mathbb I.
```

These effects sum to $`\mathbb I`$, are positive definite, and remain informationally complete: on trace-zero perturbations their derivatives are simply multiplied by $`1-\eta`$. Consequently the pilot has positive outcome probabilities and positive classical Fisher information on every identifiable tangent of the local model.

On a fixed compact identifiable region, concentration of its empirical outcome frequencies and a smooth local inverse or localized likelihood estimator give root-$`n_0`$ accuracy and the required moments. A bounded fallback estimate handles the event outside the chosen localization neighborhood. This step selects a local parameter branch; local identifiability alone does not resolve a separate global aliasing problem.

### Second-stage estimator

Choose

```math
n_0=\lceil n^\alpha\rceil,
\qquad \frac12<\alpha<1,
\qquad n_1=n-n_0.
```

Use the pilot to estimate the state within the rank-$`r`$ model, choose its eigenbasis measurably, and build $`M_{\rho_{\widetilde\theta}}`$. Conditional on the pilot record, this POVM is fixed for the remaining $`n_1`$ copies. For its probabilities, define

```math
\begin{aligned}
p_z(\theta;\widetilde\theta)
&=\operatorname{tr}\!\left(
\rho_\theta E_z(\widetilde\theta)\right),\\
\widetilde s_z
&=\left.\nabla_\theta
\log p_z(\theta;\widetilde\theta)
\right|_{\theta=\widetilde\theta},\\
\widetilde I
&=\sum_zp_z(\widetilde\theta;\widetilde\theta)
\widetilde s_z\widetilde s_z^{\mathsf T}.
\end{aligned}
```

The derivative in the second line acts on the first argument only. A one-step estimator is

```math
\widehat\theta_n
=\widetilde\theta
+\widetilde I^{-1}\frac1{n_1}
\sum_{i=1}^{n_1}\widetilde s_{Z_i}.
```

The conditional Fisher guarantee is

```math
\widetilde I\succeq
\frac1{2r}J(\widetilde\theta).
```

To obtain its risk, put $`\Delta=\widetilde\theta-\theta_0`$. Taylor expansion of $`p_z(\theta_0;\widetilde\theta)`$ about its first argument $`\widetilde\theta`$ gives, conditional on the pilot,

```math
\mathbb E_{\theta_0}[\widetilde s_Z\mid\text{pilot}]
=-\widetilde I\Delta+O(\|\Delta\|^2),
```

and

```math
\operatorname{Var}_{\theta_0}
(\widetilde s_Z\mid\text{pilot})
=\widetilde I+O(\|\Delta\|).
```

The remainder bounds are uniform over the calibrated measurements in this local region. Indeed, their nominal probabilities obey the explicit positive lower bounds in [construction](construction.md#probabilities-and-outcome-count), their effects have bounded operator norm, and the state model has uniformly bounded derivatives on the region.

It follows that the conditional bias of the one-step estimator is $`O(\|\Delta\|^2)`$, while its conditional covariance is

```math
\frac1{n_1}\left[
\widetilde I^{-1}+O(\|\Delta\|)
\right].
```

The fourth-moment condition makes the scaled squared bias vanish:

```math
n\,\mathbb E\|\Delta\|^4
=O\!\left(\frac{n}{n_0^2}\right)
\longrightarrow0.
```

Also $`n/n_1\to1`$ and $`J(\widetilde\theta)\to J_0`$. A bounded extension on the localization-failure event contributes $`o(n^{-1})`$ to the risk. Hence

```math
\boxed{
\limsup_{n\to\infty}
 n\,\mathbb E_{\theta_0}
 \left[(\widehat\theta_n-\theta_0)^{\mathsf T}
 W(\widehat\theta_n-\theta_0)\right]
\le 2r\operatorname{tr}(WJ_0^{-1}).
}
```

If the pilot moment and localization bounds hold uniformly on a fixed smaller neighborhood of $`\theta_0`$, the same argument gives, for each fixed $`H<\infty`$,

```math
\begin{aligned}
\limsup_{n\to\infty}\ 
\sup_{\|h\|\le H}\ 
n\,\mathbb E_{\theta_0+h/\sqrt n}
\bigl[
&(\widehat\theta_n-\theta_0-h/\sqrt n)^{\mathsf T}\\
&\qquad W(\widehat\theta_n-\theta_0-h/\sqrt n)
\bigr]
\le 2r\operatorname{tr}(WJ_0^{-1}).
\end{aligned}
```

The regular pilot construction above supplies these uniform bounds after restricting to a compact neighborhood inside the identifiable region. This is a uniform local risk statement. Convergence to a particular limiting distribution is not used, including when the selected eigenbasis does not converge.

### Degenerate positive eigenvalues

The argument never differentiates the selected eigenbasis. For each realized pilot estimate, any orthonormal basis within a degenerate occupied eigenspace and any orthonormal kernel basis can be used. All such choices satisfy the same Fisher inequality and the same local probability lower bounds. Consequently the Taylor and moment argument does not require a continuously selected eigenbasis, a nonzero gap between distinct occupied eigenvalues, or convergence to a particular basis inside a degenerate block.

The occupied support must remain separated from the kernel in this fixed local region. The calibration example in [resources](resources.md#calibration-sensitivity-for-a-weakly-occupied-direction) explains why this pointwise pilot result does not supply a uniform finite-sample calibration cost when the smallest positive eigenvalue tends to zero.

## Individual and collective cost comparison

We use local asymptotic minimax costs, which require control of an unknown local perturbation and allow biased estimators. Let $`\mathsf A=\mathrm{ind}`$ denote protocols measuring one copy at a time with classical adaptation, and let $`\mathsf A=\mathrm{coll}`$ denote protocols allowing joint measurements of the $`n`$ copies. A protocol includes its estimator.

For a fixed positive semidefinite weight $`W`$ and a local radius $`H`$, define

```math
\begin{aligned}
R_{n,H}^{\mathsf A}(W)
=\inf_{\mathcal S_n\in\mathsf A}
\sup_{\|h\|\le H}
n\,\mathbb E_{\theta_0+h/\sqrt n}^{\mathcal S_n}
\bigl[
&(\widehat\theta_n-\theta_0-h/\sqrt n)^{\mathsf T}\\
&\qquad W(\widehat\theta_n-\theta_0-h/\sqrt n)
\bigr],
\end{aligned}
```

and

```math
C_{\mathsf A}(W)
=\lim_{H\to\infty}\liminf_{n\to\infty}
R_{n,H}^{\mathsf A}(W).
```

The protocol may depend on the known model, local center $`\theta_0`$, weight, radius, and sample size, but not on the unknown $`h`$. For every fixed radius, the parameter ball lies inside the model domain for sufficiently large $`n`$. The outer limit exists as an extended nonnegative number because the risks are nondecreasing in $`H`$. This definition does not require convergence of an estimator's distribution. The exact finite-sample locally unbiased result proved above remains a separate statement.

Write

```math
C_{\mathrm{SLD}}(W)
=\operatorname{tr}(WJ_0^{-1}).
```

### Attainable individual upper bound

For the fixed measurement and score estimator calibrated at $`\theta_0`$, Taylor expansion gives bias $`O(H^2/n)`$ and covariance $`n^{-1}[I_0^{-1}+O(H/\sqrt n)]`$, uniformly over $`\|h\|\le H`$. Thus

```math
\limsup_{n\to\infty}
\sup_{\|h\|\le H}
n\,\mathbb E_{\theta_0+h/\sqrt n}
\bigl[
(\widehat\theta_n-\theta_0-h/\sqrt n)^{\mathsf T}
W(\widehat\theta_n-\theta_0-h/\sqrt n)
\bigr]
=\operatorname{tr}(WI_0^{-1}).
```

This fixed-center protocol is admissible in the local minimax definition. The pilot construction additionally supplies the uniform upper bound without a supplied calibration, under its stated uniform local conditions. Consequently,

```math
C_{\mathrm{ind}}(W)
\le 2r C_{\mathrm{SLD}}(W).
```

### Collective lower bound without an unbiasedness assumption

Choose a smooth probability density $`\pi(u)`$ supported in the unit ball of $`\mathbb R^p`$, vanishing at its boundary, with finite prior Fisher matrix

```math
K_\pi=\int
(\nabla\log\pi(u))(\nabla\log\pi(u))^{\mathsf T}
\pi(u)\,du.
```

Use the local prior $`\theta=\theta_0+(H/\sqrt n)u`$. Its Fisher matrix in the $`\theta`$ coordinates is $`nK_\pi/H^2`$. Denote expectation over this prior by $`\mathbb E_\pi`$.

For every collective protocol, its outcome Fisher matrix obeys

```math
I_n(\theta)\preceq J(\rho_\theta^{\otimes n})
=nJ(\theta).
```

The equality is SLD additivity for independent input copies. Recorded classical randomization and adaptive measurements also define POVMs on these copies, so the same bound applies to them. The ordinary score convention suffices for the bound, including outcomes whose probability vanishes at particular parameters.

The matrix Bayesian Cramér–Rao inequality, obtained by integration by parts against the smooth prior, bounds the mean squared error of any estimator with finite Bayes risk:

```math
\begin{aligned}
n\,\mathbb E_\pi\mathbb E_\theta
\bigl[(\widehat\theta_n-\theta)
(\widehat\theta_n-\theta)^{\mathsf T}\bigr]
&\succeq
\left[
\frac1n\mathbb E_\pi I_n(\theta)
+\frac{K_\pi}{H^2}
\right]^{-1}\\
&\succeq
\left[
\mathbb E_\pi J(\theta)+\frac{K_\pi}{H^2}
\right]^{-1}.
\end{aligned}
```

The prior has no boundary term, and its support lies in the local parameter ball. Supremum risk is at least Bayes risk, so the bound holds after taking the infimum over collective protocols. For fixed $`H`$, continuity of $`J`$ gives $`\mathbb E_\pi J(\theta)\to J_0`$ as $`n\to\infty`$. Sending $`H\to\infty`$ then removes the prior Fisher term. Hence

```math
C_{\mathrm{coll}}(W)
\ge C_{\mathrm{SLD}}(W).
```

This proves the SLD lower bound for the stated local minimax costs, without requiring local unbiasedness or a limiting distribution for competing estimators. Together with the individual upper bound, it yields

```math
\boxed{
C_{\mathrm{ind}}(W)
\le 2r C_{\mathrm{coll}}(W).
}
```

This compares actual measurement classes; it does not replace the individual optimum by a lower bound on that optimum. If $`C_H(W)`$ is the Holevo bound for the same local model, then $`C_H(W)\ge C_{\mathrm{SLD}}(W)`$ also gives $`C_{\mathrm{ind}}(W)\le2rC_H(W)`$. Identifying the Holevo bound with the collective optimum requires its appropriate attainability result, but that identification is unnecessary for the displayed comparison with $`C_{\mathrm{coll}}`$.

The exact constant $`c_*(\rho)=1/(2r)`$ in [optimality](optimality.md) is a statement about a common measurement and the SLD metric. In a multiparameter model, the SLD cost can be smaller than the attainable collective cost. Thus the exact Fisher theorem does not determine an exact worst-case collective enhancement of $`2r`$.

## Attributed context: a collective advantage of $`r+1`$

The maximally mixed tomography example giving a factor equal to dimension plus one is prior work; see Das et al., Theorem 2 and Sec. 5.6, [Quantum 9, 1867 (2025)](https://doi.org/10.22331/q-2025-09-30-1867), and [related work](../references/RELATED_WORK.md). Its known-support version places the upper factor above in context.

For tomography within a known $`r`$-dimensional support, take $`\rho_0=\mathbb I_r/r`$ and an orthonormal traceless Hermitian coordinate basis. There are $`m=r^2-1`$ parameters and

```math
J_0=r\mathbb I_m,
\qquad W=J_0,
\qquad C_{\mathrm{SLD}}=m.
```

The locally unbiased operator tuple given by that coordinate basis has covariance matrix $`\mathbb I_m/r`$ and zero imaginary covariance. Hence $`C_H=C_{\mathrm{SLD}}=m`$; standard full-rank collective attainability applies within the known support. Gill–Massar in dimension $`r`$ gives, for individual readout,

```math
\operatorname{tr}(J_0^{-1}I)\le r-1,
\qquad
\operatorname{tr}(J_0I^{-1})
\ge\frac{m^2}{r-1}=m(r+1).
```

The Haar rank-one POVM, or a finite weighted projective 2-design, attains $`I=J_0/(r+1)`$. Its fixed-center score estimator gives the corresponding local minimax upper bound.

For the matching local minimax lower bound, conditional Fisher information adds under classical adaptation. Applying Gill–Massar at each parameter value yields

```math
\operatorname{tr}\!\left(J(\theta)^{-1}I_n(\theta)\right)
\le n(r-1).
```

For fixed $`H`$, the local prior above has $`J(\theta)\to J_0`$ uniformly as $`n\to\infty`$. The Bayesian Cramér–Rao bound and the matrix arithmetic–harmonic mean inequality therefore give, uniformly over adaptive individual protocols,

```math
n\,\text{Bayes risk for }W=J_0
\ge
\frac{m^2}{
r-1+o(1)+
\operatorname{tr}(J_0^{-1}K_\pi)/H^2
}.
```

Taking the same limits proves $`C_{\mathrm{ind}}\ge m(r+1)`$ for the local minimax definition, including biased estimators. Together with collective attainability and the individual upper bound, this gives

```math
\frac{C_{\mathrm{ind}}}{C_{\mathrm{coll}}}=r+1.
```

Embedding this model in a larger ambient Hilbert space preserves its exact rank. For $`r\ge2`$, the worst true collective advantage across the admitted models therefore lies between $`r+1`$ and $`2r`$. These bounds establish linear rank dependence; the sharp uniform Fisher fraction and the sharp collective-cost ratio remain distinct optimization problems.
