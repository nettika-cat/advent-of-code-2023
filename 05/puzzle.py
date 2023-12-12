from itertools import count
from math import inf
from typing import Iterable, NamedTuple


class RangeConversion(NamedTuple):
    destination_start: int
    source_start: int
    range_length: int

    def resolve(self, source: int) -> int | None:
        if self.source_start <= source < self.source_start + self.range_length:
            return self.destination_start + source - self.source_start
        return None

    def reverse_resolve(self, destination: int) -> int | None:
        if (
            self.destination_start
            <= destination
            < self.destination_start + self.range_length
        ):
            return self.source_start + destination - self.destination_start
        return None


class SeedRange(NamedTuple):
    start: int
    length: int

    def includes(self, seed: int):
        return self.start <= seed < self.start + self.length


def resolve_destination(source: int, map: list[RangeConversion]) -> int:
    for range_conversion in map:
        if destination := range_conversion.resolve(source):
            return destination
    return source


def resolve_source(destination: int, map: list[RangeConversion]) -> int:
    for range_conversion in map:
        if source := range_conversion.reverse_resolve(destination):
            return source
    return destination


def solve_pt_1(seeds: list[int], maps: list[list[RangeConversion]]) -> int:
    minimum_location = 9_999_999_999_999
    for seed in seeds:
        result = seed
        for map in maps:
            result = resolve_destination(result, map)
        minimum_location = min(minimum_location, result)
    return minimum_location


def solve_pt_2(seeds: list[int], maps: list[list[RangeConversion]]) -> int:
    seed_ranges = [
        SeedRange(start, length) for start, length in zip(seeds[::2], seeds[1::2])
    ]

    for location in count():
        if location % 100_000 == 0:
            print(
                f"Part 2 - [checking {location:,} through {location + 99_999:,}]",
                end="\r",
            )

        result = location
        for map in reversed(maps):
            result = resolve_source(result, map)

        seed_candidate = result
        for map in maps:
            result = resolve_destination(result, map)

        for seed_range in seed_ranges:
            if seed_range.includes(seed_candidate):
                return location

    raise NotImplementedError()
