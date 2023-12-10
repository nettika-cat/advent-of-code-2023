from __future__ import annotations

from dataclasses import dataclass
from typing import NamedTuple


class SchematicNumber(NamedTuple):
    number: str
    row: int
    col: int

    def extend_digit(self, digit: str) -> SchematicNumber:
        return SchematicNumber(self.number + digit, self.row, self.col)


class SchematicSymbol(NamedTuple):
    symbol: str
    row: int
    col: int


@dataclass
class Schematic:
    numbers: list[SchematicNumber]
    symbols: list[SchematicSymbol]

    @classmethod
    def parse(cls, input: str) -> Schematic:
        row = 0
        col = 0
        current_number: SchematicNumber | None = None
        numbers: list[SchematicNumber] = []
        symbols: list[SchematicSymbol] = []

        for char in input:
            match char:
                # Digit
                case n if n in "0123456789":
                    if not current_number:
                        current_number = SchematicNumber("", row, col)
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
                    symbols.append(SchematicSymbol(char, row, col))
                    col += 1

        # Finalize a number at the end of the schematic
        if current_number:
            numbers.append(current_number)

        return cls(numbers, symbols)

    def part_numbers(self) -> list[tuple[SchematicNumber, SchematicSymbol]]:
        results = []

        for number in self.numbers:
            for symbol in self.symbols:
                if (
                    # Symbol within 1 row
                    (number.row - 1 <= symbol.row <= number.row + 1)
                    and
                    # Symbol within 1 column
                    (number.col - 1 <= symbol.col <= number.col + len(number.number))
                ):
                    results.append((number, symbol))
                    break

        return results
