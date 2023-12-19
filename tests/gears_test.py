from advent_of_code.gears import (
    Number,
    Part,
    Schematic,
    Symbol,
    solve_part_1,
    solve_part_2,
)

mock_input = """
467..114..
...*......
..35..633.
......#...
617*......
.....+..58
..592.....
......755.
...$.*....
.664.598.3
""".strip()


def test_schematic_number_extend_digit():
    assert Number("", 1, 2).extend_digit("3") == Number("3", 1, 2)
    assert (Number("5", 3, 5).extend_digit("0").extend_digit("4")) == Number(
        "504", 3, 5
    )


def test_parse_schematic():
    assert Schematic.parse(mock_input) == Schematic(
        [
            Number("467", 0, 0),
            Number("114", 0, 5),
            Number("35", 2, 2),
            Number("633", 2, 6),
            Number("617", 4, 0),
            Number("58", 5, 8),
            Number("592", 6, 2),
            Number("755", 7, 6),
            Number("664", 9, 1),
            Number("598", 9, 5),
            Number("3", 9, 9),
        ],
        [
            Symbol("*", 1, 3),
            Symbol("#", 3, 6),
            Symbol("*", 4, 3),
            Symbol("+", 5, 5),
            Symbol("$", 8, 3),
            Symbol("*", 8, 5),
        ],
    )


def test_schematic_part_numbers():
    assert Schematic.parse(mock_input).parts() == {
        Part(
            Number("467", 0, 0),
            Symbol("*", 1, 3),
        ),
        Part(
            Number("35", 2, 2),
            Symbol("*", 1, 3),
        ),
        Part(
            Number("633", 2, 6),
            Symbol("#", 3, 6),
        ),
        Part(
            Number("617", 4, 0),
            Symbol("*", 4, 3),
        ),
        Part(
            Number("592", 6, 2),
            Symbol("+", 5, 5),
        ),
        Part(
            Number("755", 7, 6),
            Symbol("*", 8, 5),
        ),
        Part(
            Number("664", 9, 1),
            Symbol("$", 8, 3),
        ),
        Part(
            Number("598", 9, 5),
            Symbol("*", 8, 5),
        ),
    }


def test_solve_part_1():
    assert solve_part_1(mock_input) == 4361


def test_solve_part_2():
    assert solve_part_2(mock_input) == 467835
