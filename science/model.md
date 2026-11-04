# A thermal bath with partially resolved transition pathways

The control parameter in this model changes whether the environment distinguishes two transitions of the same energy. It leaves the entire population dynamics and every coherence self-damping coefficient fixed. The resulting channels nevertheless have different times for losing distillable entanglement and for becoming measure-and-prepare. The exact boundaries are derived in [Exact thresholds](exact_thresholds.md), and their communication meaning is proved in [Operational meaning](operational_meaning.md).

This page defines the generator, proves its thermal detailed balance and primitivity, and identifies exactly what the comparison holds fixed. [The thermal extension](thermal_extension.md) supplies an explicit strictly positive-temperature certificate.

## Conventions and scales

The system has four energy eigenstates, labelled $`0,1,2,3`$ in the computational order $`00,01,10,11`$. Write $`F_{ij}=|i\rangle\langle j|`$, and let juxtaposition of Pauli matrices denote a tensor product. The physical Hamiltonian is

```math
H_{\mathrm{phys}}=E_0 H,
\qquad
H=3ZI+ZZ=\operatorname{diag}(4,2,-4,-2),
\qquad E_0>0.
```

All energies and Bohr frequencies below are in units of $`E_0`$. The variable $`\beta`$ means the dimensionless inverse temperature $`\beta_{\mathrm{phys}}E_0`$, with Boltzmann's constant included in the definition of physical inverse temperature. The dimensionless time is $`t=\kappa t_{\mathrm{phys}}`$, where $`\kappa>0`$ is a common dissipative rate. Thus every quoted time threshold is divided by $`\kappa`$ in physical units, and every quoted dissipative spectral gap is multiplied by $`\kappa`$.

No equality between the energy scale and the dissipative rate is assumed. The generator is a Davies weak-coupling idealization; the common rate may be taken small relative to $`E_0/\hbar`$ without changing the dimensionless conclusions. We use the interaction-picture channel

```math
\Phi_{\beta,\eta,t}=e^{t\mathcal L_{\beta,\eta}}.
```

The parameter range is $`0\le\eta\le1`$, and $`\beta`$ is finite and nonnegative. Our sign convention is

```math
[H,F_{ij}]=(E_i-E_j)F_{ij}.
```

A positive frequency therefore labels an energy-raising transition. Its rate is smaller than the reverse rate at positive inverse temperature.

## The Davies generator

For an operator $`A`$, set

```math
\mathcal D[A](\rho)
=A\rho A^\dagger-\frac12\{A^\dagger A,\rho\}.
```

For a list of transition operators $`\mathbf F=(F_1,\ldots,F_m)`$ and a positive semidefinite coefficient matrix $`C`$, define

```math
\mathcal K[C;\mathbf F](\rho)
=\sum_{a,b=1}^{m} C_{ab}
\left(F_a\rho F_b^\dagger
-\frac12\{F_b^\dagger F_a,\rho\}\right).
```

Each list below contains operators of one common positive Bohr frequency:

```math
\begin{aligned}
\mathbf F_2&=(F_{01},F_{32}),
&C_2(\eta)&=2\begin{pmatrix}1&-\eta\\-\eta&1\end{pmatrix},\\[2mm]
\mathbf F_4&=(F_{13}),
&C_4&=(4),\\[2mm]
\mathbf F_6&=(F_{03},F_{12}),
&C_6(\eta)&=2\begin{pmatrix}1&\eta\\\eta&1\end{pmatrix},\\[2mm]
\mathbf F_8&=(F_{02}),
&C_8&=(4).
\end{aligned}
```

Let $`\mathbf F_\omega^\dagger`$ denote the list of adjoints in the same order. The full dissipator is

```math
\begin{aligned}
\mathcal L_{\beta,\eta}
={}&\mathcal D[ZI]+\mathcal D[ZZ]\\
&+\sum_{\omega\in\{2,4,6,8\}}
\left[
e^{-\beta\omega/2}\mathcal K[C_\omega(\eta);\mathbf F_\omega]
+e^{+\beta\omega/2}\mathcal K[C_\omega(\eta);\mathbf F_\omega^\dagger]
\right].
\end{aligned}
```

Here $`C_4`$ and $`C_8`$ do not depend on $`\eta`$. Both two-dimensional matrices have eigenvalues $`2(1+\eta)`$ and $`2(1-\eta)`$. The generator is therefore in GKLS form throughout the stated range. The exponential rate prescription specifies a KMS-compatible family; varying $`\beta`$ is not asserted to vary the temperature of one fixed microscopic bath with unchanged couplings and spectral density.

