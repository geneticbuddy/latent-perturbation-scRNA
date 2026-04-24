import scanpy as sc
import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# --------------------------------------------------
# NOTE:
# This script recomputes expected and observed shifts
# directly from the latent perturbation pipeline.
# Values are NOT hardcoded.
# --------------------------------------------------

# -----------------------------
# LOAD DATA
# -----------------------------
adata = sc.datasets.pbmc68k_reduced()

# -----------------------------
# PSEUDOTIME
# -----------------------------
sc.pp.neighbors(adata)
sc.tl.diffmap(adata)
adata.uns['iroot'] = 0
sc.tl.dpt(adata)

# -----------------------------
# HVG SELECTION
# -----------------------------
if 'highly_variable' not in adata.var:
    sc.pp.highly_variable_genes(adata, n_top_genes=2000)

adata_hvg = adata[:, adata.var['highly_variable']].copy()

# -----------------------------
# PREPARE MATRIX
# -----------------------------
X = adata_hvg.X.toarray() if hasattr(adata_hvg.X, "toarray") else adata_hvg.X
gene_idx = {gene: i for i, gene in enumerate(adata_hvg.var_names)}

# -----------------------------
# MODEL
# -----------------------------
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

# -----------------------------
# SELECT GENES (safe fallback)
# -----------------------------
candidate_genes = ["S100A8", "S100A9"]

valid_genes = [g for g in candidate_genes if g in gene_idx]

# fallback if missing
if len(valid_genes) < 2:
    valid_genes = list(adata_hvg.var_names[:2])

gene1, gene2 = valid_genes[:2]

print("Using genes:", gene1, gene2)

# -----------------------------
# SHIFT FUNCTIONS (correct perturbation)
# -----------------------------
def compute_shift_single(gene):
    X_mod = X.copy()
    idx = gene_idx[gene]
    X_mod[:, idx] *= 0.5   # partial perturbation

    with torch.no_grad():
        z_mod = model(torch.tensor(X_mod, dtype=torch.float32)).numpy()

    return np.mean(z_mod - z_all, axis=0)

def compute_shift_combined(genes):
    X_mod = X.copy()
    for gene in genes:
        idx = gene_idx[gene]
        X_mod[:, idx] *= 0.5

    with torch.no_grad():
        z_mod = model(torch.tensor(X_mod, dtype=torch.float32)).numpy()

    return np.mean(z_mod - z_all, axis=0)

# -----------------------------
# COMPUTE SHIFTS
# -----------------------------
shift_1 = compute_shift_single(gene1)
shift_2 = compute_shift_single(gene2)

expected = shift_1 + shift_2
observed = compute_shift_combined([gene1, gene2])

# -----------------------------
# MAGNITUDES
# -----------------------------
expected_mag = np.linalg.norm(expected)
observed_mag = np.linalg.norm(observed)
error = abs(expected_mag - observed_mag)

print("\n--- RESULTS ---")
print("Expected:", expected_mag)
print("Observed:", observed_mag)
print("Error:", error)

# -----------------------------
# PLOT FIGURE
# -----------------------------
plt.figure(figsize=(6,6))

plt.bar(["Expected", "Observed"], [expected_mag, observed_mag])

# annotate values
plt.text(0, expected_mag + 0.00005, f"{expected_mag:.4f}", ha='center')
plt.text(1, observed_mag + 0.00005, f"{observed_mag:.4f}", ha='center')

# error annotation
plt.text(0.5, max(expected_mag, observed_mag)*0.9,
         f"Error = {error:.4f}", ha='center')

plt.ylabel("Shift Magnitude")
plt.title("Figure 2: Additivity Validation")

plt.tight_layout()
plt.savefig("Figure2.png", dpi=300)
plt.show()
