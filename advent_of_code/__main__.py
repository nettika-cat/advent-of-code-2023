import time
from argparse import ArgumentParser

import requests

from advent_of_code import __version__
from advent_of_code.solver import Solver

solvers: dict[int, Solver] = {}


def main():
    # Parse CLI arguments
    parser = ArgumentParser(prog="Advent of Code 2023 Solver")
    parser.add_argument(
        "--session",
        "-s",
        required=True,
        help="Session token",
    )
    parser.add_argument(
        "--day",
        "-d",
        required=True,
        type=int,
        help="Day of the month to solve",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    args = parser.parse_args()

    # Validate day number
    if args.day > 30 or args.day < 0:
        print("Invalid day number")
        exit(1)

    # Fetch input for the day
    print(f"Fetching Day {args.day} Input...")
    with requests.get(
        f"https://adventofcode.com/2023/day/{args.day}/input",
        cookies={"session": args.session},
    ) as response:
        if not response.ok:
            print("Unable to fetch input. Check your session token.")
            exit(1)
        input = response.text.strip()

    # Resolve solver
    solver = solvers.get(args.day)
    if not solver:
        print(f"No solver for day {args.day}")
        exit(1)

    # Execute solvers
    print(f"Solving day {args.day}'s puzzle")
    start = time.time()
    print("Part 1 -", solver.solve_part_1(input))
    print("Part 2 -", solver.solve_part_2(input))
    end = time.time()
    print(f"Solved in {end-start:,} seconds.")


if __name__ == "__main__":
    main()
