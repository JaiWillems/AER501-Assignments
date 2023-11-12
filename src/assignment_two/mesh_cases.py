from src.assignment_two.types import FrameNode, FrameElement, Mesh


class MeshCases:

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
        node_1 = FrameNode(0, 0, True)
        node_2 = FrameNode(0.5, 0)
        node_3 = FrameNode(1, 0)
        node_4 = FrameNode(1, 0.5)
        node_5 = FrameNode(1, 1)
        node_6 = FrameNode(0.5, 1)
        node_7 = FrameNode(0, 1, True)
        node_8 = FrameNode(0.5, 0.5)
        node_9 = FrameNode(1.5, 0)
        node_10 = FrameNode(2, 0)
        node_11 = FrameNode(2, 0.5)
        node_12 = FrameNode(2, 1)
        node_13 = FrameNode(1.5, 1)
        node_14 = FrameNode(1.5, 0.5)
        node_15 = FrameNode(2.5, 0)
        node_16 = FrameNode(3, 0)
        node_17 = FrameNode(3, 0.5)
        node_18 = FrameNode(3, 1)
        node_19 = FrameNode(2.5, 1)
        node_20 = FrameNode(2.5, 0.5)
        return Mesh([
            FrameElement(node_1, node_2),
            FrameElement(node_2, node_3),
            FrameElement(node_3, node_4),
            FrameElement(node_4, node_5),
            FrameElement(node_5, node_6),
            FrameElement(node_6, node_7),
            FrameElement(node_7, node_8),
            FrameElement(node_8, node_3),
            FrameElement(node_3, node_9),
            FrameElement(node_9, node_10),
            FrameElement(node_10, node_11),
            FrameElement(node_11, node_12),
            FrameElement(node_12, node_13),
            FrameElement(node_13, node_5),
            FrameElement(node_5, node_14),
            FrameElement(node_14, node_10),
            FrameElement(node_10, node_15),
            FrameElement(node_15, node_16),
            FrameElement(node_16, node_17),
            FrameElement(node_17, node_18),
            FrameElement(node_18, node_19),
            FrameElement(node_19, node_12),
            FrameElement(node_12, node_20),
            FrameElement(node_20, node_16)
        ])

    @staticmethod
    def three_elements_per_node():
        node_1 = FrameNode(0, 0, True)
        node_2 = FrameNode(0.33333, 0)
        node_3 = FrameNode(0.66667, 0)
        node_4 = FrameNode(1, 0)
        node_5 = FrameNode(1, 0.33333)
        node_6 = FrameNode(1, 0.66667)
        node_7 = FrameNode(1, 1)
        node_8 = FrameNode(0.66667, 1)
        node_9 = FrameNode(0.33333, 1)
        node_10 = FrameNode(0, 1, True)
        node_11 = FrameNode(0.33333, 0.66667)
        node_12 = FrameNode(0.66667, 0.33333)
        node_13 = FrameNode(1.33333, 0)
        node_14 = FrameNode(1.66667, 0)
        node_15 = FrameNode(2, 0)
        node_16 = FrameNode(2, 0.33333)
        node_17 = FrameNode(2, 0.66667)
        node_18 = FrameNode(2, 1)
        node_19 = FrameNode(1.66667, 1)
        node_20 = FrameNode(1.33333, 1)
        node_21 = FrameNode(1.33333, 0.66667)
        node_22 = FrameNode(1.66667, 0.33333)
        node_23 = FrameNode(2.33333, 0)
        node_24 = FrameNode(2.66667, 0)
        node_25 = FrameNode(3, 0)
        node_26 = FrameNode(3, 0.33333)
        node_27 = FrameNode(3, 0.66667)
        node_28 = FrameNode(3, 1)
        node_29 = FrameNode(2.66667, 1)
        node_30 = FrameNode(2.33333, 1)
        node_31 = FrameNode(2.33333, 0.66667)
        node_32 = FrameNode(2.66667, 0.33333)

        return Mesh([
            FrameElement(node_1, node_2),
            FrameElement(node_2, node_3),
            FrameElement(node_3, node_4),
            FrameElement(node_4, node_5),
            FrameElement(node_5, node_6),
            FrameElement(node_6, node_7),
            FrameElement(node_7, node_8),
            FrameElement(node_8, node_9),
            FrameElement(node_9, node_10),
            FrameElement(node_10, node_11),
            FrameElement(node_11, node_12),
            FrameElement(node_12, node_4),
            FrameElement(node_4, node_13),
            FrameElement(node_13, node_14),
            FrameElement(node_14, node_15),
            FrameElement(node_15, node_16),
            FrameElement(node_16, node_17),
            FrameElement(node_17, node_18),
            FrameElement(node_18, node_19),
            FrameElement(node_19, node_20),
            FrameElement(node_20, node_7),
            FrameElement(node_7, node_21),
            FrameElement(node_21, node_22),
            FrameElement(node_22, node_15),
            FrameElement(node_15, node_23),
            FrameElement(node_23, node_24),
            FrameElement(node_24, node_25),
            FrameElement(node_25, node_26),
            FrameElement(node_26, node_27),
            FrameElement(node_27, node_28),
            FrameElement(node_28, node_29),
            FrameElement(node_29, node_30),
            FrameElement(node_30, node_18),
            FrameElement(node_18, node_31),
            FrameElement(node_31, node_32),
            FrameElement(node_32, node_25)
        ])

    @staticmethod
    def four_elements_per_node():
        node_1 = FrameNode(0, 0, True)
        node_2 = FrameNode(0.25, 0)
        node_3 = FrameNode(0.5, 0)
        node_4 = FrameNode(0.75, 0)
        node_5 = FrameNode(1, 0)
        node_6 = FrameNode(1, 0.25)
        node_7 = FrameNode(1, 0.5)
        node_8 = FrameNode(1, 0.75)
        node_9 = FrameNode(1, 1)
        node_10 = FrameNode(0.75, 1)
        node_11 = FrameNode(0.5, 1)
        node_12 = FrameNode(0.25, 1)
        node_13 = FrameNode(0, 1, True)
        node_14 = FrameNode(0.25, 0.75)
        node_15 = FrameNode(0.5, 0.5)
        node_16 = FrameNode(0.75, 0.25)
        node_17 = FrameNode(1.25, 0)
        node_18 = FrameNode(1.5, 0)
        node_19 = FrameNode(1.75, 0)
        node_20 = FrameNode(2, 0)
        node_21 = FrameNode(2, 0.25)
        node_22 = FrameNode(2, 0.5)
        node_23 = FrameNode(2, 0.75)
        node_24 = FrameNode(2, 1)
        node_25 = FrameNode(1.75, 1)
        node_26 = FrameNode(1.5, 1)
        node_27 = FrameNode(1.25, 1)
        node_28 = FrameNode(1.25, 0.75)
        node_29 = FrameNode(1.5, 0.5)
        node_30 = FrameNode(1.75, 0.25)
        node_31 = FrameNode(2.25, 0)
        node_32 = FrameNode(2.5, 0)
        node_33 = FrameNode(2.75, 0)
        node_34 = FrameNode(3, 0)
        node_35 = FrameNode(3, 0.25)
        node_36 = FrameNode(3, 0.5)
        node_37 = FrameNode(3, 0.75)
        node_38 = FrameNode(3, 1)
        node_39 = FrameNode(2.75, 1)
        node_40 = FrameNode(2.5, 1)
        node_41 = FrameNode(2.25, 1)
        node_42 = FrameNode(2.25, 0.75)
        node_43 = FrameNode(2.5, 0.5)
        node_44 = FrameNode(2.75, 0.25)

        return Mesh([
            FrameElement(node_1, node_2),
            FrameElement(node_2, node_3),
            FrameElement(node_3, node_4),
            FrameElement(node_4, node_5),
            FrameElement(node_5, node_6),
            FrameElement(node_6, node_7),
            FrameElement(node_7, node_8),
            FrameElement(node_8, node_9),
            FrameElement(node_9, node_10),
            FrameElement(node_10, node_11),
            FrameElement(node_11, node_12),
            FrameElement(node_12, node_13),
            FrameElement(node_13, node_14),
            FrameElement(node_14, node_15),
            FrameElement(node_15, node_16),
            FrameElement(node_16, node_5),
            FrameElement(node_5, node_17),
            FrameElement(node_17, node_18),
            FrameElement(node_18, node_19),
            FrameElement(node_19, node_20),
            FrameElement(node_20, node_21),
            FrameElement(node_21, node_22),
            FrameElement(node_22, node_23),
            FrameElement(node_23, node_24),
            FrameElement(node_24, node_25),
            FrameElement(node_25, node_26),
            FrameElement(node_26, node_27),
            FrameElement(node_27, node_9),
            FrameElement(node_9, node_28),
            FrameElement(node_28, node_29),
            FrameElement(node_29, node_30),
            FrameElement(node_30, node_20),
            FrameElement(node_20, node_31),
            FrameElement(node_31, node_32),
            FrameElement(node_32, node_33),
            FrameElement(node_33, node_34),
            FrameElement(node_34, node_35),
            FrameElement(node_35, node_36),
            FrameElement(node_36, node_37),
            FrameElement(node_37, node_38),
            FrameElement(node_38, node_39),
            FrameElement(node_39, node_40),
            FrameElement(node_40, node_41),
            FrameElement(node_41, node_24),
            FrameElement(node_24, node_42),
            FrameElement(node_42, node_43),
            FrameElement(node_43, node_44),
            FrameElement(node_44, node_34)
        ])
