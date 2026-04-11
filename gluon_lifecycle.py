#!/usr/bin/env python3
"""
gluon_lifecycle.py — GBP Gluon Lifecycle Model
================================================
Models the gluon as a figure-8 (T4) wave that travels through
quark lane pairs, losing energy via pure geometric projection
at each toroid boundary, depositing inertial mass, then dying
at the colorless {1,29} lanes and recycling.

PHYSICS:
  - Gluon wave = T4 figure-8 topology (dual color-anticolor)
  - Energy loss = Hilbert→state space projection at each toroid boundary
  - projection = sin²(lane) × phi_k(toroid_type)   [pure geometry]
  - Colorless {1,29} lanes = vacuum, gluon graveyard
  - Deposited energy → constituent quark inertial mass
  - Noether: energy loss per step is the symmetry cost of each toroid

GLUON LIFECYCLE:
  Born at Toroid A → traverses B → C → dies at colorless →
  deposits inertial mass → feedback seeds next gluon

FIGURE-8 PAIRS (two lanes per toroid visit):
  Toroid A {7,  11}  T1 plain torus     — born here
  Toroid B {13, 17}  T2 Mobius twist    — maximum energy loss
  Toroid C {19, 23}  T3 Y-junction      — nearly transparent
  Colorless{1,  29}  T1 plain torus     — dies, deposits remainder

PROJECTION FORMULA (pure geometry, no quark flavor factors):
  proj(lane, toroid) = min(1, sin²(lane × π/15) × φ^k(toroid))
  deposited = E_in × (1 - avg_proj)
  E_out     = E_in × avg_proj

AUTHORS: HistoryViper (Jason Richardson) — Independent Researcher
         AI collaboration: Claude (Anthropic)
CODE:    github.com/historyViper/mod30-spinor
RELATED: gbp_complete_v7_5.py, mass_ladder_v2_gravity.py
"""

import math

# ── Constants ──────────────────────────────────────────────────────────────
PI       = math.pi
PHI      = (1 + math.sqrt(5)) / 2
GEO_B    = math.sin(PI/15)**2
ALPHA_IR = 0.848809
LU       = GEO_B / ALPHA_IR
PI15     = PI / 15

# Toroid phi scaling — pure geometry
# Each additional Mobius twist multiplies boundary scale by sqrt(phi)
TOPO_PHI = {
    'T1': PHI**0.0,   # plain torus       — no twist      φ^0 = 1.000
    'T2': PHI**0.5,   # Mobius twist      — 1 twist       φ^0.5 = 1.272
    'T3': PHI**1.0,   # Y-junction        — 2 twists      φ^1.0 = 1.618
    'T4': PHI**1.5,   # figure-8 (photon) — 3 twists      φ^1.5 = 2.058
}

# Lane assignments (from mod-30 spinor geometry)
LANE_QUARKS = {
    7:  'strange',
    11: 'down',
    13: 'bottom',
    17: 'top',
    19: 'up',
    23: 'charm',
    1:  'colorless',
    29: 'colorless',
}

# Current quark masses (PDG MS-bar, MeV)
CURRENT_MASS = {
    'up':      2.16,
    'down':    4.67,
    'strange': 93.4,
    'charm':   1270.0,
    'bottom':  4180.0,
    'top':     173400.0,
}

# Constituent masses (GBP v7.5, MeV)
CONSTITUENT = {
    'up':     336.0,
    'down':   340.0,
    'strange': 486.0,
    'charm':   1550.0,
    'bottom':  4730.0,
    'top':     173400.0,
}

# ── Gluon figure-8 step sequence ───────────────────────────────────────────
# (lane_a, lane_b, toroid_type, label)
GLUON_STEPS = [
    (7,  11, 'T1', 'Toroid A — born    (strange/down,  T1 plain)'),
    (13, 17, 'T2', 'Toroid B           (bottom/top,    T2 Mobius)'),
    (19, 23, 'T3', 'Toroid C           (up/charm,      T3 Y-junction)'),
    (1,  29, 'T1', 'Colorless — dies   ({1,29},        T1 plain)'),
]

# ── Core geometry ──────────────────────────────────────────────────────────
def sin2_lane(r):
    """Boundary projection sin²(r·π/15) for lane r."""
    return math.sin(r * PI15)**2

def lane_projection(lane, toroid):
    """
    Pure geometric projection at a lane/toroid crossing.
    projection = sin²(lane·π/15) × φ^k(toroid)
    Capped at 1.0 — projection is a probability.
    """
    return min(1.0, sin2_lane(lane) * TOPO_PHI[toroid])

def step_projection(la, lb, toroid):
    """Average projection across figure-8 pair."""
    return (lane_projection(la, toroid) + lane_projection(lb, toroid)) / 2.0

