from src.assignment_two.types import FrameNode, NodalDisplacement


class ForcedVibrationResults:

    def __init__(self, nodes_to_displacements: dict) -> None:
        """Nodal displacements from forced vibration analysis.

        :param nodes_to_displacements: Dictionary of node keys and nodal
            displacement values.
        """
        self._node_to_displacements = nodes_to_displacements

    def displacement_for_node(self, node: FrameNode) -> NodalDisplacement:
        return self._node_to_displacements[node]
