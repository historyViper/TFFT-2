#!/usr/bin/env python3
"""
GBP v7 Mass Ladder - Finding the Optimal Residue Pattern
======================================================
The key question: Is there a pattern to which residue (r ∈ {1,7,11,13,17,19,23,29})
each particle gets assigned?

Let's optimize to find the best mapping.
"""

import math
from typing import Dict, List, Tuple
from collections import defaultdict
import itertools

# ============================================================================
# CONSTANTS
# ============================================================================

GAMMA_1 = 14.1347251420745
PHI = (1 + math.sqrt(5)) / 2
GEO_B = math.sin(math.pi / 15) ** 2
ALPHA_IR = 0.848809
LU = GEO_B / ALPHA_IR

GEN_N = {'gen1': 4, 'gen2': 7, 'gen3': 2}
ALLOWED_RESIDUES = [1, 7, 11, 13, 17, 19, 23, 29]

# ============================================================================
# PARTICLE DATABASE
# ============================================================================

PARTICLE_MASSES = {
    'Xi_cc++': 3621.4, 'Xi_cc+': 3518.94, 'Omega_cc+': 2695.2,
    'Lambda_c+': 2286.46, 'Xi_c+': 2467.71, 'Xi_c0': 2470.44,
    'Sigma_c++': 2453.97, 'Sigma_c+': 2452.65, 'Sigma_c0': 2453.75,
    'Omega_c0': 2674.4, 'Xi_c*+': 2645.53, 'Xi_c*0': 2646.33,
    'Sigma_c*++': 2520.2, 'Sigma_c*+': 2518.8, 'Sigma_c*0': 2517.5, 'Omega_c*0': 2765.9,
    'Lambda': 1115.683, 'Sigma+': 1189.37, 'Sigma0': 1192.642, 'Sigma-': 1197.449,
    'Xi0': 1314.86, 'Xi-': 1321.71, 'Omega-': 1672.45,
    'Lambda_b0': 5620.6, 'Xi_b-': 5797.0, 'Xi_b0': 5768.4,
    'Sigma_b+': 5811.0, 'Sigma_b0': 5813.4, 'Omega_b-': 6046.0,
}

PARTICLE_FAMILIES = {
    'Lambda_c+': 'gen1', 'Sigma_c++': 'gen1', 'Sigma_c+': 'gen1', 'Sigma_c0': 'gen1',
    'Sigma_c*++': 'gen1', 'Sigma_c*+': 'gen1', 'Sigma_c*0': 'gen1',
    'Xi_c+': 'gen2', 'Xi_c0': 'gen2', 'Xi_c*+': 'gen2', 'Xi_c*0': 'gen2',
    'Omega_c0': 'gen2', 'Omega_c*0': 'gen2',
    'Xi_cc++': 'gen3', 'Xi_cc+': 'gen3', 'Omega_cc+': 'gen3',
    'Lambda': 'gen1', 'Sigma+': 'gen1', 'Sigma0': 'gen1', 'Sigma-': 'gen1',
    'Xi0': 'gen2', 'Xi-': 'gen2', 'Omega-': 'gen2',
    'Lambda_b0': 'gen1', 'Sigma_b+': 'gen1', 'Sigma_b0': 'gen1',
    'Xi_b-': 'gen2', 'Xi_b0': 'gen2', 'Omega_b-': 'gen2',
}

PARTICLE_TOPOLOGY = {
    'Lambda_c+': 1, 'Sigma_c++': 1, 'Sigma_c+': 1, 'Sigma_c0': 1,
    'Xi_c+': 2, 'Xi_c0': 2, 'Omega_c0': 3,
    'Xi_c*+': 2, 'Xi_c*0': 2, 'Omega_c*0': 3,
    'Sigma_c*++': 1, 'Sigma_c*+': 1, 'Sigma_c*0': 1,
    'Xi_cc++': 2, 'Xi_cc+': 2, 'Omega_cc+': 3,
    'Lambda': 1, 'Sigma+': 1, 'Sigma0': 1, 'Sigma-': 1,
    'Xi0': 2, 'Xi-': 2, 'Omega-': 3,
    'Lambda_b0': 1, 'Sigma_b+': 1, 'Sigma_b0': 1,
    'Xi_b-': 2, 'Xi_b0': 2, 'Omega_b-': 3,
}

# ============================================================================
# MODEL FUNCTIONS
# ============================================================================

def S2(gen: str) -> float:
    return math.sin(GEN_N[gen] * math.pi / 15) ** 2

def boundary_scale(k: int) -> float:
    return LU * (PHI ** k)

def compute_mass(residue: int, gen: str, k: int, E_ref: float) -> float:
    n = residue / 30.0 * math.pi
    exp_factor = math.exp(-n / math.pi)
    return E_ref * exp_factor * S2(gen) * (1 + boundary_scale(k))


