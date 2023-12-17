"My solutions to Advent of Code 2023"

__author__ = "Nettika <nettika@leaf.ninja>"
__version__ = "1.0.0"

from typing import Callable

from advent_of_code import cubes, trebuchet

Solver = Callable[[str], str]


solvers: dict[int, tuple[Solver, Solver]] = {
    1: (trebuchet.solve_part_1, trebuchet.solve_part_2),
    2: (cubes.solve_part_1, cubes.solve_part_2),
}
