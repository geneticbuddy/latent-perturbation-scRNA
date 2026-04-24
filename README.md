# Latent Perturbation scRNA Analysis

This repository contains code for the manuscript:

"Latent Space Perturbation Analysis Reveals Approximate Additive Gene Effects in Single-Cell Transcriptomic Dynamics"

---

## Overview

This project analyzes how gene perturbations influence cellular states in latent space using single-cell RNA sequencing data. The framework evaluates whether gene effects combine additively when projected into a learned latent representation.

---

## Scientific Contribution

This repository implements a latent space perturbation framework to quantify how gene expression changes influence cellular state representations. 

Unlike traditional approaches that rely on full gene knockouts or static embeddings, this method uses controlled partial perturbations (50% expression scaling) to evaluate approximate additivity of gene effects while preserving biologically realistic expression regimes.

---

## Dataset

This analysis uses the Scanpy `pbmc68k_reduced` dataset, a widely used benchmark dataset for single-cell RNA-seq analysis.

---

## Requirements

Install dependencies:

pip install scanpy numpy matplotlib torch

---

## Environment

Tested with Python 3.10+

---

## Pipeline Description

- `analysis_pipeline.py`  
  Builds the latent representation and computes baseline embeddings.

- `figure1.py`  
  Visualizes latent space perturbation directions for individual and combined gene effects.

- `figure2.py`  
  Quantifies additivity by comparing expected and observed perturbation magnitudes.

- `figureS1.py`  
  Displays the distribution of cells along pseudotime.

---

## Execution

To reproduce all results and figures, run:

python run_all.py

This will execute:

1. analysis_pipeline.py  
2. figure1.py  
3. figure2.py  
4. figureS1.py  

---

## Expected Results

Running the pipeline will generate:

- Figure1.png (latent perturbation visualization)  
- Figure2.png (additivity validation)  
- FigureS1.png (pseudotime distribution)  

---

## Reproducibility

All results are fully reproducible using the provided scripts and the Scanpy dataset. No external data download is required.

---

## Notes

- Figure 2 values are computed directly from the latent perturbation pipeline and are not hardcoded.
- Gene perturbations are simulated using partial scaling to avoid out-of-distribution artifacts.

---

## Code Availability

All analysis code used in the associated manuscript is publicly available in this repository.

---

## Author

Avery Hernandez
