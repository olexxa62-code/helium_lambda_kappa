# System A.3: He-II λ-Transition - Provenance Documentation

**System Classification**: A.3 He-II λ-Transition κ Analysis  
**Author**: Oleksii Onasenko  
**Developer**: SubstanceNet  
**Theoretical Framework**: The Emergence Parameter κ ≈ 1: An Empirical Signature of Criticality in Physical and Biological Systems

**License**: Apache 2.0 (see LICENSE file)

---

## System Overview

**Critical Point**: T_λ = 2.1768 K (vapor pressure)  
**Principal Result**: κ ≈ 1.00 throughout superfluid phase

Liquid helium-4 at vapor pressure undergoing λ-transition from normal fluid (He-I, T > T_λ) to superfluid (He-II, T < T_λ). Analysis based on high-precision space-based measurements (Lipa et al., 2003) with nanokelvin temperature resolution.

---

## Parameters at Critical Point

### Complexity
- A/A_c = 1 (thermodynamic limit)
- Space experiment eliminates gravitational finite-size effects
- System measured to within 2 nK of transition

### Topological Order
- τ = ρ_s/ρ (superfluid density fraction, canonical order parameter)
- τ(t) ∝ t^ζ with ζ = 0.6705 ± 0.0006 (experimental)
- τ = 0 for T > T_λ (normal phase)
- τ > 0 for T < T_λ (superfluid phase)

### Correlation
- Λ = ξ (correlation length of thermal fluctuations)
- Λ(t) ∝ t^(-ν) with ν ≈ 2/3
- Λ → ∞ as T → T_λ (critical divergence)
- Λ_c = ξ evaluated at reference point

### Emergence Parameter
- κ = (A/A_c) × τ × (Λ/Λ_c) = τ(t) × Λ(t)/Λ_c
- κ ∝ t^(ζ-ν) = t^0.0035 ≈ constant
- κ = 1.0026 ± 0.0105 throughout superfluid phase

---

## Key Result

**κ ≈ 1 forms a plateau throughout T < T_λ** (0.5 K to 2.17 K), not exclusively a peak at the critical point. This distinguishes superfluidity from other phase transitions.

---

## Mechanism: Perfect Compensation
```
ζ - ν = 0.6705 - 0.667 = 0.0035 ≈ 0
```

As temperature decreases below T_λ:
- Order increases: ρ_s ∝ t^ζ (quantum coherence grows)
- Correlations decrease: ξ ∝ t^(-ν) (fluctuations shrink)
- Perfect compensation: κ ∝ t^(ζ-ν) ≈ const ≈ 1

**Physical interpretation**: The superfluid exhibits equal emergent character at all temperatures below T_λ, representing a stable emergent state rather than a critical phenomenon.

---

## Methodological Features

- Independent measurements from world-class experiments
- Zero-gravity environment (Space Shuttle Columbia, 1992)
- Temperature resolution: 2 nK
- Validated scaling laws: Josephson relation 3ζ + α - 2 = -0.0012 ± 0.0027 ≈ 0

---

## Primary Sources

### Experimental Data

**Lipa, J. A., Nissen, J. A., Stricker, D. A., Swanson, D. R., & Chui, T. C. P.** (2003). Specific heat of liquid helium in zero gravity very near the lambda point. *Physical Review B*, **68**, 174518. arXiv:cond-mat/0310163

- Measured α = -0.0127 ± 0.0003 (Table II, direct measurement)
- Space-based experiment, highest precision to date
- Temperature resolution: 2 nanokelvin
- Table I compiles experimental and theoretical values from literature

### Critical Exponents

**From Lipa et al. (2003), Table I:**

**ζ = 0.6705 ± 0.0006** (experimental, "Observed")
- Source: Goldner, L. S., Mulders, N., & Ahlers, G. (1992), as cited in Lipa Table I, Reference [18]
- Most precise experimental determination of superfluid density exponent
- Original: *Journal of Low Temperature Physics*, **93**, 131-182

**ν ≈ 2/3 (= 0.667)** (theoretical approximation)
- Standard value for 3D XY universality class
- Used by Lipa et al. in text for correlation length: ξ ∝ t^(-2/3)
- Precise theoretical value: ν = 0.67155(27) from Campostrini et al. (2001)

### Theoretical Framework

**Campostrini, M., Hasenbusch, M., Pelissetto, A., Rossi, P., & Vicari, E.** (2001). Critical behavior of the three-dimensional XY universality class. *Physical Review B*, **63**, 214503. arXiv:cond-mat/0010360

- RG calculations for 3D XY model (n=2, D=3)
- Theoretical predictions cited in Lipa Table I, Reference [8]:
  - α (predicted) = -0.0146 ± 0.0008
  - ζ (predicted) = 0.67015 ± 0.00027
- Confirms λ-transition belongs to XY universality class

### Analysis

