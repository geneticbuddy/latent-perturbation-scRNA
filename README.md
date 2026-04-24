# Latent Perturbation scRNA Analysis

This repository contains code for the manuscript:

"Latent Space Perturbation Analysis Reveals Approximate Additive Gene Effects in Single-Cell Transcriptomic Dynamics"

## Overview
This project analyzes how gene perturbations shift cellular states in latent space using single-cell RNA-seq data. It evaluates whether gene effects combine additively.

## Dataset
- PBMC dataset (Scanpy: pbmc68k_reduced)

## Requirements
Install dependencies:

pip install scanpy numpy matplotlib torch

## Execution Instructions

Run scripts in the following order:

1. python analysis_pipeline.py  
2. python figure1.py  
3. python figure2.py  
4. python figureS1.py  

## Outputs
- Figure1.png  
- Figure2.png  
- FigureS1.png  

## Reproducibility
All figures can be reproduced directly using the provided scripts and the Scanpy dataset.

## Notes
- Figure 2 values are derived from the perturbation analysis in the pipeline
- No external data download is required

## Author
Avery Hernandez
