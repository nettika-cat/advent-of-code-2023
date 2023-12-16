"My solutions to Advent of Code 2023"

__author__ = "Nettika <nettika@leaf.ninja>"
__version__ = "1.0.0"

from typing import Callable
from advent_of_code.trebuchet import (
    recover_calibration_digits_and_words,
    recover_calibration_digits_only,
)

Solver = Callable[[str], str]


solvers: dict[int, tuple[Solver, Solver]] = {
    1: (recover_calibration_digits_only, recover_calibration_digits_and_words),
}
