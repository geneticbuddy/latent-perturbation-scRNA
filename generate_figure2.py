# NOTE:
# Values derived from latent perturbation analysis in analysis_pipeline.py
import numpy as np
import matplotlib.pyplot as plt

expected = 0.0016
observed = 0.0015

plt.bar(["Expected", "Observed"], [expected, observed])

plt.ylabel("Shift Magnitude")
plt.title("Figure 2")

plt.savefig("Figure2.png", dpi=300)
plt.show()
