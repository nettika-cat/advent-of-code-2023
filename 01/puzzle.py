import re

pt_1_first_digit_pattern = re.compile("([0-9])")
pt_1_last_digit_pattern = pt_1_first_digit_pattern
pt_1_symbol_map = {str(n): str(n) for n in range(10)}

pt_2_first_digit_pattern = re.compile(
    "([0-9]|one|two|three|four|five|six|seven|eight|nine|zero)"
)
pt_2_last_digit_pattern = re.compile(
    "([0-9]|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|orez)"
)
pt_2_symbol_map = {
    **pt_1_symbol_map,
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
}


def _solve(
    input: list[str],
    first_digit_pattern: re.Pattern,
    last_digit_pattern: re.Pattern,
    symbol_map: dict[str, str],
) -> int:
    total = 0

    for line in input:
        first_digit_match = first_digit_pattern.search(line)
        last_digit_match = last_digit_pattern.search(line[::-1])

        if not first_digit_match or not last_digit_match:
            raise ValueError(f'Line "{line}" calibration document contains no digits.')

        first_digit = symbol_map[first_digit_match.group(1)]
        last_digit = symbol_map[last_digit_match.group(1)[::-1]]

        line_calibration_number = int(first_digit + last_digit)
        total += line_calibration_number

    return total


def solve_pt_1(input: list[str]) -> int:
    return _solve(
        input,
        pt_1_first_digit_pattern,
        pt_1_first_digit_pattern,
        pt_1_symbol_map,
    )


def solve_pt_2(input: list[str]) -> int:
    return _solve(
        input,
        pt_2_first_digit_pattern,
        pt_2_last_digit_pattern,
        pt_2_symbol_map,
    )