# ── Lifecycle simulation ───────────────────────────────────────────────────
def run_lifecycle(E_born=1.0, n_cycles=5, verbose=True):
    """
    Simulate gluon lifecycle for n_cycles.
    Returns (all_cycles_data, cumulative_deposit_per_step, E_final)
    """
    if verbose:
        _section("GBP GLUON LIFECYCLE — figure-8 toroid traversal")
        print(f"  Born energy : {E_born:.6f} (normalized)")
        print(f"  Cycles      : {n_cycles}")
        print(f"  Projection  : sin²(lane·π/15) × φ^k(toroid)  [pure geometry]")
        print()

    all_cycles    = []
    step_deposits = [0.0] * len(GLUON_STEPS)
    E = E_born

    for cycle in range(1, n_cycles + 1):
        cycle_data  = []
        E_cycle_in  = E

        if verbose:
            print(f"  CYCLE {cycle}  (E = {E:.10f})")
            print(f"  {'#':<3} {'Lanes':<10} {'T':>3} {'φ^k':>7} "
                  f"{'sin²a':>8} {'sin²b':>8} {'pa':>8} {'pb':>8} "
                  f"{'avg_p':>8} {'E_in':>12} {'deposit':>12} {'E_out':>12}")
            print(f"  {'-'*105}")

        for i, (la, lb, T, label) in enumerate(GLUON_STEPS):
            pk      = TOPO_PHI[T]
            s2a     = sin2_lane(la)
            s2b     = sin2_lane(lb)
            pa      = lane_projection(la, T)
            pb      = lane_projection(lb, T)
            avg_p   = (pa + pb) / 2.0
            dep     = E * (1.0 - avg_p)
            E_out   = E * avg_p

            step_deposits[i] += dep

            row = dict(cycle=cycle, step=i+1, lanes=(la,lb), toroid=T,
                       phi_k=pk, s2a=s2a, s2b=s2b, pa=pa, pb=pb,
                       avg_proj=avg_p, E_in=E, deposited=dep, E_out=E_out,
                       label=label)
            cycle_data.append(row)

            if verbose:
                print(f"  {i+1:<3} {str((la,lb)):<10} {T:>3} {pk:>7.4f} "
                      f"{s2a:>8.5f} {s2b:>8.5f} {pa:>8.5f} {pb:>8.5f} "
                      f"{avg_p:>8.5f} {E:>12.8f} {dep:>12.8f} {E_out:>12.8f}"
                      f"  ← {label}")
            E = E_out

        all_cycles.append(cycle_data)

        if verbose:
            dep_cycle = E_cycle_in - E
            print(f"\n  Cycle {cycle}: deposited={dep_cycle:.10f}  "
                  f"feedback={E:.10f}\n")

        if E < 1e-15:
            if verbose:
                print(f"  → Energy exhausted after {cycle} cycles.\n")
            break

    return all_cycles, step_deposits, E

# ── Analysis ───────────────────────────────────────────────────────────────
def energy_analysis(step_deposits, E_final):
    _section("ENERGY DEPOSITION BY TOROID STEP")

    total = sum(step_deposits) + E_final
    print(f"  {'Step':<4} {'Lanes':<10} {'Toroid':>7} {'deposited':>14} "
          f"{'fraction%':>10}  label")
    print(f"  {'-'*75}")

    for i, (la, lb, T, label) in enumerate(GLUON_STEPS):
        dep  = step_deposits[i]
        frac = dep / total * 100
        print(f"  {i+1:<4} {str((la,lb)):<10} {T:>7} {dep:>14.8f} "
              f"{frac:>10.4f}%  {label}")

    print(f"\n  {'feedback seed':<26} {E_final:>14.8f} "
          f"{E_final/total*100:>10.4f}%")
    print(f"  {'TOTAL':<26} {total:>14.8f} {'100.0000%':>10}")

def projection_table():
    _section("GEOMETRIC PROJECTION TABLE — sin²(lane) × φ^k per step")

    print(f"  {'Step':<4} {'Lanes':<10} {'Toroid':>6} {'φ^k':>7} "
          f"{'sin²(a)':>9} {'sin²(b)':>9} {'proj_a':>9} {'proj_b':>9} "
          f"{'avg_proj':>10}")
    print(f"  {'-'*80}")

    for i, (la, lb, T, label) in enumerate(GLUON_STEPS):
        pk  = TOPO_PHI[T]
        s2a = sin2_lane(la)
        s2b = sin2_lane(lb)
        pa  = lane_projection(la, T)
        pb  = lane_projection(lb, T)
        avg = (pa + pb) / 2.0
        print(f"  {i+1:<4} {str((la,lb)):<10} {T:>6} {pk:>7.4f} "
              f"{s2a:>9.5f} {s2b:>9.5f} {pa:>9.5f} {pb:>9.5f} {avg:>10.5f}"
              f"  ← {label}")

    print()
    print("  Interpretation:")
    print("  T1 plain  (φ^0=1.000): no twist — projection = raw sin²")
    print("  T2 Mobius (φ^0.5=1.272): 1 twist — projection amplified")
    print("  T3 Y-junc (φ^1.0=1.618): 2 twists — near-transparent for high sin²")
    print("  T1 color. (φ^0=1.000): colorless floor — minimum projection")

