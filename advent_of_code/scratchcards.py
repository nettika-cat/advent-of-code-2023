"Day 4: Scratchcards"

from __future__ import annotations

import re
from dataclasses import dataclass
from functools import cached_property


@dataclass
class Scratchcard:
    id: int
    winning_numbers: set[int]
    your_numbers: set[int]

    id_pattern = re.compile("Card +([1-9][0-9]*)")

    @staticmethod
    def _parse_id(id_segment: str) -> int:
        id_match = Scratchcard.id_pattern.match(id_segment)
        if not id_match:
            raise ValueError("Scratchcard ID is invalid")
        return int(id_match.group(1))

    @staticmethod
    def _parse_numbers(segment: str) -> set[int]:
        try:
            return {int(n) for n in segment.strip().split(" ") if n != ""}
        except:
            raise ValueError("Scratchcard number sequence is invalid.")

    @classmethod
    def parse(cls, desc: str) -> Scratchcard:
        id_segment, _, numbers_segment = desc.partition(":")
        # fmt: off
        winning_numbers_segment, _, your_numbers_segment = numbers_segment.partition("|")

        id = cls._parse_id(id_segment)
        winning_numbers = cls._parse_numbers(winning_numbers_segment)
        your_numbers = cls._parse_numbers(your_numbers_segment)

        return Scratchcard(id, winning_numbers, your_numbers)

    @staticmethod
    def resolve_copies(cards: list[Scratchcard]) -> list[int]:
        copies = [1] * len(cards)
        for i in range(len(cards)):
            for j in range(cards[i].match_count):
                copies[i + j + 1] += copies[i]
        return copies

    @cached_property
    def match_count(self):
        matching_numbers = self.winning_numbers.intersection(self.your_numbers)
        return len(matching_numbers)

    @cached_property
    def points(self):
        return 2 ** (self.match_count - 1) if self.match_count > 0 else 0


def solve_part_1(input: str) -> int:
    return sum(Scratchcard.parse(card_desc).points for card_desc in input.split("\n"))


def solve_part_2(input: str) -> int:
    cards = [Scratchcard.parse(card_desc) for card_desc in input.split("\n")]
    copies = Scratchcard.resolve_copies(cards)
    return sum(copies)
