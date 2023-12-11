from typing import NamedTuple


class Race(NamedTuple):
    time: int
    distance: int


def solve(input: list[Race]):
    permutations_total = 1

    for race in input:
        strategies_total = 0
        for hold_time in range(race.time):
            race_time = race.time - hold_time
            realized_distance = race_time * hold_time
            if realized_distance > race.distance:
                strategies_total += 1
        permutations_total = permutations_total * strategies_total

    return permutations_total
