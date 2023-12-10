from pathlib import Path

from puzzle import solve_pt_1, solve_pt_2


def main():
    input = Path(__file__).parent.joinpath("schematic.txt").read_text().strip()
    print("Sum of Part Numbers:")
    print("Part 1 -", solve_pt_1(input))
    print("Part 2 -", solve_pt_2(input))


if __name__ == "__main__":
    main()
