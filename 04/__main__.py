from pathlib import Path

from puzzle import solve_pt_1, solve_pt_2


def main():
    input = Path(__file__).parent.joinpath("cards.txt").read_text().strip().split("\n")
    print("Total Points of Scratchcards -", solve_pt_1(input))
    print("Total Scratchcard Copies -", solve_pt_2(input))


if __name__ == "__main__":
    main()
