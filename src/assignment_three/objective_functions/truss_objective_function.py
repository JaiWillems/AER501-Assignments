from src.assignment_three.api import AssignmentOneApi
from src.assignment_three.objective_functions import ObjectiveFunctionInterface


class TrussObjectiveFunction(ObjectiveFunctionInterface):

    def __init__(
            self,
            member_yield_strength: float,
            member_density: float,
            c: float,
            alpha: float
    ) -> None:
        """Objective function for the 10 Bar Truss.

        :param member_yield_strength: Member yield strength in Pa.
        :type member_yield_strength: float.
        :param member_density: Member density in kg/m^3.
        :type member_density: float.
        :param c: Penalty parameter coefficient.
        :param c: float.
        :param alpha: Penalty parameter exponent.
        :type alpha: float.
        """
        self._member_yield_strength = member_yield_strength
        self._member_density = member_density
        self._c = c
        self._alpha = alpha

    def evaluate(self, x: list, **kwargs: int) -> float:
        """Evaluate the objective function.

        :param x: Design vector.
        :type x: list.
        :param kwargs: keyword arguments, iteration 'i' is required.
        :type kwargs: dict.
        :return: Cost value.
        :rtype float:
        """

        _, _, element_stresses = AssignmentOneApi.solve_10_bar_truss(x)

        mass = self._calculate_truss_mass(element_stresses.keys())
        constraint_violation = self._calculate_stress_constraint_violation(
            element_stresses.values()
        )

        return mass + (self._c * kwargs["i"]) ** self._alpha * constraint_violation

    def _calculate_truss_mass(self, elements: list) -> float:
        volume = 0
        for element in elements:
            volume += element.cross_sectional_area() * element.length()
        return self._member_density * volume

    def _calculate_stress_constraint_violation(self, stresses: list) -> float:
        violation = 0
        for stress in stresses:
            violation += max(0, abs(stress) - self._member_yield_strength) ** 2
        return violation
