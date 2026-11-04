# A rigorous positive-temperature bound-entangled channel

The exact onset laws in [Exact thresholds](exact_thresholds.md) are proved at infinite temperature. Their physical mechanism is not confined to a maximally mixed stationary state: the Davies model in [Model](model.md) has a strictly PPT, non-entanglement-breaking channel at the explicit positive dimensionless inverse temperature $`\beta=10^{-4}`$. Here $`\beta=\beta_{\mathrm{phys}}E_0`$ and $`t=\kappa t_{\mathrm{phys}}`$ as defined in the model page.

The proof uses strict spectral margins at $`\beta=0`$ and a quantitative channel perturbation bound. It certifies a neighborhood of admissible thermal generators, not merely a single exactly symmetric point. It does not give exact finite-temperature onset times or a uniform weak-interference theorem at fixed positive temperature.

## A strict reference point

Set $`\eta=1`$ and choose

```math
q=e^{-4t_*}=\frac{12}{25},
\qquad
t_* = \frac14\log\frac{25}{12}.
```

For a channel $`\Phi`$, use the normalized Choi state

```math
J(\Phi)=(\mathrm{id}_4\otimes\Phi)
(|\Omega_4\rangle\langle\Omega_4|),
\qquad
|\Omega_4\rangle=\frac12\sum_{i=0}^{3}|i,i\rangle.
```

Partial transpose $`\Gamma`$ acts on the output factor. Let the Breuer–Hall positive map be

```math
\mathcal B(X)=\mathrm{tr}(X)I-X-VX^TV^\dagger,
\qquad V=YI,\qquad V^T=-V.
```

