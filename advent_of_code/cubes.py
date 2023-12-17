from __future__ import annotations

import re
from collections import UserDict
from dataclasses import dataclass
from typing import ClassVar


class Configuration(UserDict[str, int]):
    color_yield_pattern: ClassVar[re.Pattern] = re.compile(r"(\d+) (\w+)")

    @staticmethod
    def _parse_color_yield(yield_desc: str) -> tuple[str, int]:
        yield_match = Configuration.color_yield_pattern.match(yield_desc.strip())
        if not yield_match:
            raise ValueError(f"Color yield is invalid: {yield_desc}")
        amount = int(yield_match.group(1))
        color = yield_match.group(2)
        return (color, amount)

    @classmethod
    def parse(cls, desc: str) -> Configuration:
        return cls(
            cls._parse_color_yield(yield_desc)
            for yield_desc in desc.split(",")
            if len(yield_desc)
        )

    @classmethod
    def parse_sequence(cls, desc: str) -> list[Configuration]:
        return [cls.parse(draw_desc) for draw_desc in desc.split(";") if len(draw_desc)]

    def power(self) -> int:
        return self.get("blue", 0) * self.get("green", 0) * self.get("red", 0)


@dataclass
class Game:
    id: int
    draws: list[Configuration]

    id_pattern: ClassVar[re.Pattern] = re.compile(r"Game (\d+)$")

    @classmethod
    def parse_table(cls, table: str) -> list[Game]:
        return [cls.parse(line) for line in table.split("\n")]

    @classmethod
    def parse(cls, desc: str) -> Game:
        id_segment, _, draws_segment = desc.partition(":")
        return cls(
            cls._parse_id(id_segment),
            Configuration.parse_sequence(draws_segment),
        )

    @staticmethod
    def _parse_id(desc: str) -> int:
        id_match = Game.id_pattern.match(desc)
        if not id_match:
            raise ValueError("Game ID is invalid.")
        return int(id_match.group(1))

    def meets_configuration(self, configuration: Configuration) -> bool:
        for draw in self.draws:
            for name, quantity in draw.items():
                if quantity > configuration.get(name, 0):
                    return False
        return True

    def minimum_configuration(self) -> Configuration:
        config = Configuration()
        for draw in self.draws:
            for name, quantity in draw.items():
                config[name] = max(quantity, config.get(name, 0))
        return config


def solve_part_1(input: str) -> str:
    actual_bag = Configuration(red=12, green=13, blue=14)
    return str(
        sum(
            game.id
            for game in Game.parse_table(input)
            if game.meets_configuration(actual_bag)
        )
    )


def solve_part_2(input: str) -> str:
    return str(
        sum(game.minimum_configuration().power() for game in Game.parse_table(input))
    )