At $`\eta=0`$, all nonzero-frequency jumps are resolved rank-one transitions. At $`\eta=1`$, the positive-frequency jumps can be chosen as

```math
\sqrt2(F_{01}-F_{32}),\qquad
2F_{13},\qquad
\sqrt2(F_{03}+F_{12}),\qquad
2F_{02},
```

together with their adjoints and the two diagonal dephasing jumps. The opposite relative signs in the frequency-2 and frequency-6 blocks are part of the specified model. The result is not a claim about every possible choice of unresolved pathways.

### The Hamiltonian part

Every jump has a definite Bohr frequency, and cross terms couple only transitions of the same frequency. Consequently,

```math
\mathcal L_{\beta,\eta}\circ\operatorname{Ad}_{e^{-isH}}
=\operatorname{Ad}_{e^{-isH}}\circ\mathcal L_{\beta,\eta}
\qquad(s\in\mathbb R).
```

For the specified physical generator

```math
\mathcal G_{\mathrm{phys}}
=-\frac{i}{\hbar}[E_0H,\cdot]+\kappa\mathcal L_{\beta,\eta},
```

the Schrödinger-picture channel differs from the interaction-picture channel only by a unitary on the output. Their PPT, entanglement-breaking, and two-way quantum-capacity thresholds coincide.

The exact model fixes this Hamiltonian part. An arbitrary additional diagonal Lamb shift need not commute with the coherence-transfer blocks merely because it commutes with $`H`$. Such a term cannot automatically be removed as an output unitary. It must either be absent or compensated, satisfy the required commutation relation, or be treated as an additional perturbation. Strict interior certificates are stable to sufficiently small generator perturbations; the exact threshold formulas are not asserted for arbitrary Lamb shifts.

## GNS detailed balance, with the rate sign checked

The faithful Gibbs state is

```math
\sigma_\beta=\frac{e^{-\beta H}}{\operatorname{tr}(e^{-\beta H})}.
```

We use the Heisenberg GNS inner product

```math
\langle X,Y\rangle_{\sigma_\beta}
=\operatorname{tr}(\sigma_\beta X^\dagger Y).
```

Let $`\mathcal L_{\beta,\eta}^{*}`$ be the trace adjoint of the Schrödinger dissipator. It is self-adjoint in this inner product. The following calculation proves this statement directly rather than inferring quantum detailed balance from a population stationary state.

Diagonalize each real symmetric matrix $`C_\omega`$ and absorb its positive eigenvalues into jump amplitudes. The resulting raising jumps $`A_\omega`$ have adjoint lowering partners and satisfy

```math
[H,A_\omega]=\omega A_\omega,
\qquad
\sigma_\beta A_\omega=e^{-\beta\omega}A_\omega\sigma_\beta.
```

For the Heisenberg jump map $`\mathcal M_A(X)=A^\dagger X A`$, cyclicity of the trace gives

```math
\begin{aligned}
\langle X,\mathcal M_{A_\omega}(Y)\rangle_{\sigma_\beta}
&=\operatorname{tr}(A_\omega\sigma_\beta X^\dagger A_\omega^\dagger Y)\\
&=e^{\beta\omega}
\operatorname{tr}(\sigma_\beta A_\omega X^\dagger A_\omega^\dagger Y)\\
&=\left\langle e^{\beta\omega}A_\omega X A_\omega^\dagger,
Y\right\rangle_{\sigma_\beta}.
\end{aligned}
```

Thus its GNS adjoint is $`\mathcal M_{A_\omega}^{\sharp}=e^{\beta\omega}\mathcal M_{A_\omega^\dagger}`$. The rate pair obeys

```math
\gamma_\beta(\omega)=e^{-\beta\omega/2},
\qquad
\gamma_\beta(-\omega)=e^{+\beta\omega/2}
=e^{\beta\omega}\gamma_\beta(\omega).
```

The two weighted jump maps are therefore each other's GNS adjoints. Moreover, $`A_\omega^\dagger A_\omega`$ and $`A_\omega A_\omega^\dagger`$ commute with $`H`$, so their anticommutator maps are individually GNS self-adjoint. The diagonal Hermitian jumps $`ZI`$ and $`ZZ`$ have the same property. Summing these terms proves

```math
\langle X,\mathcal L_{\beta,\eta}^{*}(Y)\rangle_{\sigma_\beta}
=\langle\mathcal L_{\beta,\eta}^{*}(X),Y\rangle_{\sigma_\beta}.
```