def optimize_residue_assignments():
    """Find the best residue for each unique (family, topology) group."""
    print("=" * 70)
    print("OPTIMIZING RESIDUE ASSIGNMENTS")
    print("=" * 70)
    
    # Group particles by (family, topology)
    groups = defaultdict(list)
    for name in PARTICLE_MASSES:
        if name in PARTICLE_FAMILIES and name in PARTICLE_TOPOLOGY:
            key = (PARTICLE_FAMILIES[name], PARTICLE_TOPOLOGY[name])
            groups[key].append((name, PARTICLE_MASSES[name]))
    
    print(f"\nFound {len(groups)} unique (family, topology) groups:")
    for key, particles in sorted(groups.items()):
        masses = [p[1] for p in particles]
        print(f"  {key}: {len(particles)} particles, mass range {min(masses):.0f}-{max(masses):.0f}")
    
    # For each group, find the best residue assignment
    # We do a grid search over (E_ref, residue) for each group
    
    particle_names = list(PARTICLE_MASSES.keys())
    valid_particles = [p for p in particle_names if p in PARTICLE_FAMILIES and p in PARTICLE_TOPOLOGY]
    
    # Grid search overall E_ref and residue
    best_mape = 100.0
    best_assignments = {}
    
    print("\n[Grid searching E_ref and residue assignments...]")
    
    for E_ref in range(1000, 8000, 100):
        # For each particle, try each allowed residue
        assignments = {}
        
        for name in valid_particles:
            gen = PARTICLE_FAMILIES[name]
            k = PARTICLE_TOPOLOGY[name]
            exp_mass = PARTICLE_MASSES[name]
            
            # Find best residue for this particle
            best_residue_for_particle = 29  # default
            best_error_for_particle = float('inf')
            
            for residue in ALLOWED_RESIDUES:
                pred = compute_mass(residue, gen, k, E_ref)
                if pred > 0:
                    err = abs(pred - exp_mass) / exp_mass
                    if err < best_error_for_particle:
                        best_error_for_particle = err
                        best_residue_for_particle = residue
            
            assignments[name] = best_residue_for_particle
        
        # Compute overall MAPE
        total_err = 0.0
        for name in valid_particles:
            residue = assignments[name]
            gen = PARTICLE_FAMILIES[name]
            k = PARTICLE_TOPOLOGY[name]
            exp_mass = PARTICLE_MASSES[name]
            pred = compute_mass(residue, gen, k, E_ref)
            if pred > 0:
                total_err += abs(pred - exp_mass) / exp_mass * 100
        
        mape = total_err / len(valid_particles)
        if mape < best_mape:
            best_mape = mape
            best_assignments = assignments.copy()
            best_E_ref = E_ref
    
    print(f"\nBest E_ref = {best_E_ref}")
    print(f"Best MAPE = {best_mape:.4f}%")
    
    # Show assignments
    print("\n[Optimal Residue Assignments]")
    print("-" * 70)
    print(f"{'Particle':<12} {'Family':<8} {'k':<3} {'Residue':<8} {'Exp':<12} {'Pred':<12} {'Err%'}")
    print("-" * 70)
    
    # Group by residue
    residue_groups = defaultdict(list)
    for name in valid_particles:
        residue = best_assignments[name]
        gen = PARTICLE_FAMILIES[name]
        k = PARTICLE_TOPOLOGY[name]
        exp_mass = PARTICLE_MASSES[name]
        pred = compute_mass(residue, gen, k, best_E_ref)
        err = abs(pred - exp_mass) / exp_mass * 100
        residue_groups[residue].append((name, gen, k, exp_mass, pred, err))
    
    for residue in sorted(residue_groups.keys()):
        print(f"\n  Residue {residue}:")
        for name, gen, k, exp, pred, err in residue_groups[residue]:
            print(f"    {name:<12} {gen:<8} {k:<3} {residue:<8} {exp:<12.2f} {pred:<12.2f} {err:.2f}%")
    
    # Run ablation with optimized assignments
    print("\n" + "=" * 70)
    print("ABLATION WITH OPTIMIZED ASSIGNMENTS")
    print("=" * 70)
    
    def compute_mape_ablated(use_boundary: bool, use_S2: bool) -> float:
        total_err = 0.0
        for name in valid_particles:
            residue = best_assignments[name]
            gen = PARTICLE_FAMILIES[name]
            k = PARTICLE_TOPOLOGY[name]
            exp_mass = PARTICLE_MASSES[name]
            
            # Compute with ablation
            n = residue / 30.0 * math.pi
            exp_factor = math.exp(-n / math.pi)
            mass = best_E_ref * exp_factor
            
            if use_S2:
                mass *= S2(gen)
            
            if use_boundary:
                mass *= (1 + boundary_scale(k))
            
            if mass > 0:
                total_err += abs(mass - exp_mass) / exp_mass * 100
        
        return total_err / len(valid_particles)
    
    baseline = compute_mape_ablated(True, True)
    print(f"\nBaseline (full model): {baseline:.4f}%")
    
    no_boundary = compute_mape_ablated(False, True)
    print(f"Remove lam (boundary): {no_boundary:.4f}% (+{no_boundary - baseline:.4f}%)")
    
    no_S2 = compute_mape_ablated(True, False)
    print(f"Remove S2 (geo): {no_S2:.4f}% (+{no_S2 - baseline:.4f}%)")
    
    both = compute_mape_ablated(False, False)
    print(f"Remove both: {both:.4f}% (+{both - baseline:.4f}%)")
    
    # Test pattern: do residues follow topology?
    print("\n" + "=" * 70)
    print("PATTERN ANALYSIS")
    print("=" * 70)
    
    # See if residue correlates with topology k
    k_groups = defaultdict(list)
    for name in valid_particles:
        k = PARTICLE_TOPOLOGY[name]
        r = best_assignments[name]
        k_groups[k].append(r)
    
    print("\nResidue by topology k:")
    for k in sorted(k_groups.keys()):
        residues = k_groups[k]
        avg = sum(residues) / len(residues)
        print(f"  k={k}: residues = {residues}, avg = {avg:.1f}")


if __name__ == '__main__':
    optimize_residue_assignments()
    print("\n" + "=" * 70)