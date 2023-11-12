from src.assignment_two.types import FrameNode, FrameElement, Mesh


class MeshTypes:

    @staticmethod
    def one_element_per_node():
        node_1 = FrameNode(0, 0, True)
        node_2 = FrameNode(0, 1, True)
        node_3 = FrameNode(1, 0)
        node_4 = FrameNode(1, 1)
        node_5 = FrameNode(2, 0)
        node_6 = FrameNode(2, 1)
        node_7 = FrameNode(3, 0)
        node_8 = FrameNode(3, 1)
        return Mesh([
            FrameElement(node_1, node_3),
            FrameElement(node_3, node_4),
            FrameElement(node_2, node_4),
            FrameElement(node_2, node_3),
            FrameElement(node_3, node_5),
            FrameElement(node_5, node_6),
            FrameElement(node_4, node_6),
            FrameElement(node_4, node_5),
            FrameElement(node_5, node_7),
            FrameElement(node_7, node_8),
            FrameElement(node_6, node_8),
            FrameElement(node_6, node_7)
        ])

    @staticmethod
    def two_elements_per_node():
        raise NotImplementedError(
            "The two stiffness_matrix mesh is not implemented.")

    @staticmethod
    def three_elements_per_node():
        raise NotImplementedError(
            "The three stiffness_matrix mesh is not implemented.")

    @staticmethod
    def four_elements_per_node():
        raise NotImplementedError(
            "The four stiffness_matrix mesh is not implemented.")
