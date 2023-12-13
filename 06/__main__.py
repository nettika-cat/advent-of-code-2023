from puzzle import Race, solve


def main():
    print("Permutations of Winning Strategies:")
    print(
        "Part 1 -",
        solve(
            [
                Race(61, 430),
                Race(67, 1036),
                Race(75, 1307),
                Race(71, 1150),
            ]
        ),
    )
    print(
        "Part 2 -",
        solve(
            [Race(61677571, 430103613071150)],
        ),
    )


if __name__ == "__main__":
    main()