**Onasenko, O.** (2025). System A.3: He-II λ-Transition - Emergence Parameter Analysis. This work.
- First application of κ framework to λ-transition
- Discovery of κ plateau mechanism

---

## Justification for Parameters

### T_λ = 2.1768 K
Standard value for liquid 4He at vapor pressure (SVP). Measured to 9 significant figures. Used throughout Lipa et al. (2003).

### Critical Point Determination
T_λ is independently known from:
1. Specific heat C_p divergence (λ-shaped peak)
2. Superfluid density onset (ρ_s > 0 for T < T_λ)
3. Thermal conductivity jump
4. Second sound appearance

### ζ = 0.6705 (Experimental)
**Source**: Goldner et al. (1992), as cited in Lipa et al. (2003), Table I, Reference [18]

Measured from second sound velocity v_2^2 ∝ ρ_s. Scaling: ρ_s ∝ |t|^ζ near T_λ. Direct experimental determination with 0.09% precision.

**Note**: Theoretical prediction ζ = 0.67015 ± 0.00027 (Campostrini, 2001) differs slightly from experimental value.

### ν ≈ 2/3 (Theoretical Approximation)
**Source**: Standard approximation used by Lipa et al. in text

Determined from:
1. Correlation length: ξ ∝ |t|^(-ν)
2. Specific heat: C_p ∝ |t|^(-α) with α = 2 - 3ν (for D=3, n=2)
3. RG calculations: ν = 0.67155(27) (Campostrini et al., 2001)

The value ν = 2/3 is particularly robust, used as convenient approximation throughout literature.

---

## System-Specific Notes

### τ Definition: ρ_s/ρ
For superfluids, τ = ρ_s/ρ is the natural choice:
- ρ_s is the order parameter (canonical in Landau theory)
- Directly measurable (second sound, rotating bucket experiments)
- Zero above T_λ, non-zero below (clear phase distinction)
- Grows monotonically as T decreases

### Λ Definition: ξ
We use ξ (correlation length of thermal fluctuations) as it diverges at T_λ and sets the scale for critical phenomena.

### Plateau versus Peak
Both τ and Λ are temperature-dependent with nearly equal exponents (ζ ≈ ν), enabling compensation and yielding κ ∝ t^0 ≈ plateau.

---

## Universality Class

**3D XY Model**: n = 2 (complex order parameter), D = 3 (spatial dimensions)

**Members**:
- 4He λ-transition
- Superconductors (flux line lattice melting)
- Certain magnets (planar spins)
- Atomic BECs with 2-component order parameter

---

## Experimental vs Theoretical Values

### Table: Comparison

| Parameter | Experimental | Source | Theoretical | Source |
|-----------|-------------|--------|-------------|--------|
| α | -0.0127 ± 0.0003 | Lipa (2003) Table II | -0.0146 ± 0.0008 | Campostrini (2001) |
| ζ | 0.6705 ± 0.0006 | Goldner (1992) | 0.67015 ± 0.00027 | Campostrini (2001) |
| ν | - | - | 0.67155(27) ≈ 2/3 | Campostrini (2001) |

**Our Analysis Uses**: Experimental ζ (Goldner), approximation ν = 2/3

---

## Limitations

- Synthetic model uses power laws with measured exponents, not raw C_p(T) data
- Thermodynamic limit assumed (valid for Lipa et al. experiment)
- Asymptotic regime assumed valid over full range
- Corrections to scaling not included (Wegner terms with Δ ≈ 0.5)

---

## Data Availability

All analysis code, synthetic data, and figures available in project repository:
- Analyzer: `src/kappa_analyzer.py`
- Visualizer: `src/visualizer.py`
- Results: `results/kappa_analysis.csv`
- Figures: `figures/fig*.png` (600 DPI)
- Methodology: `docs/METHODOLOGY.md`

**References**: Available in `docs/references/`
- Lipa et al. (2003) - Primary experimental source
- Campostrini et al. (2001) - Theoretical XY model

---

## Reproducibility

Complete analysis reproducible via:
```bash
cd src
python kappa_analyzer.py
python visualizer.py ../results/kappa_analysis.csv
```

Expected results:
- Mean κ = 1.0026 ± 0.0105
- Range: [0.94, 1.02]
- Scaling: κ ∝ t^0.0035

---

## Theoretical Significance

### Understanding of Emergence

Traditional view: Emergence occurs at critical points (κ ≈ 1 at T_c, p_c), marking transitions.

He-II insight: Emergence can be a stable phase property (κ ≈ 1 throughout phase), marking stable states.

### Physical Interpretation

The κ plateau indicates:
1. Superfluidity exhibits equal emergent character at all T < T_λ
2. The entire superfluid phase constitutes a stable emergent state
3. κ ≈ 1 represents a phase property, not exclusively a critical point property

---

**Date**: November 2025  
**Status**: Analysis complete  
**Version**: 2.0
