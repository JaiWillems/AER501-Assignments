import numpy as np
from matplotlib import pyplot as plt

from src.assignment_two.mesh_cases import MeshCases
from src.assignment_two.solvers import ForcedVibrationFullOrderSolver
from src.assignment_two.types import FrameNode

plt.style.use("seaborn-v0_8-muted")

PROPORTIONAL_STIFFNESS_DAMPING_FACTOR = 0.0
PROPORTIONAL_MASS_DAMPING_FACTOR = 10.0

MINIMUM_FREQUENCY_HZ = 0
MAXIMUM_FREQUENCY_HZ = 250
NUMBER_OF_POINTS = 1000

NODE_OF_INTEREST_X = 3
NODE_OF_INTEREST_Y = 0
NODE_OF_INTEREST_CONSTRAINED = False

meshes = {
    "NELE=1": MeshCases.one_element_per_node(),
    "NELE=2": MeshCases.two_elements_per_node(),
    "NELE=3": MeshCases.three_elements_per_node(),
    "NELE=4": MeshCases.four_elements_per_node()
}

node_of_interest = FrameNode(
    NODE_OF_INTEREST_X,
    NODE_OF_INTEREST_Y,
    NODE_OF_INTEREST_CONSTRAINED
)

excitation_frequency_range = np.linspace(
    MINIMUM_FREQUENCY_HZ,
    MAXIMUM_FREQUENCY_HZ,
    NUMBER_OF_POINTS
)
for plot_label, mesh in meshes.items():

    desired_node_displacements = []

    for excitation_frequency in excitation_frequency_range:
        nodal_information = ForcedVibrationFullOrderSolver.solve(
            mesh,
            float(excitation_frequency),
            PROPORTIONAL_STIFFNESS_DAMPING_FACTOR,
            PROPORTIONAL_MASS_DAMPING_FACTOR
        )
        nodal_displacement = nodal_information.displacement_for_node(
            node_of_interest
        )
        desired_node_displacements.append(nodal_displacement.absolute_x())

    plt.semilogy(
        excitation_frequency_range,
        desired_node_displacements,
        label=plot_label
    )

plt.ylabel("Displacement Response")
plt.xlabel("Frequency (Hz)")
plt.legend()
plt.grid()
plt.show()
