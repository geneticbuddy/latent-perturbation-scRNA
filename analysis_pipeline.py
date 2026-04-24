import scanpy as sc
import numpy as np
import torch
import torch.nn as nn

# Load dataset
adata = sc.datasets.pbmc68k_reduced()

# Pseudotime
sc.pp.neighbors(adata)
sc.tl.diffmap(adata)
adata.uns['iroot'] = 0
sc.tl.dpt(adata)

# HVGs
if 'highly_variable' not in adata.var:
    sc.pp.highly_variable_genes(adata, n_top_genes=2000)

adata_hvg = adata[:, adata.var['highly_variable']].copy()

# Prepare matrix
X = adata_hvg.X.toarray() if hasattr(adata_hvg.X, "toarray") else adata_hvg.X

# Model
class Encoder(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 2)
        )

    def forward(self, x):
        return self.net(x)

model = Encoder(X.shape[1])

with torch.no_grad():
    z_all = model(torch.tensor(X, dtype=torch.float32)).numpy()

print("Pipeline complete")
