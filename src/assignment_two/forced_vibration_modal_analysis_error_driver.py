import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

from src.assignment_two.mesh_cases import MeshCases
from src.assignment_two.solvers import ForcedVibrationFullOrderSolver, ForcedVibrationModalAnalysisSolver
from src.assignment_two.types import FrameNode

MESH = MeshCases.four_elements_per_node()

MODES = [13, 14, 15, 16, 17, 18, 19]

PROPORTIONAL_STIFFNESS_DAMPING_FACTOR = 0.0
PROPORTIONAL_MASS_DAMPING_FACTOR = 10.0

MINIMUM_FREQUENCY_HZ = 0
MAXIMUM_FREQUENCY_HZ = 250
NUMBER_OF_POINTS = 500

NODE_OF_INTEREST_X = 3
NODE_OF_INTEREST_Y = 0
NODE_OF_INTEREST_CONSTRAINED = False

node_of_interest = FrameNode(
    NODE_OF_INTEREST_X,
    NODE_OF_INTEREST_Y,
    NODE_OF_INTEREST_CONSTRAINED
)

cmap = plt.cm.Spectral(np.linspace(0, 1, len(MODES)))
mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=cmap)

excitation_frequency_range = np.linspace(
    MINIMUM_FREQUENCY_HZ,
    MAXIMUM_FREQUENCY_HZ,
    NUMBER_OF_POINTS
)

full_order_displacements = []
for excitation_frequency in excitation_frequency_range:
    full_order_results = ForcedVibrationFullOrderSolver.solve(
        MESH,
        float(excitation_frequency),
        PROPORTIONAL_STIFFNESS_DAMPING_FACTOR,
        PROPORTIONAL_MASS_DAMPING_FACTOR
    )
    full_order_displacements.append(
        full_order_results.displacement_for_node(node_of_interest).absolute_x()
    )

for number_of_modes in MODES:

    displacement_error = []

    for i, excitation_frequency in enumerate(excitation_frequency_range):
        modal_analysis_results = ForcedVibrationModalAnalysisSolver.solve(
            MESH,
            number_of_modes,
            float(excitation_frequency),
            PROPORTIONAL_STIFFNESS_DAMPING_FACTOR,
            PROPORTIONAL_MASS_DAMPING_FACTOR
        )
        modal_analysis_displacement = modal_analysis_results.displacement_for_node(
            node_of_interest
        ).absolute_x()

        displacement_error.append(
            abs(modal_analysis_displacement - full_order_displacements[i])
        )

    plt.semilogy(
        excitation_frequency_range,
        displacement_error,
        label=f"NOM={number_of_modes}"
    )

plt.ylabel("Displacement Error")
plt.xlabel("Frequency (Hz)")
plt.legend()
plt.grid()
plt.show()
