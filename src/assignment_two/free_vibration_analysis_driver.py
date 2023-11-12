from matplotlib import pyplot as plt

from src.assignment_two.mesh_cases import MeshCases
from src.assignment_two.solvers import FreeVibrationSolver

plt.style.use("seaborn-v0_8-muted")

number_of_modes = 12
meshes = {
    "NELE=1": MeshCases.one_element_per_node(),
    "NELE=2": MeshCases.two_elements_per_node(),
    "NELE=3": MeshCases.three_elements_per_node(),
    "NELE=4": MeshCases.four_elements_per_node()
}

mode_numbers = range(1, number_of_modes + 1)

for plot_label, mesh in meshes.items():
    results = FreeVibrationSolver.solve(mesh, number_of_modes)
    plt.plot(mode_numbers, results.natural_frequencies(), label=plot_label)

plt.ylabel("Frequency (Hz)")
plt.xlabel("Eigenmode Number")
plt.legend()
plt.grid()
plt.show()
