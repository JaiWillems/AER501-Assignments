import math
import numpy as np

from src.assignment_one.types.element import Element


def calculate_element_stiffness_matrix(element: Element) -> list:
    rotation_matrix = _global_coordinate_rotation(element.incline())
    stiffness_matrix = _stiffness_matrix(element.stiffness())
    return rotation_matrix.T * stiffness_matrix * rotation_matrix


def _stiffness_matrix(k: float) -> np.ndarray:
    return np.array([[k, 0, -k, 0], [0, 0, 0, 0], [-k, 0, k, 0], [0, 0, 0, 0]])


def _global_coordinate_rotation(theta: float) -> np.ndarray:
    return np.array([[(math.cos(theta)), (math.sin(theta)), 0, 0],
                     [-math.sin(theta), (math.cos(theta)), 0, 0],
                     [0, 0, (math.cos(theta)), (math.sin(theta))],
                     [0, 0, -math.sin(theta), (math.cos(theta))]])
