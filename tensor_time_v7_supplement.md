# Tensor Time v7 — Supplement to v6
## New Results, Corrections, and the TFFT v3.0 Integration

**Jason Richardson (HistoryViper)**  
Independent Researcher  
github.com/historyViper/Best_QCD_Mass_Model  
Zenodo: 10.5281/zenodo.19798271  
May 2026

*This document is a supplement to Tensor Time v6 (April 2026).*  
*Read v6 first for the full technical framework.*  
*TFFT v3.0 is the canonical overview document — start there.*

---

## How the Paper Ecosystem Works

Three documents, three levels:

| Document | Level | What it is |
|----------|-------|-----------|
| **TFFT v3.0** | Overview | Start here. Single postulate → all results. No prerequisites. |
| **Tensor Time v6** | Technical reference | Full toroid machinery, Hamiltonian closure table, gluon lifecycle, Jacobson, black holes. Read after TFFT. |
| **This supplement (v7)** | New results since v6 | Lattice QCD connection, observer-Noether term, v2 corrections. Append to v6. |

The companion papers (GBP Maxwell, Yang-Mills, W/Z/Higgs, Lattice QCD) are
specialist papers on individual sectors. They are fully self-contained and
can be read independently.

---

## What Changed from v6 to v7

### Corrections

**1. Lepton mass formula — v2 exponential discarded**

v6 carried forward TFFT v2's formula m_n = m_Planck × exp(−n/π) as a
working approximation. This is now replaced.

The correct mechanism is mod-12 mirror pairs:

```
Z₁₂* = {1, 5, 7, 11}   (coprime to 12 = 2² × 3)
P₁₂(r) = sin²(rπ/6) = 1/4   for all r ∈ Z₁₂*   (exact)
```

Mirror pairs (sum = 12):
- Pair A {1, 11} → electron generation
- Pair B {5, 7} → muon generation  
- Cross-term: Pair A × Pair B interference → tau (naturally heavier, not a higher harmonic)

The exponential formula gave muon at ~+4%, tau at ~+9%. More importantly
it gave the wrong mechanism — the masses are not a simple harmonic series.
They are products of modular arithmetic on the same 4-lane structure, where
the interference cross-term produces the third generation.

Full lepton mass calculation from this mechanism is in progress.

**2. MOND scale — cosmological tracking removed**

v6 referenced TFFT v2's a₀ = c²/(2πR_H). This is replaced by:

```
a₀ = (c² / R_beat) · tan(π/30)
```

where R_beat is the T1 Möbius beat wavelength — a fixed geometric constant
from the 6° beat angle between the Möbius and parallelogram grids. At the
present epoch R_beat ≈ 2πR_H (within ~10%), which is why the v2 formula
worked locally. But v3 predicts **a₀ does not track cosmic expansion.**

Testable with JWST at z=1–2: if a₀ is constant, v3 is correct.

---

### New Results (not in v6)

**3. Observer-Noether term — wavefunction collapse derived** **(D)**

The GOE/GUE sheet assignments in the GBP mass code were previously
determined empirically. v7 identifies the Lagrangian term that produces them:

```
L_observer = LU · Q_N(r̂) · ψ̄ γ^μ (∂_μχ) ψ
```

where χ is the temporal curvature field (local time dilation), Q_N is the
Noether charge (Q₈ = 7/2 hadronic, Q₄ = 1 leptonic), and LU is the
universal projection scale.

Physical meaning:

- **∂_μχ = 0:** observer and particle in same time frame → GOE (no preferred
  chirality, time-reversal symmetric, unobserved state)
- **∂_μχ ≠ 0:** observer in different time frame → chirality selected by the
  gradient → GUE (measured state)

**Wavefunction collapse is the Euler-Lagrange solution for ψ under this term.**
The spinor component aligned with ∂_μχ is selected. This is not a postulate
added to the framework — it is a consequence of the observer being a particle
with its own χ-field configuration.

