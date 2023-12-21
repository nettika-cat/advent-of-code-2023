from advent_of_code.oasis import (
    extrapolate_sequence,
    parse_sequence,
    solve_part_1,
    solve_part_2,
)


def test_parse_sequencce():
    assert parse_sequence("1 2 3") == (1, 2, 3)


def test_extrapolate_sequence():
    assert extrapolate_sequence((0, 3, 6, 9, 12, 15)) == 18
    assert extrapolate_sequence((1, 3, 6, 10, 15, 21)) == 28
    assert extrapolate_sequence((10, 13, 16, 21, 30, 45)) == 68


def test_solve_part_1():
    assert (
        solve_part_1(
            "\n".join(
                [
                    "0 3 6 9 12 15",
                    "1 3 6 10 15 21",
                    "10 13 16 21 30 45",
                ]
            )
        )
        == 114
    )


def test_solve_part_2():
    assert (
        solve_part_2(
            "\n".join(
                [
                    "0 3 6 9 12 15",
                    "1 3 6 10 15 21",
                    "10 13 16 21 30 45",
                ]
            )
        )
        == 2
    )
