from pathlib import Path

from almanac import maps, seeds
from puzzle import solve_pt_1, solve_pt_2


def main():
    print("Lowest Location Numbers:")
    print("Part 1 -", solve_pt_1(seeds, maps))
    print("Part 2 -", solve_pt_2(seeds, maps), " " * 30)


if __name__ == "__main__":
    main()
