# Curcuminoid Biosynthesis Enzyme Comparison

## Overview
This repository contains a literature-based comparative analysis of the curcuminoid
biosynthesis pathway in turmeric (*Curcuma longa*), focusing on the four key
enzymes: **CURS1, CURS2, CURS3** (curcumin synthase isoforms) and **DCS**
(diketide-CoA synthase). These are Type III polyketide synthase enzymes
responsible for producing curcumin, demethoxycurcumin, and bisdemethoxycurcumin.

**This is a literature synthesis project, not a novel wet-lab or sequencing
study.** All numerical and structural data below are drawn directly from
previously published, peer-reviewed research, cited explicitly below and inline
in the analysis script. The contribution of this project is the comparative
synthesis, computation of derived comparisons, and visualization of these
published findings — not new experimental data generation.

## Why This Project
This project connects back to my final-year research project, which used
Curcuma longa (along with Azadirachta indica and Camellia sinensis) to develop
a polyherbal anti-aging formulation. That project worked with the whole plant
extract; this project looks one level deeper, at the specific enzymes
responsible for producing curcumin, one of the key bioactive compounds in that
extract.

## Data Sources
1. Santhoshkumar, R. & Yusuf, A. (2020). *In silico structural modeling and
   analysis of physicochemical properties of curcumin synthase (CURS1, CURS2,
   and CURS3) proteins of Curcuma longa.* Journal of Genetic Engineering and
   Biotechnology. https://doi.org/10.1186/s43141-020-00041-x
2. Katsuyama, Y. et al. (2009). *Identification and characterization of
   multiple curcumin synthases from the herb Curcuma longa.* FEBS Letters.
   https://doi.org/10.1016/j.febslet.2009.07.029
3. Structural and biochemical elucidation of mechanism for decarboxylative
   condensation of beta-keto acid by curcumin synthase. PubMed ID: 21148316.
4. Chakraborty, A. et al. (2021). *Genome sequencing of turmeric provides
   evolutionary insights into its medicinal properties.* Communications
   Biology. https://doi.org/10.1038/s42003-021-02720-y

## Repository Contents
| File | Description |
|---|---|
| `curcuminoid_enzyme_comparison.py` | Python script compiling and visualizing published physicochemical, structural, and genetic data for CURS1/2/3/DCS |
| `curs_physicochemical_comparison.png` | Generated comparison chart (molecular weight, pI, secondary structure) |
| `DESeq2_analysis.R` | R script for differential expression analysis and heatmap visualization using DESeq2/pheatmap |
| `Training_Log_NGS.txt` | Documentation of hands-on NGS training (Linux, FastQC, Trimmomatic, BWA, BCFtools, Nextflow) |

## What the Analysis Covers
- Molecular weight, theoretical pI, and aliphatic index of CURS1/2/3
- Secondary structure composition (alpha helix / extended strand / random coil)
- Substrate preferences of each enzyme (which curcuminoids each one produces)
- Gene structure (exon/intron count) for all four genes
- Catalytic triad and gatekeeper residues from the published CURS1 crystal
  structure (PDB: 3OV2)
- NCBI accession numbers for all four genes

## Skills Demonstrated
- Literature-based bioinformatics data synthesis and citation practice
- Python (matplotlib) for scientific data visualization
- R/RStudio: DESeq2, pheatmap, differential expression analysis
- NGS Workflow: Quality control, read mapping, variant calling
- Nextflow: nf-core/viralrecon pipeline execution
- Linux: Command-line bioinformatics tools

## Planned Next Steps
This project is a foundation for future genome-mining work (e.g., antiSMASH-style
biosynthetic gene cluster analysis) once I have access to appropriate
computational infrastructure and training — genuine hands-on experience with
these tools is something I'm seeking through further study, not something I
currently claim to have completed.
## Related Work
See also: github.com/talhaayub597/Turmeric-Transcriptomics — differential expression analysis of turmeric rhizome vs. leaf tissue (NCBI GEO: GSE16733).

## Author
Talha Ayub
- GitHub: github.com/talhaayub597
- ORCID: orcid.org/0009-0000-0869-6338
- Email: talhaayub597@gmail.com

## License
MIT