The GOE/GUE sheet assignments previously treated as inputs are now outputs:
- J=3/2 decuplet (Delta, Sigma*, Xi*): symmetric spin, net ∂_μχ ≈ 0 → GOE = S0 ✓
- J=1/2 octet: one anti-aligned quark, nonzero coupling → GUE = S1 ✓  
- Heavy baryons (charm/bottom): large Malus weight at high-mass lanes → S2 ✓

**4. Lattice QCD structural identity** **(D)**

The GBP projection weight P(r) = sin²(rπ/15) and the standard lattice QCD
mode weight w(r,N) = sin²(rπ/N) are related at N=30 by an exact identity:

```
P(r) = 4cos²(rπ/30) · sin²(rπ/30)   for all r ∈ Z₃₀*
```

The factor 4cos²(rπ/30) is the **Lüscher-Weisz O(a²) improvement correction**
— the rectangle term that improved lattice actions add to reduce discretization
errors. GBP's projection is exactly the Lüscher-Weisz improved lattice weight,
restricted to the 8 coprime modes.

This means GBP may be the **analytic closed-form solution** that lattice QCD
approximates numerically. The restriction to Z₃₀* is what improved lattice
actions are trying to achieve perturbatively with rectangle corrections.

**Testable prediction:** The gluon spectral function (Ilgenfritz et al. 2018,
arXiv:1701.08610) should show quasi-particle peak heights at ratios:

```
{1,29} : {13,17} : {11,19} : {7,23} = 0.0437 : 0.1673 : 0.5584 : 1.0000
```

Reading four peak heights from Figure 10 of that paper is sufficient to test this.
Companion script: `gbp_lattice_comparison.py`

**5. Beta function sum rule** **(D)**

```
Q₈ = Σ_{r ∈ Z₃₀*} P(r) = 7/2 = b₀(n_f=6)/2
```

where b₀(n_f) = 11 − 2n_f/3 is the QCD one-loop beta function coefficient.
This is an exact algebraic identity. It connects the Noether charge of the
Z₃₀* winding system to the UV behavior of the strong coupling — and derives
six quark flavors as the unique solution. The number of flavors is not fitted;
it is forced by the geometry.

**6. Mass gap from P(0) = 0** **(D)**

The Yang-Mills mass gap has a one-line geometric proof:

```
P(0) = sin²(0) = 0   →   colorless singlet has zero Noether charge
                     →   cannot propagate (Schur's lemma)
                     →   minimum excitation energy Δ = α_IR × Λ_QCD > 0
```

This is topological, not dynamical. P(0) = 0 is an algebraic identity that
survives all averaging and coarse-graining operations. The gap does not close
in the continuum limit because it is not set by a running coupling — it is
set by the fixed geometric fact that sin²(0) = 0.

Full treatment in: `gbp_yang_mills_v4.md`

**7. QCD continuum limit from Fourier averaging** **(D)**

The discrete projection weights have an exact decomposition:

```
sin²(rπ/15) = 1/2 − (1/2)cos(2rπ/15)
              └── DC ──┘  └─── AC ────┘
```

The AC term averages to zero over large volumes by the Riemann-Lebesgue lemma.
In the continuum limit:

```
⟨P(r)⟩ → 1/2
```

Substituting into the discrete Wilson action recovers:

```
S_cont = ∫ d⁴x (1/4) F_{μν}^a F^{aμν}
```

— the exact Yang-Mills and Maxwell actions. The 1/2 is not a fitting parameter;
it is the DC term of the exact Fourier decomposition of sin²(rπ/15).

This closes the loop between the discrete GBP framework and continuum QFT:
the continuum limit of the Z₃₀*-restricted path integral is standard Yang-Mills.

Full treatment in: `GBP_Maxwell_paper_v3.4.md`

---

## Updated Derivation Count

As of v7, the framework derives the following from T=c + mod-30 geometry:

