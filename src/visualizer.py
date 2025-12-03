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

Visualization tools for He-II λ-transition κ analysis.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from pathlib import Path
import sys

# Publication-quality settings
mpl.rcParams['figure.dpi'] = 600
mpl.rcParams['savefig.dpi'] = 600
mpl.rcParams['font.size'] = 11
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['axes.labelsize'] = 12
mpl.rcParams['axes.titlesize'] = 13
mpl.rcParams['xtick.labelsize'] = 10
mpl.rcParams['ytick.labelsize'] = 10
mpl.rcParams['legend.fontsize'] = 10
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.markersize'] = 6

class HeliumVisualizer:
    """Visualization for He-II λ-transition analysis."""
    
    def __init__(self, data_path):
        """
        Initialize visualizer.
        
        Parameters
        ----------
        data_path : str
            Path to CSV data file.
        """
        self.data = pd.read_csv(data_path)
        self.T_lambda = 2.1768
        
    def plot_kappa_plateau(self, output_dir='../figures'):
        """
        Figure 1: κ Plateau Throughout Superfluid Phase.
        
        Parameters
        ----------
        output_dir : str
            Output directory path.
        """
        fig, ax = plt.subplots(figsize=(10, 6))
        
        mask = self.data['T'] < self.T_lambda
        data_super = self.data[mask]
        
        ax.semilogx(data_super['t'], data_super['kappa'], 
                   'o-', color='#e74c3c', alpha=0.7, 
                   label='κ(t)', markersize=4)
        
        ax.axhline(y=1.0, color='k', linestyle='--', 
                  linewidth=1.5, alpha=0.5, label='κ = 1')
        
        kappa_mean = data_super['kappa'].mean()
        kappa_std = data_super['kappa'].std()
        ax.axhspan(kappa_mean - kappa_std, kappa_mean + kappa_std,
                  alpha=0.2, color='green', label=f'κ = {kappa_mean:.3f} ± {kappa_std:.3f}')
        
        ax.axvline(x=1e-9, color='purple', linestyle=':', 
                  linewidth=2, alpha=0.7, label='Critical point (t→0)')
        
        ax.set_xlabel('Reduced Temperature t = |1 - T/T$_λ$|', fontsize=13)
        ax.set_ylabel('Emergence Parameter κ', fontsize=13)
        ax.set_title('He-II: κ Plateau in Superfluid Phase', 
                    fontsize=14, fontweight='bold')
        ax.legend(loc='best', framealpha=0.9)
        ax.grid(True, alpha=0.3, which='both')
        ax.set_xlim(data_super['t'].min() * 0.8, data_super['t'].max() * 1.2)
        
        ax.text(0.5, 0.95, 'κ ≈ 1: Stable Emergent State', 
               transform=ax.transAxes, fontsize=11,
               bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.3),
               verticalalignment='top', horizontalalignment='center')
        
        Path(output_dir).mkdir(exist_ok=True)
        plt.tight_layout()
        plt.savefig(f'{output_dir}/fig1_kappa_plateau.png', dpi=600, bbox_inches='tight')
        print(f"Saved: {output_dir}/fig1_kappa_plateau.png")
        plt.close()
        
    def plot_component_analysis(self, output_dir='../figures'):
        """
        Figure 2: Component Analysis (τ and Λ/Λ_c).
        
        Parameters
        ----------
        output_dir : str
            Output directory path.
        """
        mask = self.data['T'] < self.T_lambda
        data_super = self.data[mask]
        
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 10))
        
        # Panel 1: Superfluid density
        ax1.loglog(data_super['t'], data_super['rho_s'], 
                  'o-', color='#3498db', alpha=0.7, markersize=4)
        ax1.set_ylabel('τ = ρ$_s$/ρ\n(Topological Order)', fontsize=12)
        ax1.set_title('Component Analysis: τ ∝ t$^{ζ}$ and Λ ∝ t$^{-ν}$', 
                     fontsize=13, fontweight='bold')
        ax1.grid(True, alpha=0.3, which='both')
        ax1.text(0.05, 0.95, f'ζ = 0.6705', transform=ax1.transAxes,
                fontsize=10, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
        
        # Panel 2: Correlation length
        ax2.loglog(data_super['t'], data_super['xi_norm'], 
                  'o-', color='#f39c12', alpha=0.7, markersize=4)
        ax2.set_ylabel('Λ/Λ$_c$ = ξ/ξ$_{ref}$\n(Correlation)', fontsize=12)
        ax2.grid(True, alpha=0.3, which='both')
        ax2.text(0.05, 0.95, f'ν = 0.6717', transform=ax2.transAxes,
                fontsize=10, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        # Panel 3: κ
        ax3.semilogx(data_super['t'], data_super['kappa'], 
                    'o-', color='#e74c3c', alpha=0.7, markersize=4)
        ax3.axhline(y=1.0, color='k', linestyle='--', linewidth=1.5, alpha=0.5)
        ax3.set_ylabel('κ = τ × (Λ/Λ$_c$)', fontsize=12)
        ax3.set_xlabel('Reduced Temperature t = |1 - T/T$_λ$|', fontsize=13)
        ax3.grid(True, alpha=0.3, which='both')
        
        exponent = 0.6705 - 0.6717
        ax3.text(0.5, 0.95, f'κ ∝ t$^{{ζ-ν}}$ = t$^{{{exponent:.4f}}}$ ≈ const', 
                transform=ax3.transAxes, fontsize=11,
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5),
                verticalalignment='top', horizontalalignment='center')
        
        plt.tight_layout()
        plt.savefig(f'{output_dir}/fig2_component_analysis.png', dpi=600, bbox_inches='tight')
        print(f"Saved: {output_dir}/fig2_component_analysis.png")
        plt.close()
        
    def plot_phase_diagram(self, output_dir='../figures'):
        """
        Figure 3: Phase Diagram with κ Regimes.
        
        Parameters
        ----------
        output_dir : str
            Output directory path.
        """
        fig, ax = plt.subplots(figsize=(10, 6))
        
        T_full = np.linspace(0.5, 2.5, 1000)
        kappa_full = np.zeros_like(T_full)
        mask_super = T_full < self.T_lambda
        
        kappa_full[mask_super] = 1.0
        kappa_full[~mask_super] = 0.0
        
        ax.plot(T_full[mask_super], kappa_full[mask_super], 
               'r-', linewidth=3, label='Superfluid (He-II): κ ≈ 1')
        ax.plot(T_full[~mask_super], kappa_full[~mask_super], 
               'b-', linewidth=3, label='Normal (He-I): κ = 0')
        
        ax.axvline(x=self.T_lambda, color='purple', linestyle='--', 
                  linewidth=2, alpha=0.7)
        ax.text(self.T_lambda, 0.5, f'  T$_λ$ = {self.T_lambda} K',
               rotation=90, verticalalignment='center', fontsize=11,
               bbox=dict(boxstyle='round', facecolor='lavender', alpha=0.7))
        
        ax.axvspan(0.5, self.T_lambda, alpha=0.2, color='red', label='Emergent Phase')
        ax.axvspan(self.T_lambda, 2.5, alpha=0.2, color='blue', label='Non-Emergent')
        
        ax.set_xlabel('Temperature T (K)', fontsize=13)
        ax.set_ylabel('Emergence Parameter κ', fontsize=13)
        ax.set_title('He-II Phase Diagram: Emergent vs Non-Emergent States', 
                    fontsize=14, fontweight='bold')
        ax.set_ylim(-0.1, 1.3)
        ax.legend(loc='upper right', framealpha=0.9)
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(f'{output_dir}/fig3_phase_diagram.png', dpi=600, bbox_inches='tight')
        print(f"Saved: {output_dir}/fig3_phase_diagram.png")
        plt.close()
        
    def plot_scaling_verification(self, output_dir='../figures'):
        """
        Figure 4: Verification of κ ∝ t^(ζ-ν) ≈ const.
        
        Parameters
        ----------
        output_dir : str
            Output directory path.
        """
        mask = self.data['T'] < self.T_lambda
        data_super = self.data[mask]
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        exponent = 0.6705 - 0.6717
        theory = np.power(data_super['t'].values, exponent)
        theory_normalized = theory / theory[len(theory)//2] * data_super['kappa'].iloc[len(theory)//2]
        
        ax1.loglog(data_super['t'], data_super['kappa'], 
                  'o', color='#e74c3c', alpha=0.6, markersize=5, label='Calculated κ')
        ax1.loglog(data_super['t'], theory_normalized, 
                  'k--', linewidth=2, alpha=0.7, label=f'Theory: κ ∝ t$^{{{exponent:.4f}}}$')
        
        ax1.set_xlabel('Reduced Temperature t', fontsize=12)
        ax1.set_ylabel('κ', fontsize=12)
        ax1.set_title('Scaling Verification (log-log)', fontsize=13, fontweight='bold')
        ax1.legend(loc='best', framealpha=0.9)
        ax1.grid(True, alpha=0.3, which='both')
        
        ax2.plot(data_super['t'], data_super['kappa'], 
                'o-', color='#e74c3c', alpha=0.7, markersize=4)
        
        mean_kappa = data_super['kappa'].mean()
        ax2.axhline(y=mean_kappa, color='green', linestyle='--', 
                   linewidth=2, label=f'Mean: {mean_kappa:.4f}')
        ax2.axhline(y=1.0, color='k', linestyle=':', 
                   linewidth=1.5, alpha=0.5, label='κ = 1')
        
        ax2.set_xlabel('Reduced Temperature t', fontsize=12)
        ax2.set_ylabel('κ', fontsize=12)
        ax2.set_title('κ ≈ const Plateau (linear scale)', fontsize=13, fontweight='bold')
        ax2.legend(loc='best', framealpha=0.9)
        ax2.grid(True, alpha=0.3)
        ax2.set_xscale('log')
        
        plt.tight_layout()
        plt.savefig(f'{output_dir}/fig4_scaling_verification.png', dpi=600, bbox_inches='tight')
        print(f"Saved: {output_dir}/fig4_scaling_verification.png")
        plt.close()
        
    def generate_all_figures(self, output_dir='../figures'):
        """
        Generate all publication-quality figures.
        
        Parameters
        ----------
        output_dir : str
            Output directory path.
        """
        print("\n" + "="*60)
        print("Generating Publication Figures")
        print("="*60)
        
        self.plot_kappa_plateau(output_dir)
        self.plot_component_analysis(output_dir)
        self.plot_phase_diagram(output_dir)
        self.plot_scaling_verification(output_dir)
        
        print("="*60)
        print("All figures generated")
        print(f"Location: {output_dir}/")
        print("="*60)

def main():
    """Main visualization pipeline."""
    if len(sys.argv) < 2:
        print("Usage: python visualizer.py <data_csv_path>")
        print("Example: python visualizer.py ../results/kappa_analysis.csv")
        sys.exit(1)
    
    data_path = sys.argv[1]
    
    viz = HeliumVisualizer(data_path)
    viz.generate_all_figures()

if __name__ == '__main__':
    main()
