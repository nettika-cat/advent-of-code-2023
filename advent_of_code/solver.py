from abc import ABC, abstractmethod


class Solver(ABC):
    @abstractmethod
    def solve_part_1(self, input: str) -> None:
        pass

    @abstractmethod
    def solve_part_2(self, input: str) -> None:
        pass
