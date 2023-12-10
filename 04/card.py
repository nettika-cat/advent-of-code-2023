from __future__ import annotations

from dataclasses import dataclass
from functools import cached_property


@dataclass
class Card:
    winning_numbers: set[int]
    your_numbers: set[int]

    @classmethod
    def parse(cls, desc: str) -> Card:
        try:
            _, numbers_segment = desc.split(":")
            winning_numbers_segment, your_numbers_segment = numbers_segment.split("|")
            winning_numbers = {
                int(n) for n in winning_numbers_segment.strip().split(" ") if n != ""
            }
            your_numbers = {
                int(n) for n in your_numbers_segment.strip().split(" ") if n != ""
            }
        except:
            raise ValueError("Card description is invalid.")

        return Card(winning_numbers, your_numbers)

    @cached_property
    def match_count(self):
        matching_numbers = self.winning_numbers.intersection(self.your_numbers)
        return len(matching_numbers)

    @cached_property
    def points(self):
        return 2 ** (self.match_count - 1) if self.match_count > 0 else 0
