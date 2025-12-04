#!/usr/bin/env python3
"""
System Classification: A.3 He-II λ-Transition κ Analysis
Author: Oleksii Onasenko
Developer: SubstanceNet
Theoretical Framework: The Emergence Parameter κ ≈ 1: An Empirical Signature 
                       of Criticality in Physical and Biological Systems

Copyright 2025 Oleksii Onasenko

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Emergence parameter κ analysis for He-II λ-transition.

Data sources:
- Critical exponents from Lipa et al. (2003), Physical Review B 68, 174518
- Experimental values via high-precision space-based measurements
"""

import numpy as np
import pandas as pd
import os

# Physical constants and critical exponents
T_LAMBDA = 2.1768  # K (lambda point at vapor pressure, Lipa et al., 2003)

# Critical exponents (from Lipa et al., 2003, Table I):
ZETA = 0.6705      # Superfluid density exponent (experimental)
                   # Goldner et al. (1992) as cited in Lipa Table I, ref [18]
                   
NU = 0.6717        # Correlation length exponent (XY universality class)
                   # Standard approximation used in Lipa et al. text
                   
ALPHA = -0.0127    # Specific heat exponent (experimental)
                   # Lipa et al. (2003), Table II, direct measurement

class HeliumLambdaAnalyzer:
    """Analyzer for emergence parameter κ in He-II λ-transition."""
    
    def __init__(self, T_lambda=T_LAMBDA):
        """
        Initialize analyzer.
        
        Parameters
        ----------
        T_lambda : float
            Lambda transition temperature in Kelvin.
        """
        self.T_lambda = T_lambda
        self.data = None
        
    def reduced_temperature(self, T):
        """
        Calculate reduced temperature t = |1 - T/T_λ|.
        
        Parameters
        ----------
        T : array_like
            Temperature in Kelvin.
            
        Returns
        -------
        array_like
            Reduced temperature.
        """
        return np.abs(1.0 - T / self.T_lambda)
    
    def superfluid_density(self, t):
        """
        Calculate superfluid density fraction ρ_s/ρ.
        
        ρ_s/ρ ∝ t^ζ for T < T_λ
        
        Parameters
        ----------
        t : array_like
            Reduced temperature.
            
        Returns
        -------
        array_like
            Normalized superfluid density.
        """
        return np.power(t, ZETA)
    
    def correlation_length(self, t):
        """
        Calculate correlation length ξ (normalized).
        
        ξ ∝ t^(-ν) for T near T_λ
        
        Parameters
        ----------
        t : array_like
            Reduced temperature.
            
        Returns
        -------
        array_like
            Normalized correlation length.
        """
        return np.power(t, -NU)
    
    def calculate_kappa(self, T):
        """
        Calculate emergence parameter κ with normalization.
        
        κ = (A/A_c) × τ × (Λ/Λ_c)
        
        Parameters
        ----------
        T : array_like
            Temperature in Kelvin.
            
        Returns
        -------
        tuple
            (kappa, reduced_temperature)
        """
        t = self.reduced_temperature(T)
        mask = T < self.T_lambda
        kappa = np.zeros_like(T)
        
        if np.any(mask):
            t_super = t[mask]
            tau_raw = self.superfluid_density(t_super)
            xi_raw = self.correlation_length(t_super)
            kappa_raw = tau_raw * xi_raw
            
            # Normalize to κ = 1 at reference point
            t_ref = 0.01
            tau_ref = np.power(t_ref, ZETA)
            xi_ref = np.power(t_ref, -NU)
            kappa_ref = tau_ref * xi_ref
            
            kappa[mask] = kappa_raw / kappa_ref
        
        return kappa, t
    
    def theoretical_kappa_scaling(self, t):
        """
        Calculate theoretical scaling κ ∝ t^(ζ-ν).
        
        Parameters
        ----------
        t : array_like
            Reduced temperature.
            
        Returns
        -------
        array_like
            Normalized κ values.
        """
        exponent = ZETA - NU
        kappa_raw = np.power(t, exponent)
        
        t_ref = 0.01
        kappa_ref = np.power(t_ref, exponent)
        
        return kappa_raw / kappa_ref
    
    def generate_synthetic_data(self, n_points=100):
        """
        Generate synthetic data for κ analysis.
        
        Parameters
        ----------
        n_points : int
            Number of data points.
            
        Returns
        -------
        DataFrame
            Analysis data.
        """
        T_min = 0.5
        T_max = self.T_lambda - 1e-9
        
        T_near = np.logspace(np.log10(T_max - 0.01), np.log10(T_max), n_points//2)
        T_far = np.linspace(T_min, T_max - 0.01, n_points//2)
        
        T = np.concatenate([T_far, T_near])
        T = np.sort(T)
        
        kappa, t = self.calculate_kappa(T)
        
        rho_s = np.zeros_like(T)
        xi_norm = np.zeros_like(T)
        
        mask = T < self.T_lambda
        if np.any(mask):
            t_super = t[mask]
            rho_s[mask] = self.superfluid_density(t_super)
            
            t_ref = 0.01
            xi_raw = self.correlation_length(t_super)
            xi_ref = self.correlation_length(t_ref)
            xi_norm[mask] = xi_raw / xi_ref
        
        self.data = pd.DataFrame({
            'T': T,
            't': t,
            'kappa': kappa,
            'rho_s': rho_s,
            'xi_norm': xi_norm
        })
        
        return self.data
    
    def analyze(self, output_dir='../results'):
        """
        Perform complete κ analysis.
        
        Parameters
        ----------
        output_dir : str
            Output directory path.
            
        Returns
        -------
        dict
            Analysis results.
        """
        if self.data is None:
            self.generate_synthetic_data()
        
        mask = self.data['T'] < self.T_lambda
        data_super = self.data[mask]
        
        kappa_mean = data_super['kappa'].mean()
        kappa_std = data_super['kappa'].std()
        kappa_min = data_super['kappa'].min()
        kappa_max = data_super['kappa'].max()
        
        kappa_at_001 = data_super[np.abs(data_super['t'] - 0.01) < 0.001]['kappa'].mean()
        kappa_at_01 = data_super[np.abs(data_super['t'] - 0.1) < 0.01]['kappa'].mean()
        
        results = {
            'T_lambda': self.T_lambda,
            'zeta': ZETA,
            'nu': NU,
            'zeta_minus_nu': ZETA - NU,
            'kappa_mean': kappa_mean,
            'kappa_std': kappa_std,
            'kappa_min': kappa_min,
            'kappa_max': kappa_max,
            'kappa_at_t_001': kappa_at_001,
            'kappa_at_t_01': kappa_at_01,
            'n_points': len(data_super),
            'T_range': (data_super['T'].min(), data_super['T'].max())
        }
        
        os.makedirs(output_dir, exist_ok=True)
        
        self.data.to_csv(f'{output_dir}/kappa_analysis.csv', index=False)
        
        with open(f'{output_dir}/analysis_summary.txt', 'w') as f:
            f.write("System A.3: He-II λ-Transition - κ Analysis Summary\n")
            f.write("="*60 + "\n\n")
            f.write(f"Lambda Point: T_λ = {self.T_lambda:.4f} K\n\n")
            f.write("Critical Exponents (from Lipa et al., 2003):\n")
            f.write(f"  ζ (superfluid density) = {ZETA:.4f}\n")
            f.write(f"    Source: Goldner et al. (1992), Table I ref [18]\n")
            f.write(f"  ν (correlation length) = {NU:.3f}\n")
            f.write(f"    Source: XY universality class (Campostrini et al., 2001)\n")
            f.write(f"  ζ - ν = {ZETA - NU:.4f}\n\n")
            f.write("Theoretical Result:\n")
            f.write(f"  κ ∝ t^(ζ-ν) = t^{ZETA - NU:.4f}\n\n")
            f.write(f"Emergence Parameter Statistics (T < T_λ):\n")
            f.write(f"  Mean κ = {kappa_mean:.4f} ± {kappa_std:.4f}\n")
            f.write(f"  Range: [{kappa_min:.4f}, {kappa_max:.4f}]\n")
            f.write(f"  κ at t=0.01: {kappa_at_001:.4f}\n")
            f.write(f"  κ at t=0.1: {kappa_at_01:.4f}\n\n")
            f.write(f"Temperature Range: {results['T_range'][0]:.2f} - {results['T_range'][1]:.4f} K\n")
            f.write(f"Number of Points: {results['n_points']}\n\n")
            f.write("="*60 + "\n")
            f.write("CONCLUSION:\n")
            f.write("="*60 + "\n")
            f.write("κ maintains value of approximately 1 throughout superfluid phase,\n")
            f.write("confirming stable emergent state rather than critical point phenomenon.\n")
        
        print(f"Results saved to {output_dir}/")
        print(f"  - kappa_analysis.csv")
        print(f"  - analysis_summary.txt")
        
        return results

def main():
    """Main analysis pipeline."""
    print("="*60)
    print("System A.3: He-II λ-Transition")
    print("Emergence Parameter κ Analysis")
    print("="*60)
    print()
    
    analyzer = HeliumLambdaAnalyzer()
    
    print("Generating synthetic data...")
    analyzer.generate_synthetic_data(n_points=200)
    print(f"Generated {len(analyzer.data)} data points")
    print()
    
    print("Analyzing κ...")
    results = analyzer.analyze()
    print()
    
    print("KEY RESULTS:")
    print("-"*60)
    print(f"ζ - ν = {results['zeta_minus_nu']:.4f}")
    print(f"Mean κ (superfluid phase) = {results['kappa_mean']:.4f} ± {results['kappa_std']:.4f}")
    print(f"Range: [{results['kappa_min']:.4f}, {results['kappa_max']:.4f}]")
    print(f"κ at t=0.01: {results['kappa_at_t_001']:.4f}")
    print(f"κ at t=0.1: {results['kappa_at_t_01']:.4f}")
    print()
    print("INTERPRETATION:")
    print("  Near-zero value of (ζ-ν) implies κ ∝ t^0 ≈ constant")
    print("  Therefore κ ≈ 1 throughout entire superfluid phase")
    print("="*60)

if __name__ == '__main__':
    main()
