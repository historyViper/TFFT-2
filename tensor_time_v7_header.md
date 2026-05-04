# Tensor Time v7: A 1D String Theory of Spacetime, Mass, and Entanglement

**Jason Richardson (HistoryViper)**  
*Independent Researcher | github.com/historyViper/Best_QCD_Mass_Model*  
*Zenodo: 10.5281/zenodo.19798271*  
*v6 — April 2026 | v7 supplement — May 2026*  
*AI Collaboration: Claude (Anthropic), ChatGPT/Sage (OpenAI), DeepSeek*

---

## Navigation

**New reader? Start with TFFT v3.0** — it is the canonical overview document,
written after this paper, and covers everything from the single postulate to
the full derivation count in one place. No prerequisites.

This document (Tensor Time v7) is the **technical reference**: full toroid
machinery, Hamiltonian closure table, gluon lifecycle, Jacobson's missing
coefficient, black hole signature change, tunneling geometry, and scattering.
Read it after TFFT v3.0 for the deep mechanics.

The **v7 supplement** (`tensor_time_v7_supplement.md`) documents what is new
since v6: the observer-Noether term, the lattice QCD structural identity, the
beta function sum rule, the mass gap proof, the QCD continuum limit derivation,
and corrections to the lepton mass formula and MOND scale. Append it after this
document.

| Document | Purpose |
|----------|---------|
| TFFT v3.0 | Overview — start here |
| Tensor Time v7 (this) | Technical reference |
| v7 supplement | New results since v6 |
| GBP Maxwell v3.4 | Electromagnetism sector |
| GBP Yang-Mills v4 | Mass gap + confinement |
| GBP W/Z/Higgs v2 | Electroweak sector |
| GBP Lattice QCD | Lattice connection + testable prediction |

---

*v7 changes from v6: navigation header added; TFFT v3.0 named as canonical entry
point; v7 supplement file added for new results. All technical content from v6
is unchanged — the physics, numbers, and derivations stand as written.*

*v6 changes: T3 geometry clarified (spacetime vs Hamiltonian layers); charm
Möbius alignment corrected; dark matter section removed pending further
development; QFT-complementary framing added throughout; geometric coupling
scale and filtering mechanism made explicit; κ₀ primary expression updated to
α_IR×Λ_QCD³ with E=mc² secondary; φ³ hadronic-to-electroweak bridge conjecture
added; Higgs mechanism framing updated — mechanism preserved, fundamental scalar
field replaced by geometric threshold.*

---

## Preface: On Method

**This work is speculative and has not undergone peer review. It is offered
for scrutiny and attempted falsification.**

The Standard Model of particle physics is one of the most precisely verified
scientific frameworks ever constructed. QED is accurate to twelve decimal places.
QCD reproduces the hadron spectrum at sub-percent precision. The physicists who
built these frameworks deserve full credit for that achievement, and nothing in
this paper disputes their results.

The goal here is narrower and more modest: to ask whether the mathematical
structure of QFT — which is extraordinarily well-confirmed — might have a
geometric origin that explains *why* the math takes the form it does. QFT
operates from measured constants and fitted symmetry groups. This framework
proposes that those constants and symmetries are derivable from geometry — which
would mean fewer external inputs and a reason for the structure rather than just
a description of it.

The test is strict: any geometric derivation presented here that conflicts with
QFT predictions or experimental data falsifies the framework on those grounds.
There is no freedom to adjust — derived quantities either match observations or
the theory fails. We state this explicitly because it is the only claim worth
making.

The relationship between this framework and standard QFT is the same as the
relationship between a map and the terrain it describes. QFT is an accurate
map. The terrain is what was always there. Finding the terrain does not
invalidate the map — it explains why the map works as well as it does.

Concretely: the Dirac spinor, Yang-Mills gauge fields, torsion B-field, and
path integral are all present in this framework, unchanged. The single
modification is that the path integral sums over Z₃₀* = {1,7,11,13,17,19,23,29}
winding numbers only. That restriction — which falls out of the geometry —
is what gives the mass spectrum, the coupling constants, and the mass gap.
