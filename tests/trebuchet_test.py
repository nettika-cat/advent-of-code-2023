import re

import pytest

from advent_of_code.trebuchet import (
    _recover_all_calibration_values,
    _recover_calibration_value,
    solve_part_1,
    solve_part_2,
)


def test_recover_calibration_value():
    assert (
        _recover_calibration_value(
            "..ab..cd..",
            re.compile("ab|cd"),
            re.compile("ba|dc"),
            {"ab": "1", "cd": "2"},
        )
        == 12
    )

    with pytest.raises(ValueError):
        _recover_calibration_value(
            ".",
            re.compile("ab"),
            re.compile("ba"),
            {},
        )


def test_recover_all_calibration_values():
    assert (
        _recover_all_calibration_values(
            "..ab..cd..\n..cd..ab..",
            re.compile("ab|cd"),
            re.compile("ba|dc"),
            {"ab": "1", "cd": "2"},
        )
        == 33
    )


def test_solve_part_1():
    assert (
        solve_part_1(
            "\n".join(
                [
                    "1abc2",
                    "pqr3stu8vwx",
                    "a1b2c3d4e5f",
                    "treb7uchet",
                ]
            )
        )
        == 142
    )


def test_solve_part_2():
    assert (
        solve_part_2(
            "\n".join(
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
        )
        == 281
    )
