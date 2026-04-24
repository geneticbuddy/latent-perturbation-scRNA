# Latent Space Perturbation Analysis of Gene Effects in Single-Cell RNA-seq

This repository contains code for the manuscript:

**"Latent Space Perturbation Analysis Reveals Approximate Additive Gene Effects in Single-Cell Transcriptomic Dynamics"**

---

## Overview

This framework analyzes how gene perturbations influence cellular states in latent space using single-cell RNA sequencing data. By projecting gene expression profiles into a learned low-dimensional representation, we quantify how individual and combined perturbations shift cellular embeddings.

The central objective is to evaluate whether gene effects exhibit **approximate additivity** in latent space while preserving biologically realistic perturbation regimes.

---

## Scientific Contribution

This work introduces a latent space perturbation framework that enables quantitative evaluation of gene effects using **controlled partial perturbations (50% expression scaling)**.

Unlike traditional approaches that rely on:
- full gene knockouts, or  
- static embeddings  

this method:

- preserves biologically plausible expression levels  
- avoids out-of-distribution artifacts  
- enables direct comparison between expected (additive) and observed (combined) perturbation effects  

This provides a practical approach for probing gene interactions in single-cell systems.

---

## Data Source

This analysis uses the Scanpy dataset:

- `pbmc68k_reduced`

This dataset is a widely used benchmark for single-cell RNA-seq analysis and is included directly within Scanpy, requiring no external downloads.

---

## Method Overview

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
