# Physical interpretation and scope

[Scientific entrypoint](README.md) · [Model](model.md) · [Exact thresholds](exact_thresholds.md) · [Operational meaning](operational_meaning.md) · [Thermal extension](thermal_extension.md)

## What the reservoir changes

Population relaxation records how probability moves between energy levels. It does not determine how a bath combines transition amplitudes. Two transitions with the same energy difference can appear in a common frequency block. Correlations between their bath couplings then transfer one system coherence into another.

The [model](model.md) uses this freedom in a controlled way. Its nondegenerate four-level Hamiltonian has repeated gaps at two frequencies. The diagonal entries of the bath-correlation blocks stay fixed, while their off-diagonal entries are proportional to $`\eta`$. Resolving the pathways means setting these cross-correlations to zero. Increasing $`\eta`$ makes their jump amplitudes interfere with the specified relative signs.

The comparison fixes more than a relaxation time. It fixes the full population generator, so the population evolution agrees for every initial population distribution. It also fixes the bare self-damping coefficient of every energy-basis coherence. The changed terms transfer coherences between transitions in the same Bohr-frequency sector. The resulting coherence eigenmodes, and their decay rates, can therefore differ.

At infinite temperature, the smallest nonzero decay rate is eight throughout the interpolation, in the chosen time units. Thus a single spectral-gap comparison also misses the entanglement distinction. The full Liouvillian spectra are not fixed; the exact solution uses precisely their changed coherence sectors.

## Two losses of quantum functionality

The Choi state compares the noisy system with an untouched reference. There are two distinct boundaries:

- At $`t_P`$, the state becomes PPT. For this family, a fixed local two-level projection proves distillability at every earlier time. Consequently $`t_P`$ is exactly the loss of positive two-way assisted quantum capacity.
- At $`t_E`$, the Choi state becomes separable. The channel is then a measure-and-prepare channel and destroys entanglement with every reference, irrespective of the input.

For $`\eta>0`$, the state between those times is entangled but cannot be distilled into maximally entangled pairs by local operations and classical communication. The channel can still distribute that bound entanglement by sending half of a locally prepared maximally entangled state. It cannot support a positive asymptotic quantum communication rate, even with unlimited two-way classical communication.

These claims use independent, identically implemented channel calls, unentangled initial laboratories, arbitrary local processing and free two-way classical communication. The capacity sign does not give its numerical value before the boundary. It also does not determine the unassisted capacity, secret-key capacity, or possible usefulness when combined with additional nonlocal resources.

At maximal interference the thresholds are particularly simple:

```math
t_P(1)=\frac{\log2}{4},\qquad
t_E(1)=\frac{\log5}{8},\qquad
t_E(1)-t_P(1)=\frac{\log(5/4)}8.
```

For weak interference, if $`t_0=t_P(0)=t_E(0)`$ and $`s_0=e^{-10t_0}`$, then

```math
t_P(\eta)=t_0+O(\eta^2),\qquad
t_E(\eta)-t_P(\eta)
=\frac{t_0s_0}{1+s_0}\,\eta+O(\eta^2).
```

The delay in complete entanglement breaking is therefore first order in the bath cross-correlation, whereas the communication boundary shifts only at second order near the resolved limit. The [threshold proof](exact_thresholds.md) derives these laws without fitting numerical data.

## Why detailed balance does not force the boundaries to agree

Every generator in the model satisfies quantum detailed balance with its Gibbs state. No driving or nonzero stationary population current is required. A state relaxing toward equilibrium can still have transient energy currents; detailed balance is a property of the generator and its stationary state, not a claim that every evolving input is already at equilibrium.

The [related resolved-jump theorem](../references/RELATED_WORK.md) shows why the jump structure matters. In that narrower setting, each population transition has its own rank-one jump, and coherence evolution has no equal-frequency transfer of the present kind. The equality of PPT and EB times in that setting does not extend merely by retaining the same population generator and detailed balance. Here the off-diagonal bath-correlation blocks relax the resolved-jump hypothesis.

The static geometry at $`\eta=1`$ is also known from symplectic channel studies. The contribution of the present construction is to connect it to a specified thermal Markov generator and a matched resolved limit, then obtain exact time boundaries for the full $`1,4,4,6`$ Pauli-sector interpolation. The [attribution account](../references/RELATED_WORK.md) separates this construction from known static geometry, eventual entanglement breaking and earlier noise-generated bound entanglement.

## Temperature, degeneracy and perturbations

The exact threshold equations cover $`\beta=0`$. The [thermal certificate](thermal_extension.md) proves a strict PPT-entangled point at $`\beta=10^{-4}`$ and establishes continuity around that point. This is a genuine positive-inverse-temperature example with a faithful Gibbs state. It is not an exact finite-temperature phase diagram, nor a uniform weak-interference statement at a fixed positive inverse temperature.

The energy levels are nondegenerate; the Bohr frequencies are not all distinct. The parameter $`\eta`$ measures bath distinguishability of pathways with *exactly the same* frequency. It is not a phenomenological instruction to retain rapidly oscillating terms between distinct frequencies in a fully secular master equation.

That distinction matters under detuning. If detuning splits a repeated gap and one subsequently takes the fully secular weak-coupling limit, the cross terms can disappear. Small perturbations of the already specified finite-time generator are covered by a strict-interior norm argument. Those perturbations are different from changing the Hamiltonian and rebuilding a fully secular generator in a singular limiting procedure. A diagonal Lamb shift also needs care: commuting with the system Hamiltonian alone does not guarantee commutation with the coherence-transfer dissipator. The exact formulas use the Hamiltonian and compensation stated in the model.

The construction uses positive bath-correlation matrices with a particular sign pattern. It proves an available equilibrium mechanism, rather than a universal effect of all unresolved transitions. The four-level realization and its mathematical thermal-bath parameters are explicit; a platform-specific reservoir implementation and a claim of minimum possible system dimension are outside the established result.

## What the verification adds

The [verification suite](../verification/README.md) assembles the generator directly from matrix jumps, exponentiates its finite Liouville representation, and compares the resulting Choi operators with the analytical solution. It also checks detailed balance, population matching, the EB decomposition and the thermal example. These independent finite calculations expose basis, normalization, sign and multiplicity errors. General positivity, threshold necessity and sufficiency, distillation and thermal robustness rest on the written arguments and their cited ingredients.
