from pathlib import Path

from puzzle import solve


def main():
    input = Path(__file__).parent.joinpath("hands.txt").read_text().strip().split("\n")
    print("Total Winnings:")
    print("Part 1 -", solve(input, False))
    print("Part 2 -", solve(input, True))


if __name__ == "__main__":
    main()