Positivity follows directly: for a unit vector $`\psi`$, the vectors $`\psi`$ and $`V\overline\psi`$ are orthogonal, so $`\mathcal B(|\psi\rangle\langle\psi|)`$ is the identity minus two orthogonal rank-one projections. A negative eigenvalue of $`(\mathrm{id}\otimes\mathcal B)(J)`$ therefore certifies entanglement. See the attribution of [the Breuer–Hall witness](../references/RELATED_WORK.md#the-breuerhall-witness), reference keys `breuer2006criterion` and `hall2006indecomposability`, and the comparison with [known static symplectic geometry](../references/RELATED_WORK.md#static-symplectic-channel-geometry).

The partial-transpose spectrum and witness calculation proved in [Exact thresholds](exact_thresholds.md) give

```math
m_P:=\lambda_{\min}\!\left(J(\Phi_{0,1,t_*})^\Gamma\right)
=\frac{(1-2q)(1+q)^2}{16}
=\frac{1369}{250000}
=0.005476,
```

and

```math
\langle\Omega_4|\,(\mathrm{id}\otimes\mathcal B)
J(\Phi_{0,1,t_*})\,|\Omega_4\rangle
=\frac{1-5q^2}{8}
=-\frac{19}{1000}.
```

Both inequalities are strict: this is an interior point of the PPT region with an entanglement witness of nonzero margin.

## Bounding the change of the thermal generator

An equivalent representation of the $`\eta=1`$ model is convenient for a conservative norm bound. Define

```math
\mathcal S=\{IY,XI,XX,XZ,YI,YX,YZ,ZI,ZX,ZZ\},
```

and split each Pauli operator into its Bohr components relative to the specified $`H`$:

```math
A_{P,\omega}
=\sum_{E_i-E_j=\omega}P_{ij}F_{ij}.
```

Then the generator in [Model](model.md) is exactly

```math
\mathcal L_{\beta,1}
=\sum_{P\in\mathcal S}\sum_{\omega:A_{P,\omega}\ne0}
e^{-\beta\omega/2}\mathcal D[A_{P,\omega}].
```

There are 26 nonzero components. In the order displayed in $`\mathcal S`$, their counts are $`2,4,2,4,4,2,4,1,2,1`$. Each component is a partial permutation matrix with phases, so its operator norm is at most one; every frequency obeys $`|\omega|\le8`$. This representation also makes clear that the infinite-temperature generator is the sum of the ten Hermitian Pauli dissipators after secularization.

For the diamond norm, left and right multiplication imply

```math
\|\mathcal D[A]\|_\diamond\le2\|A\|_\infty^2.
```

Since $`\beta\ge0`$,

```math
\left|e^{-\beta\omega/2}-1\right|\le e^{4\beta}-1.
```

The triangle inequality therefore yields the explicit bound

```math
\boxed{\;
\|\mathcal L_{\beta,1}-\mathcal L_{0,1}\|_\diamond
\le52(e^{4\beta}-1).
\;}
```

The count includes two zero-frequency terms whose actual contribution to the difference is zero; keeping them only makes the bound more conservative.

## Passing from generators to channels and witnesses

Duhamel's formula gives

```math
\begin{aligned}
\Phi_{\beta,1,t}-\Phi_{0,1,t}
=\int_0^t
\Phi_{\beta,1,t-s}
(\mathcal L_{\beta,1}-\mathcal L_{0,1})
\Phi_{0,1,s}\,ds.
\end{aligned}
```

Both propagators are CPTP and have diamond norm one. Hence

```math
\|\Phi_{\beta,1,t}-\Phi_{0,1,t}\|_\diamond
\le52t(e^{4\beta}-1).
```

At $`t=t_*`$, write $`\delta=52t_*(e^{4\beta}-1)`$ and let $`\Delta J`$ be the difference of the normalized Choi states. Then

```math
\|\Delta J\|_1\le\delta.
```

Partial transpose is not being used as a trace-norm contraction. The required operator-norm bound instead follows through the Hilbert–Schmidt norm:

```math
\|\Delta J^\Gamma\|_\infty
\le\|\Delta J^\Gamma\|_2
=\|\Delta J\|_2
\le\|\Delta J\|_1
\le\delta.
```

Both channels preserve trace, so their Choi states have the same input marginal $`I/4`$. The reduction term in the Breuer–Hall output consequently cancels in their difference:

```math
(\mathrm{id}\otimes\mathcal B)(\Delta J)
=-\Delta J-(I\otimes V)\Delta J^\Gamma(I\otimes V^\dagger).
```

Its operator norm is at most $`2\delta`$. Eigenvalue perturbation for the partial transpose gives

```math
\lambda_{\min}(J(\Phi_{\beta,1,t_*})^\Gamma)
\ge\frac{1369}{250000}-\delta,
```

while the expectation in the same fixed witness vector obeys

```math
\langle\Omega_4|\,(\mathrm{id}\otimes\mathcal B)
J(\Phi_{\beta,1,t_*})\,|\Omega_4\rangle
\le-\frac{19}{1000}+2\delta.
```

Thus strict PPT entanglement is certified whenever

```math
52t_*(e^{4\beta}-1)\lt \frac{1369}{250000}.
```

This condition also makes the fixed witness expectation strictly negative because $`2(1369/250000)\lt 19/1000`$, and therefore the Breuer–Hall output has a negative eigenvalue. No assertion about its globally smallest eigenvector is needed.

## An entirely explicit positive inverse temperature

Take $`\beta=10^{-4}`$, so $`4\beta=1/2500`$. No numerical matrix exponential is needed to verify the certificate. The elementary estimates

```math
e^x-1\lt \frac{x}{1-x}\quad(0\lt x\lt 1),
\qquad
t_*\lt \frac{3}{16}
```

give

```math
\delta
\lt 52\frac{3}{16}\frac1{2499}
=\frac{39}{9996}
\lt \frac{1369}{250000}.
```

For the second estimate, $`e^{3/4}>1+3/4+(3/4)^2/2+(3/4)^3/6=269/128>25/12`$, so $`\log(25/12)\lt 3/4`$. All inequalities in the certificate are therefore strict and can be checked using rational numbers. Direct evaluation of the conservative expression gives $`\delta\approx0.0038174`$, but the rational comparison already proves the result.

It follows that the finite-temperature, primitive, GNS-detailed-balanced channel $`\Phi_{10^{-4},1,t_*}`$ is PPT and not entanglement breaking. Its Choi state is bound entangled across input reference versus system. Adding the specified commuting Hamiltonian part preserves this classification, as explained in [Model](model.md).

## Open neighborhoods in time and admissible rates

The strict inequalities provide robustness, rather than a statement confined to an isolated parameter value. For example, use the rational bound $`\bar\delta=39/9996`$ and define

```math
\bar m_P=\frac{1369}{250000}-\bar\delta>0,
\qquad
\bar m_B=\frac{19}{1000}-2\bar\delta>0.
```

Any CPTP channel within diamond distance

```math
\epsilon_{\mathrm{ch}}\lt \min\{\bar m_P,\bar m_B/2\}
```

of $`\Phi_{10^{-4},1,t_*}`$ remains strictly PPT with a negative Breuer–Hall eigenvalue. For a nearby GKLS generator $`\widetilde{\mathcal L}`$ and a nearby positive time $`\widetilde t`$, a sufficient estimate is

```math
\|e^{\widetilde t\widetilde{\mathcal L}}
-e^{t_*\mathcal L}\|_\diamond
\le
\widetilde t\,\|\widetilde{\mathcal L}-\mathcal L\|_\diamond
+|\widetilde t-t_*|\,\|\mathcal L\|_\diamond,
\qquad \mathcal L=\mathcal L_{10^{-4},1}.
```

The same representation bounds $`\|\mathcal L\|_\diamond\le52e^{4\beta}`$. Sufficiently small changes of time and jump coefficients therefore preserve a nonempty interval of PPT-entangled channels.

To retain the thermal interpretation, perturbations must remain valid Davies generators for the stated Hamiltonian: keep the repeated-frequency blocks, preserve positivity of their coefficient matrices, and pair reverse rates by the KMS relation. Continuity does not turn an arbitrary generator perturbation into a detailed-balanced one.

Nor is robustness restricted to the rank-one coefficient blocks at $`\eta=1`$. The explicit matrices give

```math
\|\mathcal L_{\beta,\eta}-\mathcal L_{\beta,1}\|_\diamond
\le8(1-\eta)\bigl(\cosh\beta+\cosh3\beta\bigr).
```

Indeed, only the two cross terms at each of the frequencies $`\pm2,\pm6`$ change, their cross anticommutator products vanish, and each remaining map $`X\mapsto F_aXF_b^\dagger`$ has diamond norm at most one. Values $`\eta\lt 1`$ sufficiently close to one therefore retain the strict thermal certificate. At such points both two-dimensional coefficient matrices are positive definite, so the result persists in an ordinary open neighborhood within the admissible rate parameters, rather than relying on maximal bath overlap.

For every fixed $`\eta>0`$, an interior time in the exact infinite-temperature interval similarly has strict PPT and witness margins. Continuity supplies some positive-temperature neighborhood for that fixed $`\eta`$. Its size may shrink as $`\eta\to0`$.

## Scope of the thermal result

The following distinctions are essential:

- The all-$`\eta`$ onset formulas and the linear weak-interference opening law are proved at $`\beta=0`$.
- At positive temperature, the present theorem proves a strict PPT-entangled channel and nearby intervals for explicit faithful Davies generators. It does not determine their exact PPT or EB onset times.
- There is no theorem here that every positive temperature supports the mechanism, or that arbitrarily weak interference works at each fixed positive temperature. A temperature neighborhood obtained for one fixed $`\eta`$ is not uniform in $`\eta`$.
- The small explicit inverse temperature reflects the conservatism of a simple norm certificate. It is not an asserted physical threshold, and failure of the bound is not evidence of separability.
- The operational proof of positive two-way capacity at every time before PPT onset is established for the exactly solved $`\beta=0`$ family in [Operational meaning](operational_meaning.md). No exact positive-capacity boundary is inferred at $`\beta>0`$.
- The time/rate neighborhood keeps the model's Bohr-frequency structure. Splitting the repeated gaps and then taking a fully secular limit is a different operation, discussed in [Model](model.md).

The purpose of this extension is precise: the separation between PPT and entanglement-breaking behavior survives in a genuine finite-temperature detailed-balanced dynamics with a nondegenerate Hamiltonian. It is not a claim that thermal bound entanglement itself is new; the relevant state-level and channel-level antecedents are separated in [Related work](../references/RELATED_WORK.md).
