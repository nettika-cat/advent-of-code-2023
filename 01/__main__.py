from puzzle import solve_pt_1, solve_pt_2
from pathlib import Path


def main():
    input = (
        Path(__file__)
        .parent.joinpath("calibration_document.txt")
        .read_text()
        .strip()
        .split("\n")
    )
    print("Calibration Numbers:")
    print("Part 1 -", solve_pt_1(input))
    print("Part 2 -", solve_pt_2(input))


if __name__ == "__main__":
    main()
