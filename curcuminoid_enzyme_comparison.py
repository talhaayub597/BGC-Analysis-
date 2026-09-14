"""
Comparative Structural and Biochemical Analysis of Curcuminoid Biosynthesis
Enzymes (CURS1, CURS2, CURS3, DCS) in Curcuma longa (Turmeric)

Author: Talha Ayub
Purpose: Independent literature-based bioinformatics synthesis project.

IMPORTANT — DATA SOURCE DISCLOSURE:
All numerical values in this script are taken directly from previously
published, peer-reviewed literature (cited inline and in README.md).
This script does NOT generate novel wet-lab or sequencing data. It
synthesizes, compares, and visualizes existing published findings on
the curcuminoid biosynthesis pathway (Type III polyketide synthases).

Primary sources:
1. Santhoshkumar, R. & Yusuf, A. (2020). In silico structural modeling
   and analysis of physicochemical properties of curcumin synthase
   (CURS1, CURS2, and CURS3) proteins of Curcuma longa.
   J Genet Eng Biotechnol. https://doi.org/10.1186/s43141-020-00041-x
2. Katsuyama, Y. et al. (2009). Identification and characterization of
   multiple curcumin synthases from the herb Curcuma longa. FEBS Letters.
   https://doi.org/10.1016/j.febslet.2009.07.029
3. Structural and biochemical elucidation of mechanism for decarboxylative
   condensation of beta-keto acid by curcumin synthase. PubMed: 21148316.
4. Chakraborty, A. et al. (2021). Genome sequencing of turmeric provides
   evolutionary insights into its medicinal properties. Commun Biol.
   https://doi.org/10.1038/s42003-021-02720-y
"""

import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------------------------
# REAL, PUBLISHED DATA (Santhoshkumar & Yusuf, 2020)
# ---------------------------------------------------------------------
enzymes = ["CURS1", "CURS2", "CURS3"]

molecular_weight_da = [21093.19, 20266.13, 20629.52]
theoretical_pI = [4.93, 5.28, 4.96]
aliphatic_index = [99.19, 89.30, 86.37]
alpha_helix_pct = [42.72, 41.38, 44.74]
random_coil_pct = [24.87, 31.03, 17.89]
extended_strand_pct = [16.24, 19.40, 17.89]
qmean_z_score = [-0.83, -0.89, -1.09]

# NCBI accession numbers (Chakraborty et al. 2021 / Katsuyama et al. 2009)
accessions = {
    "CURS1": "BAH56226",
    "CURS2": "AB506762",
    "CURS3": "AB506763",
    "DCS": "BAH56225",
}

# Substrate preference (Katsuyama et al. 2009 — enzymatic characterization)
substrate_preference = {
    "CURS1": "feruloyl-CoA + diketide-CoA (curcumin)",
    "CURS2": "feruloyl-CoA (curcumin / demethoxycurcumin)",
    "CURS3": "feruloyl-CoA + p-coumaroyl-CoA (curcumin, bisdemethoxycurcumin, demethoxycurcumin)",
}

# Catalytic triad residues, CURS1 crystal structure (PDB: 3OV2)
catalytic_triad_curs1 = {"Cys": 164, "His": 303, "Asn": 336}
gatekeeper_residues_curs1 = {"Phe": [215, 265]}

# Gene structure (Chakraborty et al. 2021)
gene_structure = {
    "CURS1": {"exons": 2, "introns": 1},
    "CURS2": {"exons": 2, "introns": 1},
    "CURS3": {"exons": 2, "introns": 1},
    "DCS": {"exons": 3, "introns": 2},
}


def print_summary():
    print("=" * 70)
    print("CURCUMINOID BIOSYNTHESIS ENZYME COMPARISON (published data)")
    print("=" * 70)
    for i, enz in enumerate(enzymes):
        print(f"\n{enz} (NCBI: {accessions[enz]})")
        print(f"  Molecular weight   : {molecular_weight_da[i]:.2f} Da")
        print(f"  Theoretical pI     : {theoretical_pI[i]}")
        print(f"  Aliphatic index    : {aliphatic_index[i]}")
        print(f"  Secondary structure: {alpha_helix_pct[i]}% helix, "
              f"{extended_strand_pct[i]}% strand, {random_coil_pct[i]}% coil")
        print(f"  QMEAN Z-score      : {qmean_z_score[i]}")
        print(f"  Substrate preference: {substrate_preference[enz]}")
        print(f"  Gene structure     : {gene_structure[enz]['exons']} exons, "
              f"{gene_structure[enz]['introns']} intron(s)")

    print(f"\nDCS (NCBI: {accessions['DCS']})")
    print(f"  Gene structure     : {gene_structure['DCS']['exons']} exons, "
          f"{gene_structure['DCS']['introns']} introns")
    print(f"\nCURS1 catalytic triad (PDB 3OV2): {catalytic_triad_curs1}")
    print(f"CURS1 gatekeeper residues: {gatekeeper_residues_curs1}")


def plot_physicochemical_comparison(outpath="curs_physicochemical_comparison.png"):
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

    axes[0].bar(enzymes, molecular_weight_da, color=["#2b6cb0", "#2f855a", "#c05621"])
    axes[0].set_title("Molecular Weight (Da)")
    axes[0].set_ylabel("Da")

    axes[1].bar(enzymes, theoretical_pI, color=["#2b6cb0", "#2f855a", "#c05621"])
    axes[1].set_title("Theoretical pI")
    axes[1].set_ylabel("pI")

    x = np.arange(len(enzymes))
    width = 0.25
    axes[2].bar(x - width, alpha_helix_pct, width, label="Alpha helix", color="#2b6cb0")
    axes[2].bar(x, extended_strand_pct, width, label="Extended strand", color="#2f855a")
    axes[2].bar(x + width, random_coil_pct, width, label="Random coil", color="#c05621")
    axes[2].set_xticks(x)
    axes[2].set_xticklabels(enzymes)
    axes[2].set_title("Secondary Structure Composition (%)")
    axes[2].legend(fontsize=8)

    plt.suptitle("Curcumin Synthase Isoforms: Published Physicochemical Comparison\n"
                  "(Data: Santhoshkumar & Yusuf, 2020)", fontsize=11)
    plt.tight_layout()
    plt.savefig(outpath, dpi=150)
    print(f"\nSaved chart: {outpath}")


if __name__ == "__main__":
    print_summary()
    plot_physicochemical_comparison()
