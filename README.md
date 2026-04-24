# Latent Space Perturbation Analysis of Gene Effects in Single-Cell RNA-seq

This repository contains code for the manuscript:

**"Latent Space Perturbation Analysis Reveals Approximate Additive Gene Effects in Single-Cell Transcriptomic Dynamics"**

---

## Overview

This framework analyzes how gene perturbations influence cellular states in latent space using single-cell RNA sequencing data. By projecting gene expression profiles into a learned low-dimensional representation, we quantify how individual and combined perturbations shift cellular embeddings.

The central objective is to evaluate whether gene effects exhibit **approximate additivity** in latent space while preserving biologically realistic perturbation regimes.

---

## Quick Start

Clone the repository and run the full pipeline:

git clone https://github.com/geneticbuddy/latent-perturbation-scRNA  
cd latent-perturbation-scRNA  
pip install -r requirements.txt  
python run_all.py  

---

## Scientific Contribution

This work introduces a latent space perturbation framework that enables quantitative evaluation of gene effects using **controlled partial perturbations (50% expression scaling)**.

Unlike traditional approaches that rely on:
- full gene knockouts  
- static embeddings  

this method:

- preserves biologically plausible expression levels  
- avoids out-of-distribution artifacts  
- enables direct comparison between expected (additive) and observed (combined) perturbation effects  

This approach builds on prior latent space perturbation methods (e.g., vector arithmetic models) but emphasizes controlled partial perturbations and direct empirical validation of additive structure.

---

## Data Source

This analysis uses the Scanpy dataset:

- `pbmc68k_reduced`

This dataset is a widely used benchmark for single-cell RNA-seq analysis and is included directly within Scanpy, requiring no external downloads.

---

## 🔬 Method Overview

The pipeline consists of four stages:

1. **Latent Representation Construction**  
   Gene expression data are embedded into a low-dimensional latent space using a neural encoder.

2. **Pseudotime Inference**  
   Cellular progression is modeled using diffusion pseudotime (DPT).

3. **Perturbation Simulation**  
   Gene perturbations are simulated via partial expression scaling (50%).

4. **Additivity Evaluation**  
   Expected perturbation effects (vector sums) are compared to observed combined perturbations.

---

## Repository Structure

analysis_pipeline.py   # Builds latent space and baseline embeddings  
figure1.py            # Latent perturbation visualization  
figure2.py            # Additivity validation analysis  
figureS1.py           # Pseudotime distribution  
run_all.py            # Executes full pipeline  
requirements.txt      # Dependencies  

---

## ⚙️ Installation

Install dependencies:

pip install -r requirements.txt

---

## 🚀 Execution

To reproduce all results and figures:

python run_all.py

This performs end-to-end analysis, from latent space construction to perturbation evaluation and figure generation.

---

## Expected Outputs

Running the pipeline generates:

- Figure1.png — Latent perturbation visualization  
- Figure2.png — Additivity validation  
- FigureS1.png — Pseudotime distribution  

---

## Reproducibility

All results are fully reproducible using the provided scripts and the Scanpy dataset. No external data download is required.

---

## Assumptions

This framework assumes:

- Gene perturbations can be approximated as vector shifts in latent space  
- Combined perturbations can be evaluated through additive composition of these shifts  

---

## Limitations

- The analysis uses a reduced and preprocessed dataset, which may not capture the full complexity of biological systems  
- The neural encoder is relatively simple and may not fully model higher-order nonlinear gene interactions  

Future work may incorporate more expressive models and larger datasets.

---

## Notes

- Figure 2 values are computed directly from the perturbation pipeline (not hardcoded)  
- Partial perturbation scaling is used to maintain biological realism  

---

## Code Availability

All analysis code used in the associated manuscript is publicly available:

https://github.com/geneticbuddy/latent-perturbation-scRNA

---

## Author

Avery Hernandez  
Independent Researcher
