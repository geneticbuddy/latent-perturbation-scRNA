## 🚀 Run the Demo Notebook

Click below to run the full analysis interactively in Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/geneticbuddy/latent-perturbation-scRNA/blob/main/demo_scanpy_pipeline.ipynb)

---

## Overview

This repository contains code accompanying the manuscript:

**"Latent Space Perturbation Reveals Approximate Additive Gene Effects in Single-Cell Transcriptomic Dynamics"**

This framework analyzes how gene perturbations influence cellular states in latent space using single-cell RNA sequencing data. By projecting gene expression profiles into a learned low-dimensional representation, we quantify how individual and combined perturbations shift cellular embeddings.

---

## Key Features

- Latent space modeling using neural encoders (PyTorch)
- Gene perturbation simulation via partial expression scaling
- Additivity analysis of combined perturbations
- Visualization of transcriptional shifts

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/geneticbuddy/latent-perturbation-scRNA.git
cd latent-perturbation-scRNA
pip install -r requirements.txt

