import math

from src.assignment_one.part_a.types.vector2d import Vector2d


class PostProcessor:

    @staticmethod
    def calculate_stresses(elements: list, element_strains: dict) -> dict:
        """Calculate elemental stresses.

        :param elements: Elements to determine stresses for.
        :type elements: list.
        :param element_strains: Dictionary mapping elements to strains.
        :type element_strains: dict.
        :return: Dictionary mapping elements to stresses.
        :rtype: dict.
        """
        stress_map = {}
        for element in elements:
            stress_map[element] = element.elasticity() * element_strains.get(element)
        return stress_map

    @staticmethod
    def calculate_strains(elements: list, nodal_displacements: dict) -> dict:
        """Calculate elemental strains.

        :param elements: Elements to determine strains for.
        :type elements: list.
        :param nodal_displacements: Dictionary mapping nodes to displacements.
        :type nodal_displacements: dict.
        :return: Dictionary mapping elements to strains.
        :rtype: dict.
        """
        strain_map = {}
        for element in elements:
            strain_map[element] = PostProcessor._calculate_strain(
                element,
                nodal_displacements
            )
        return strain_map

    @staticmethod
    def _calculate_strain(element, nodal_displacements):

        if element.left_node() in nodal_displacements:
            left_displacement = nodal_displacements.get(element.left_node())
        else:
            left_displacement = Vector2d.zero()

        if element.right_node() in nodal_displacements:
            right_displacement = nodal_displacements.get(element.right_node())
        else:
            right_displacement = Vector2d.zero()

        displacements = [
            left_displacement.x(),
            left_displacement.y(),
            right_displacement.x(),
            right_displacement.y()
        ]

        incline = element.incline()
        rotation = [
            -math.cos(incline),
            -math.sin(incline),
            math.cos(incline),
            math.sin(incline)
        ]

        return sum([a * b for a, b in zip(displacements, rotation)]) / element.length()
