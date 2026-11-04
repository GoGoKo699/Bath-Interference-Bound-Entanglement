# Bath interference and the lifetime of channel entanglement

An equilibrium reservoir can destroy the ability to communicate quantum information before its noise becomes equivalent to measuring an input and preparing an output. The mechanism developed here is interference between transitions with the same Bohr frequency. It acts on coherence transfer even when all population histories are fixed.

## Reading route

1. [Model and matched thermal dynamics](model.md) defines the four-level Hamiltonian, positive bath-correlation blocks, detailed balance, units and exactly which quantities are held fixed.
2. [Exact thresholds](exact_thresholds.md) diagonalizes the infinite-temperature channel, proves its PPT boundary and constructs an explicit measure-and-prepare decomposition at its entanglement-breaking boundary.
3. [Operational meaning](operational_meaning.md) proves that the PPT boundary is exactly the point where two-way assisted quantum capacity becomes zero, using an explicit two-qubit filter before that time.
4. [Positive-temperature continuation](thermal_extension.md) supplies a rigorous finite-temperature PPT-entangled point and states the perturbations covered by that certificate.
5. [Physical interpretation and scope](interpretation.md) explains the matched comparison, the role of repeated gaps and the distinction from static channel geometry and driven population currents.

The [related-work account](../references/RELATED_WORK.md) identifies the imported results and closest comparisons. The [verification suite](../verification/README.md) independently constructs the finite matrices and checks the analytical formulas; finite checks support the written proofs without replacing them.

## Definitions and principal result

The system has dimension four. Its dissipative channel is $`\Phi_{\beta,\eta,t}=\exp(t\mathcal L_{\beta,\eta})`$, where $`\beta`$ is the dimensionless inverse temperature, $`0\le\eta\le1`$ controls bath cross-correlations, and $`t\ge0`$ is dimensionless dissipative time. The model fixes its Hamiltonian and any Lamb-shift compensation as described in [the model](model.md).

The normalized Choi state uses a four-dimensional reference:

```math
J_{\beta,\eta,t}
=(\operatorname{id}_4\otimes\Phi_{\beta,\eta,t})
\bigl(|\Omega_4\rangle\langle\Omega_4|\bigr),
\qquad
|\Omega_4\rangle=\frac12\sum_{j=0}^{3}|j,j\rangle.
```

A channel is **PPT** when this state's partial transpose on the output is positive, equivalently when output transposition composed with the channel is completely positive. A channel is **entanglement breaking (EB)** when its output is separable from every untouched reference for every input. The Choi characterization makes this equivalent to separability of $`J`$ and to a measure-and-prepare realization. A PPT-entangled Choi state therefore gives a channel that is PPT but not EB. These standard equivalences and the capacity facts are attributed in [related work](../references/RELATED_WORK.md).

At $`\beta=0`$, put

```math
r=e^{-8t},\qquad
u=e^{-(10-2\eta)t},\qquad
v=e^{-(10+2\eta)t}.
```

The exact channel criteria are

```math
\Phi_{0,\eta,t}\text{ is PPT}
\quad\Longleftrightarrow\quad r+2u+2v\le1,
```

```math
\Phi_{0,\eta,t}\text{ is EB}
\quad\Longleftrightarrow\quad r+4u\le1.
```

Let $`t_P(\eta)`$ and $`t_E(\eta)`$ be their respective unique equality times. For every $`\eta>0`$, the interval $`[t_P,t_E)`$ is nonempty. On that interval the channel has a PPT-entangled Choi state and zero two-way assisted quantum capacity. Before $`t_P`$ the capacity is strictly positive. At $`\eta=0`$, the thresholds coincide.

| Statement | Domain | Proof mechanism |
|---|---|---|
| Population generator and bare coherence self-damping are independent of interference | Every finite inverse temperature and every allowed interference | Equal-frequency cross terms transfer only coherences |
| Exact PPT and EB criteria above | Infinite temperature, full interference interpolation | Partial-transpose spectrum, positive-map obstruction and explicit EB decomposition |
| Two-way capacity is positive exactly before the PPT threshold | Infinite temperature, full interference interpolation | A fixed rank-two filter and preservation of PPT under adaptive channel use |
| Every positive interference opens a gap, with linear onset at zero interference | Infinite temperature | Threshold equations and differentiation |
| A strict PPT-entangled point occurs at positive inverse temperature | Explicit inverse temperature $`\beta=10^{-4}`$, interference $`\eta=1`$ | Exact rational margins and an analytical generator perturbation bound |

The finite-temperature result establishes persistence of the phenomenon; it does not replace the infinite-temperature formulas with unproved exact thermal thresholds.

## Why the comparison is controlled

The Hamiltonian has distinct levels and repeated transition frequencies. Adjusting the bath's ability to distinguish pathways changes only off-diagonal entries of two positive Kossakowski blocks. At every temperature, it preserves the entire classical population generator and each diagonal attenuation coefficient of an energy-basis coherence. At infinite temperature it also preserves the Liouvillian spectral gap. Full coherence eigenmodes are allowed to change: that is the mechanism that separates the two entanglement lifetimes.

The result concerns a specified family of equilibrium generators. Known symplectic channel geometry supplies the endpoint setting, while the connected Davies trajectory, matched comparison and exact thresholds for the full interpolation are developed in the pages above.
