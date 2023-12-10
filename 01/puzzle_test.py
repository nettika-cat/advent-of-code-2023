from puzzle import (pt_1_first_digit_pattern, pt_1_last_digit_pattern,
                    solve_pt_1, solve_pt_2)


def test_solve_pt_1():
    assert (
        solve_pt_1(
            [
                "1abc2",
                "pqr3stu8vwx",
                "a1b2c3d4e5f",
                "treb7uchet",
            ]
        )
        == 142
    )


def test_solve_pt_2():
    assert (
        solve_pt_2(
            [
                "two1nine",
                "eightwothree",
                "abcone2threexyz",
                "xtwone3four",
                "4nineeightseven2",
                "zoneight234",
                "7pqrstsixteen",
            ]
        )
        == 281
    )