| Observable | Value | Error | Status |
|-----------|-------|-------|--------|
| 54 baryon/pentaquark masses | 0.274% MAPE | 15.07 MeV RMSE | ✓ Confirmed |
| Higgs VEV v | 245.928 GeV | 0.029% | ✓ Confirmed |
| Weinberg angle θ_W | 28.47° | 0.28° | ✓ Confirmed |
| W/Z mass ratio | cos(θ_W) = φ/√(1+φ²) | 0.26% | ✓ Confirmed |
| Optical reflection floor R_min | 1.093% | 0 violations | ✓ 83/83 materials |
| Yang-Mills mass gap Δ | 184.2 MeV | — | ✓ Derived |
| Number of gluons | 8 = φ(30) | exact | ✓ Derived |
| Number of quark flavors | 6 from Q₈=b₀/2 | exact | ✓ Derived |
| MOND scale a₀ | constant, no drift | — | H, testable |
| Gluon spectral weight ratios | 0.0437:0.1673:0.5584:1.0000 | — | H, testable |
| CKM CP violation ρη | sin²(π/15) | — | H |
| Riemann 1/(2π) factor | from mod-30 beat | — | D |

---

## What v6 Has That Is Not in This Supplement

Everything in Tensor Time v6 remains valid and is not repeated here:

- Full toroid closure table with H_beat verification
- Gluon lifecycle simulation (convergence ratio 0.006637/cycle)
- Hamiltonian path construction on T0–T4
- 10-dimensional parabola geometry and matter/antimatter asymmetry
- Jacobson's missing coefficient η = GEO_B/α_IR = LU
- Black hole signature change at horizon (Lorentzian → Euclidean)
- Tunneling as lane-constrained exit (discrete, not smooth exponential)
- Scattering geometry (mid-loop vs end-of-loop)
- The preface on method and the map/terrain analogy

That material is the technical foundation. This supplement is the new floor
built on top of it.

---

## Open Problems as of v7

| Problem | Status |
|---------|--------|
| Lepton mass hierarchy (μ, τ exact values) | Mechanism identified; calculation pending |
| CKM matrix beyond ρη | ρη derived; full 4-parameter matrix open |
| Graviton as T=c perturbation | Reinterpreted; no distinct GR deviation yet |
| Neutrino masses | Very high n or different Z-sector; not modeled |
| Tau from interference cross-term (numerical) | In progress |
| Continuum limit convergence rate (formal proof) | Physical argument complete; O(a/L) proof pending |

---

## References for New Results

[1] Richardson, J. (2026). TFFT v3.0. This repository.
    [Canonical overview — read first]

[2] Richardson, J. (2026). GBP Framework v8.9.
    Zenodo: 10.5281/zenodo.19798271

[3] Richardson, J. (2026). Maxwell's Equations as the Continuum Limit of
    Mod-30 Winding Geometry. GBP_Maxwell_paper_v3.4.md

[4] Richardson, J. (2026). Yang-Mills Mass Gap from Mod-30 Winding Geometry.
    gbp_yang_mills_v4.md

[5] Richardson, J. (2026). Z₃₀* Winding Geometry as the Analytic Origin of
    Lattice QCD Mode Structure. gbp_lattice_qcd_paper.md

[6] Richardson, J. (2026). Observer-Based Lagrangian. gbp_observer_lagrangian.md

[7] Ilgenfritz et al. (2018). Finite temperature gluon spectral function.
    Eur. Phys. J. C 78, 127. arXiv:1701.08610

[8] Lüscher, M., Weisz, P. (1985). On-shell improved lattice gauge theories.
    Commun. Math. Phys. 97, 59–77.

[9] Deur, A., Brodsky, S.J., de Téramond, G.F. (2024). The QCD Running Coupling.
    Prog. Part. Nucl. Phys. 90, 1–74.

---

*Tensor Time v7 Supplement — May 2026*  
*github.com/historyViper/Best_QCD_Mass_Model*  
*All results offered for critical review. Public domain.*
