"Day 3: Gear Ratios"

from __future__ import annotations

import math
from collections import UserDict
from dataclasses import dataclass
from functools import reduce
from typing import NamedTuple


class Symbol(NamedTuple):
    value: str
    row: int
    col: int


class Number(NamedTuple):
    value: str
    row: int
    col: int
    anchor: Symbol | None = None

    def extend_digit(self, digit: str) -> Number:
        return self._replace(value=self.value + digit)


class Part(NamedTuple):
    number: Number
    symbol: Symbol


@dataclass
class Schematic:
    numbers: list[Number]
    symbols: list[Symbol]

    @classmethod
    def parse(cls, input: str) -> Schematic:
        row = 0
        col = 0
        current_number: Number | None = None
        numbers: list[Number] = []
        symbols: list[Symbol] = []

        for char in input:
            match char:
                # Digit
                case n if n in "0123456789":
                    if not current_number:
                        current_number = Number("", row, col)
                    current_number = current_number.extend_digit(char)
                    col += 1

                # Blank
                case ".":
                    if current_number:
                        numbers.append(current_number)
                        current_number = None
                    col += 1

                # Newline
                case "\n":
                    if current_number:
                        numbers.append(current_number)
                        current_number = None
                    row += 1
                    col = 0

                # Schematic smybol
                case _:
                    if current_number:
                        numbers.append(current_number)
                        current_number = None
                    symbols.append(Symbol(char, row, col))
                    col += 1

        # Finalize a number at the end of the schematic
        if current_number:
            numbers.append(current_number)

        return cls(numbers, symbols)

    def parts(self) -> set[Part]:
        return {
            Part(number, symbol)
            for number in self.numbers
            for symbol in self.symbols
            if (
                # Symbol within 1 row
                (number.row - 1 <= symbol.row <= number.row + 1)
                and
                # Symbol within 1 column
                (number.col - 1 <= symbol.col <= number.col + len(number.value))
            )
        }

    def part_groups(self) -> dict[Symbol, set[Part]]:
        groups: dict[Symbol, set[Part]] = {}
        for part in self.parts():
            if part.symbol not in groups:
                groups[part.symbol] = set()
            groups[part.symbol].add(part)
        return groups


def solve_part_1(input: str) -> int:
    schematic = Schematic.parse(input)
    return sum(int(part.number.value) for part in schematic.parts())


def solve_part_2(input: str) -> int:
    schematic = Schematic.parse(input)
    return sum(
        reduce(
            lambda x, y: x * y,
            (int(part.number.value) for part in parts),
        )
        for symbol, parts in schematic.part_groups().items()
        if symbol.value == "*"
        if len(parts) == 2
    )
