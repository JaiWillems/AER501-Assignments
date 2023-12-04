from src.assignment_one.part_a.solver.solver import Solver
from src.assignment_one.part_a.types.element import Element
from src.assignment_one.part_a.types.node import Node, BoundaryCondition
from src.assignment_one.part_a.types.vector2d import Vector2d


class AssignmentOneApi:

    @staticmethod
    def solve_10_bar_truss():
        e = 7e10  # Pa.
        a = 0.0001  # m^2.
        p = 100  # N.

        node_one = Node(0, 0, bc=BoundaryCondition.ZERO_DISPLACEMENT)
        node_two = Node(0, 1, bc=BoundaryCondition.ZERO_DISPLACEMENT)
        node_three = Node(1, 0, force=Vector2d(0, -p))
        node_four = Node(1, 1)
        node_five = Node(2, 0, force=Vector2d(0, -p))
        node_six = Node(2, 1)

        return Solver.solve([
            Element(node_two, node_four, e, a),
            Element(node_four, node_six, e, a),
            Element(node_two, node_three, e, a),
            Element(node_one, node_four, e, a),
            Element(node_four, node_three, e, a),
            Element(node_four, node_five, e, a),
            Element(node_three, node_six, e, a),
            Element(node_six, node_five, e, a),
            Element(node_one, node_three, e, a),
            Element(node_three, node_five, e, a),
        ])
