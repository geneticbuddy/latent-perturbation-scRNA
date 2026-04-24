import scanpy as sc
import matplotlib.pyplot as plt
import numpy as np

adata = sc.datasets.pbmc68k_reduced()

sc.pp.neighbors(adata)
sc.tl.diffmap(adata)
adata.uns['iroot'] = 0
sc.tl.dpt(adata)

pseudotime = adata.obs['dpt_pseudotime'].values
pseudotime = pseudotime[~np.isnan(pseudotime)]

mean_pt = np.mean(pseudotime)
median_pt = np.median(pseudotime)

plt.hist(pseudotime, bins=40)
plt.axvline(mean_pt, linestyle='--', label='Mean')
plt.axvline(median_pt, linestyle=':', label='Median')

plt.xlabel("Pseudotime")
plt.ylabel("Cell Count")
plt.title("Figure S1")

plt.legend()
plt.savefig("FigureS1.png", dpi=300)
plt.show()
