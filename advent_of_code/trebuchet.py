import re


number_word_map = {
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

decimal_only_pattern = re.compile("[0-9]")
left_decimal_and_words_pattern = re.compile(
    "[0-9]|" + "|".join(word for word in number_word_map.keys())
)
right_decimal_and_words_pattern = re.compile(
    "[0-9]|" + "|".join(word[::-1] for word in number_word_map.keys())
)


def _recover_calibration_value(
    line: str,
    left_symbol_pattern: re.Pattern,
    right_symbol_pattern: re.Pattern,
    symbol_map: dict[str, str],
) -> int:
    left_symbol_match = left_symbol_pattern.search(line)
    right_symbol_match = right_symbol_pattern.search(line[::-1])

    if not left_symbol_match or not right_symbol_match:
        raise ValueError(f'The calibration value of line "{line}" is unrecoverable.')

    left_symbol = left_symbol_match.group()
    right_symbol = right_symbol_match.group()[::-1]

    first_digit = symbol_map.get(left_symbol, left_symbol)
    second_digit = symbol_map.get(right_symbol, right_symbol)

    return int(first_digit + second_digit)


def _recover_all_calibration_values(
    input: str,
    left_symbol_pattern: re.Pattern,
    right_symbol_pattern: re.Pattern,
    symbol_map: dict[str, str],
) -> int:
    return sum(
        _recover_calibration_value(
            line,
            left_symbol_pattern,
            right_symbol_pattern,
            symbol_map,
        )
        for line in input.split("\n")
    )


def recover_calibration_digits_only(input: str) -> str:
    return str(
        _recover_all_calibration_values(
            input,
            decimal_only_pattern,
            decimal_only_pattern,
            {},
        )
    )


def recover_calibration_digits_and_words(input: str) -> str:
    return str(
        _recover_all_calibration_values(
            input,
            left_decimal_and_words_pattern,
            right_decimal_and_words_pattern,
            number_word_map,
        )
    )
