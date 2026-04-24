import scanpy as sc
import matplotlib.pyplot as plt

adata = sc.datasets.pbmc68k_reduced()

sc.pp.pca(adata)

plt.scatter(adata.obsm['X_pca'][:,0],
            adata.obsm['X_pca'][:,1],
            s=5)

plt.title("Figure 1")
plt.savefig("Figure1.png", dpi=300)
plt.show()
