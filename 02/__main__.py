from pathlib import Path

from puzzle import solve_pt_1, solve_pt_2


def main():
    input = Path(__file__).parent.joinpath("games.txt").read_text().strip().split("\n")
    print("Sum of IDs of Valid Games:")
    print("Part 1 -", solve_pt_1(input))
    print("Part 2 -", solve_pt_2(input))


if __name__ == "__main__":
    main()
