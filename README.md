# Latent Perturbation scRNA Analysis

This repository contains code for the manuscript:

"Latent Space Perturbation Analysis Reveals Approximate Additive Gene Effects in Single-Cell Transcriptomic Dynamics"

## Overview
This project analyzes gene perturbations in latent space using single-cell RNA-seq data and evaluates approximate additivity of gene effects.

## Dataset
- PBMC dataset (Scanpy: pbmc68k_reduced)

## Requirements
- scanpy
- numpy
- matplotlib
- torch

Install dependencies:
pip install scanpy numpy matplotlib torch

## Execution Order
Run scripts in the following order:

1. analysis_pipeline.py
2. figure1.py
3. figure2.py
3. figureS1.py

## Outputs
- Figure1.png
- Figure2.png
- FigureS1.png

## Reproducibility
All figures can be reproduced directly using the provided scripts and the Scanpy dataset.

## Author
Avery Hernandez