def convergence_analysis(n_cycles=20):
    _section("CONVERGENCE — energy per cycle")

    E = 1.0
    print(f"  {'Cycle':>6} {'E_start':>14} {'deposited':>14} "
          f"{'E_end':>14} {'dep_ratio':>10}")
    print(f"  {'-'*60}")

    prev_dep = None
    for cycle in range(1, n_cycles + 1):
        E_start = E
        for la, lb, T, _ in GLUON_STEPS:
            avg_p = step_projection(la, lb, T)
            E    *= avg_p
        dep   = E_start - E
        ratio = dep / prev_dep if prev_dep else 1.0
        prev_dep = dep
        print(f"  {cycle:>6} {E_start:>14.10f} {dep:>14.10f} "
              f"{E:>14.10f} {ratio:>10.6f}")
        if E < 1e-12:
            print(f"  → Effectively zero after {cycle} cycles.")
            break

def inertial_mass_note():
    _section("INERTIAL MASS CONNECTION")

    print("  Constituent quark mass = Yukawa (Higgs) mass + gluon inertia")
    print("  Gluon inertia = accumulated T1 colorless deposits per quark lane")
    print()
    print(f"  {'Quark':<10} {'Lane':>6} {'m_current':>10} {'m_constituent':>14} "
          f"{'inertial gap':>13}")
    print(f"  {'-'*57}")

    for q, lane in [('strange',7),('down',11),('bottom',13),
                    ('top',17),('up',19),('charm',23)]:
        mc  = CURRENT_MASS[q]
        con = CONSTITUENT.get(q, 0)
        gap = con - mc if con else 0
        print(f"  {q:<10} {lane:>6} {mc:>10.2f} {con:>14.1f} {gap:>13.2f}")

    print()
    print("  Strange inertial gap / Λ_QCD ≈ φ³ = 4.236")
    print("  → Strange quark sits at Toroid A birth point,")
    print("    receives ~23% of each gluon cycle energy deposit.")
    print()
    print("  Toroid B (T2 Möbius) is the primary energy sink at ~61%.")
    print("  Bottom/top lanes 13/17 have low sin² (0.165) but T2 amplification")
    print("  creates maximum energy loss — these become the inertial mass floor.")

def summary():
    _section("SUMMARY")

    # Compute single-cycle projections for display
    steps_proj = []
    E = 1.0
    for la, lb, T, label in GLUON_STEPS:
        avg_p = step_projection(la, lb, T)
        dep   = E * (1.0 - avg_p)
        steps_proj.append((dep/1.0*100, label))
        E    *= avg_p

    print(f"""
  GLUON WAVE TOPOLOGY:
    Born   : T4 figure-8 (dual color-anticolor)
    Travels: through toroid pairs losing energy at each boundary
    Dies   : at colorless {{1,29}} T1 plain torus
    Recycles: feedback seed → new gluon born at Toroid A

  ENERGY DEPOSITION PER CYCLE (single cycle):
    Toroid A {'{7,11}'}  T1: {steps_proj[0][0]:>6.2f}%  ← born, strange/down
    Toroid B {'{13,17}'} T2: {steps_proj[1][0]:>6.2f}%  ← PRIMARY SINK (Möbius)
    Toroid C {'{19,23}'} T3: {steps_proj[2][0]:>6.2f}%  ← near-transparent
    Colorless{'{1,29}'}  T1: {steps_proj[3][0]:>6.2f}%  ← final deposit

  PROJECTION FORMULA (pure geometry):
    proj = sin²(lane·π/15) × φ^k(toroid)
    No quark flavor factors — gluon sees geometry only

  CONSTANTS:
    GEO_B    = sin²(π/15)  = {GEO_B:.8f}
    LU       = GEO_B/α_IR  = {LU:.8f}
    PHI      = golden ratio = {PHI:.8f}
    φ^0 (T1) = {TOPO_PHI['T1']:.6f}
    φ^0.5(T2)= {TOPO_PHI['T2']:.6f}
    φ^1 (T3) = {TOPO_PHI['T3']:.6f}
    φ^1.5(T4)= {TOPO_PHI['T4']:.6f}

  github.com/historyViper/mod30-spinor
""")
    _divider()

# ── Helpers ────────────────────────────────────────────────────────────────
def _divider(c='=', w=72): print(c*w)
def _section(t): print(); _divider(); print(t); _divider(); print()

# ── Main ───────────────────────────────────────────────────────────────────
def main():
    print()
    _divider('═')
    print("  GBP GLUON LIFECYCLE — gluon_lifecycle.py")
    print("  Figure-8 toroid traversal | Pure geometry projection")
    print("  sin²(lane·π/15) × φ^k(toroid)")
    _divider('═')
    print(f"  LU={LU:.6f}  PHI={PHI:.6f}  GEO_B={GEO_B:.6f}")

    projection_table()

    cycles, step_deposits, E_final = run_lifecycle(
        E_born=1.0, n_cycles=5, verbose=True
    )

    energy_analysis(step_deposits, E_final)
    convergence_analysis(n_cycles=15)
    inertial_mass_note()
    summary()

if __name__ == "__main__":
    main()