Because $`\mathcal L_{\beta,\eta}^{*}(I)=0`$, this identity also proves stationarity:

```math
\operatorname{tr}(\sigma_\beta\mathcal L_{\beta,\eta}^{*}(X))=0
\quad\text{for every }X,
\qquad
\mathcal L_{\beta,\eta}(\sigma_\beta)=0.
```

The specified Hamiltonian commutator is GNS skew-adjoint and commutes with the dissipator. Thus the full generator has the usual detailed-balance decomposition into a symmetric dissipator and a Hamiltonian part. The underlying Davies and Alicki framework is attributed under [Equilibrium generators](../references/RELATED_WORK.md#equilibrium-generators), with reference keys `davies1974markovian` and `alicki1976balance`.

## Primitivity, including maximal interference

The rank loss of $`C_2`$ and $`C_6`$ at $`\eta=1`$ does not create a dark subspace or an additional stationary state.

To see this, let $`X`$ be fixed by the Heisenberg dissipator. For any Lindblad representation with positive rates, the identity

```math
\mathcal L^*(X^\dagger X)
-\mathcal L^*(X^\dagger)X-X^\dagger\mathcal L^*(X)
=\sum_a \gamma_a[A_a,X]^\dagger[A_a,X]
```

holds. Taking the expectation in the faithful stationary state shows that $`[A_a,X]=0`$ for every jump with positive rate.

In particular, $`X`$ commutes with $`ZI`$ and $`ZZ`$. Their joint eigenspaces are the four individual energy basis vectors, so $`X`$ must be diagonal. Commutation with the transition jumps then equates its diagonal entries. At $`\eta=1`$, the collective jumps still contain the edges $`01,23,03,12`$, and the single jumps contain $`13,02`$. These form a connected graph. A commutator with a diagonal $`X`$ has independent coefficients on these matrix units, so no cancellation can evade the equality of the corresponding diagonal entries. Hence $`X`$ is scalar.

The fixed Heisenberg algebra is therefore $`\mathbb C I`$ for every finite $`\beta`$ and every $`0\le\eta\le1`$. GNS self-adjointness excludes nonzero imaginary dissipative eigenvalues. The semigroup converges to the unique faithful Gibbs state and is primitive throughout this parameter range.

## What is held fixed

### The entire population generator

Use the column convention $`\dot p=Q_\beta p`$, where $`p_j=\rho_{jj}`$. Define the symmetric off-diagonal rate matrix

```math
C=\begin{pmatrix}
0&2&4&2\\
2&0&2&4\\
4&2&0&2\\
2&4&2&0
\end{pmatrix}.
```

Then

```math
(Q_\beta)_{ij}=C_{ij}e^{-\beta(E_i-E_j)/2}\quad(i\ne j),
\qquad
(Q_\beta)_{jj}=-\sum_{i\ne j}(Q_\beta)_{ij}.
```

This matrix is independent of $`\eta`$. Its detailed balance is explicit:

```math
(Q_\beta)_{ij}(\sigma_\beta)_{jj}
=\frac{C_{ij}}{\operatorname{tr}(e^{-\beta H})}
e^{-\beta(E_i+E_j)/2}
=(Q_\beta)_{ji}(\sigma_\beta)_{ii}.
```

Thus all stationary edge currents vanish. The assertion does not exclude transient population or heat currents during relaxation from a nonequilibrium marginal.

### Coherence self-damping and coherence transfer

Let $`\Gamma_j=\sum_{i\ne j}(Q_\beta)_{ij}`$, and let

```math
z=(1,1,-1,-1),\qquad w=(1,-1,-1,1)
```

be the diagonal entries of $`ZI`$ and $`ZZ`$. For $`i\ne j`$, the coefficient of $`F_{ij}`$ in $`\mathcal L_{\beta,\eta}(F_{ij})`$ is $`-a_{ij}`$, where

```math
a_{ij}=\frac{\Gamma_i+\Gamma_j}{2}
+\frac{(z_i-z_j)^2+(w_i-w_j)^2}{2}.
```

Every $`a_{ij}`$ is independent of $`\eta`$. The changing terms are exclusively transfers between coherences of equal frequency:

```math
\begin{aligned}
\mathcal L(F_{01})&=-a_{01}F_{01}+2\eta e^{3\beta}F_{32},\\
\mathcal L(F_{32})&=-a_{32}F_{32}+2\eta e^{-3\beta}F_{01},\\
\mathcal L(F_{03})&=-a_{03}F_{03}-2\eta e^{\beta}F_{12},\\
\mathcal L(F_{12})&=-a_{12}F_{12}-2\eta e^{-\beta}F_{03}.
\end{aligned}
```

The adjoint coherences obey the adjoint equations. The remaining coherences $`F_{02},F_{13}`$ and their adjoints decay with coefficients $`a_{02},a_{13}`$ and do not mix with other coherences.

The matching can also be read directly from the jumps. Distinct transitions of the same nonzero frequency cannot share a source or target when all energy levels are nondegenerate. For such transitions, the cross anticommutator products vanish, and the cross jump map takes an off-diagonal matrix unit to another off-diagonal matrix unit. It changes neither populations nor the coefficient of a coherence in its own equation.

Equal self-damping coefficients therefore do **not** mean equal full coherence decay or equal coherence eigenmodes. At $`\beta=0`$, the return amplitude in either mixing block is $`e^{-10t}\cosh(2\eta t)`$, while its transfer amplitude has magnitude $`e^{-10t}\sinh(2\eta t)`$. The first changes at second order in weak $`\eta`$, and the second at first order.

## Infinite-temperature spectrum

At $`\beta=0`$, every population escape rate is 8 and

```math
Q_0=\begin{pmatrix}
-8&2&4&2\\
2&-8&2&4\\
4&2&-8&2\\
2&4&2&-8
\end{pmatrix}.
```

The two coherence blocks reduce to $`-10I+2\eta X`$ and $`-10I-2\eta X`$. Together with the population block and the isolated coherences, the dissipative spectrum, listed as a multiset, is

```math
0\;(1),\qquad
-8\;(1),\qquad
-(10-2\eta)\;(4),\qquad
-(10+2\eta)\;(4),\qquad
-12\;(6).
```

Parentheses give multiplicities; coincident eigenvalues at the endpoints are combined in the usual way. The dissipative spectral gap is exactly 8 for all $`0\le\eta\le1`$, or $`8\kappa`$ in physical units. The threshold separation is consequently not produced by changing the population dynamics or the slowest dissipative relaxation rate. The full Pauli solution and the exact onset laws appear in [Exact thresholds](exact_thresholds.md).

## Bath interpretation and the role of repeated gaps

The normalized matrices $`C_2/2`$ and $`C_6/2`$ can be realized as Gram matrices of two environment records with overlaps $`-\eta`$ and $`+\eta`$, respectively. Orthogonal records at $`\eta=0`$ distinguish which transition occurred. Parallel or antiparallel records at $`\eta=1`$ leave no such distinction within a frequency block. Intermediate overlaps retain partial which-transition information. The norms of both records remain fixed, which is why the individual population rates do not change. The reverse processes have the same correlation structure and the KMS-related thermal weights.

This is a change in correlations between pathways of the **same** frequency, not a failure to resolve different photon energies. The Hamiltonian has no level degeneracy: its four eigenvalues are distinct. What repeats are the gaps, at frequencies 2 and 6. A unitary CNOT change of system basis transforms $`H`$ to $`3ZI+IZ`$, but the bath jumps remain correlated; the model is not a pair of independent local thermal channels.

### Detuning and the secular order of limits

A generic detuning of the energy levels can split the repeated gaps. If that splitting is held fixed while taking the fully secular Davies weak-coupling limit, cross terms between the now-distinct frequencies average away. Sending the detuning to zero **after** that limit approaches a resolved-transition generator. It does not recover the unresolved generator at the exactly repeated gaps.

This singular order of limits is compatible with continuity of finite-dimensional channel dynamics in the generator: the fully secular construction itself changes discontinuously when Bohr-frequency equalities are removed. Small changes of rates that preserve the repeated gaps are ordinary generator perturbations and are covered by [the strict thermal certificate](thermal_extension.md). A controlled description of detunings comparable to the dissipative rate would require a suitable partial-secular or near-degenerate weak-coupling derivation; no such extension is assumed here.

The resolved endpoint belongs to the rank-one equilibrium class in *Current-Induced Bound Entanglement*. That work explicitly excludes coherence transfer between equal-frequency pathways. The present model retains equilibrium detailed balance while leaving that resolved class. See the [pinned related-project comparison](../references/RELATED_WORK.md#related-project-current-induced-bound-entanglement), reference key `currentinduced2026`, for its precise assumptions and source versions.
