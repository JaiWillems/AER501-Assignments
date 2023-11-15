

class FrameNode:

    def __init__(
            self,
            x: float,
            y: float,
            constrained: bool = False,
            harmonic_excitation_amplitude_x: float = 0,
            harmonic_excitation_amplitude_y: float = 0,
            harmonic_excitation_amplitude_m: float = 0
    ) -> None:
        """Node for a frame structure.

        :param x: X-coordinate of node.
        :param y: Y-coordinate of node.
        :param constrained: True if the node is constrained, False by default.
        :param harmonic_excitation_amplitude_x: The amplitude of a harmonic
            excitation in the x-direction, zero by default.
        :param harmonic_excitation_amplitude_y: The amplitude of a harmonic
            excitation in the y-direction, zero by default.
        :param harmonic_excitation_amplitude_x: The amplitude of a harmonic
            excitation in the moment direction, zero by default.
        """
        self._x = x
        self._y = y
        self._constrained = constrained
        self._harmonic_excitation_amplitude_x = harmonic_excitation_amplitude_x
        self._harmonic_excitation_amplitude_y = harmonic_excitation_amplitude_y
        self._harmonic_excitation_amplitude_m = harmonic_excitation_amplitude_m

    def __eq__(self, other: 'FrameNode') -> bool:
        return (
            self._x == other._x and
            self._y == other._y and
            self._constrained == other._constrained and
            self._harmonic_excitation_amplitude_x == other._harmonic_excitation_amplitude_x and
            self._harmonic_excitation_amplitude_y == other._harmonic_excitation_amplitude_y and
            self._harmonic_excitation_amplitude_m == other._harmonic_excitation_amplitude_m
        )

    def __hash__(self) -> int:
        return hash((
            self._x,
            self._y,
            self._constrained,
            self._harmonic_excitation_amplitude_x,
            self._harmonic_excitation_amplitude_y,
            self._harmonic_excitation_amplitude_m
        ))

    def x(self) -> float:
        return self._x

    def y(self) -> float:
        return self._y

    def is_constrained(self) -> bool:
        return self._constrained

    def harmonic_excitation_amplitude_x(self) -> float:
        return self._harmonic_excitation_amplitude_x

    def harmonic_excitation_amplitude_y(self) -> float:
        return self._harmonic_excitation_amplitude_y

    def harmonic_excitation_amplitude_m(self) -> float:
        return self._harmonic_excitation_amplitude_m
