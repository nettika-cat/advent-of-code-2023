from __future__ import annotations
from dataclasses import dataclass
import re

game_id_pattern = re.compile(r"^Game (\d+)$")
draw_yield_description_pattern = re.compile(r"(\d+) (\w+)")


@dataclass
class Game:
    id: int
    draws: list[dict[str, int]]

    @classmethod
    def parse(cls, desc: str) -> Game:
        try:
            id_segment, draws_segment = desc.split(":")
        except:
            raise ValueError("Game description is invalid.")

        # Parse game ID
        id_match = game_id_pattern.match(id_segment)
        if not id_match:
            raise ValueError("Game description is invalid.")
        id = int(id_match.group(1))

        # Parse draws
        draws = []
        for draw_desc in draws_segment.split(";"):
            draw = {}
            for yield_desc in draw_desc.split(","):
                yield_match = draw_yield_description_pattern.match(yield_desc.strip())
                if not yield_match:
                    raise ValueError("Game description is invalid.")
                yield_quantity = int(yield_match.group(1))
                yield_name = yield_match.group(2)
                draw[yield_name] = yield_quantity
            draws.append(draw)

        return Game(id, draws)

    def meets_configuration(self, bag: dict[str, int]) -> bool:
        for draw in self.draws:
            for name, quantity in draw.items():
                if quantity > bag.get(name, 0):
                    return False
        return True

    def minimum_configuration(self) -> dict[str, int]:
        config: dict[str, int] = {}
        for draw in self.draws:
            for name, quantity in draw.items():
                config[name] = max(quantity, config.get(name, 0))
        return config
