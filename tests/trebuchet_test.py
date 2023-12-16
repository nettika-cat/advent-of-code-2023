import re
from advent_of_code.trebuchet import (
    recover_calibration_digits_and_words,
    recover_calibration_digits_only,
    _recover_all_calibration_values,
    _recover_calibration_value,
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


def test_recover_calibration_digits_only():
    assert (
        recover_calibration_digits_only(
            "\n".join(
                [
                    "1abc2",
                    "pqr3stu8vwx",
                    "a1b2c3d4e5f",
                    "treb7uchet",
                ]
            )
        )
        == "142"
    )


def test_recover_calibration_digits_and_words():
    assert (
        recover_calibration_digits_and_words(
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
        == "281"
    )
