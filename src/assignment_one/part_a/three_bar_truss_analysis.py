from src.assignment_one.part_a.solver.solver import Solver
from src.assignment_one.part_a.types.element import Element
from src.assignment_one.part_a.types.node import Node, BoundaryCondition
from src.assignment_one.part_a.types.vector2d import Vector2d

E = 7e10  # Pa.
A = 0.0001  # m^2.
P = 100  # N.

node_one = Node(0, 0, bc=BoundaryCondition.ZERO_DISPLACEMENT)
node_two = Node(1, 0, bc=BoundaryCondition.ZERO_DISPLACEMENT)
node_three = Node(2, 0, bc=BoundaryCondition.ZERO_DISPLACEMENT)
node_four = Node(1, -1, force=Vector2d(P, 0))

element_one = Element(node_one, node_four, E, A)
element_two = Element(node_four, node_two, E, A)
element_three = Element(node_four, node_three, E, A)

displacements, strains, stresses = Solver.solve([
    element_one,
    element_two,
    element_three
])

for key, value in displacements.items():
    print(f"Node at ({key.x()}, {key.y()}) has the displacements: x={value.x()}, y={value.y()}")

for element, strain in strains.items():
    left_node = element.left_node()
    right_node = element.right_node()
    print(f"Element from ({left_node.x()}, {left_node.y()}) to ({right_node.x()}, {right_node.y()}) has strain: {strain}, and stress: {stresses.get(element)}")
