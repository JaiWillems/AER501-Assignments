import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

from src.assignment_two.mesh_cases import MeshCases
from src.assignment_two.solvers import FreeVibrationSolver

NUMBER_OF_MODES = 13

meshes = {
    "NELE=1": MeshCases.one_element_per_node(),
    "NELE=2": MeshCases.two_elements_per_node(),
    "NELE=3": MeshCases.three_elements_per_node(),
    "NELE=4": MeshCases.four_elements_per_node()
}

cmap = plt.cm.Spectral(np.linspace(0.15, 0.85, len(meshes)))
mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=cmap)

mode_numbers = range(1, NUMBER_OF_MODES + 1)
for plot_label, mesh in meshes.items():
    results = FreeVibrationSolver.solve(mesh, NUMBER_OF_MODES)
    plt.plot(mode_numbers, results.natural_frequencies(), "-D", label=plot_label)

plt.ylabel("Frequency (Hz)")
plt.xlabel("Eigenmode Number")
plt.legend()
plt.grid()
plt.show()
