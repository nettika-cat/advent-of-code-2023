from advent_of_code.gears import (
    Schematic,
    SchematicNumber,
    SchematicSymbol,
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
    assert SchematicNumber("", 1, 2).extend_digit("3") == SchematicNumber("3", 1, 2)
    assert (
        SchematicNumber("5", 3, 5).extend_digit("0").extend_digit("4")
    ) == SchematicNumber("504", 3, 5)


def test_parse_schematic():
    assert Schematic.parse(mock_input) == Schematic(
        [
            SchematicNumber("467", 0, 0),
            SchematicNumber("114", 0, 5),
            SchematicNumber("35", 2, 2),
            SchematicNumber("633", 2, 6),
            SchematicNumber("617", 4, 0),
            SchematicNumber("58", 5, 8),
            SchematicNumber("592", 6, 2),
            SchematicNumber("755", 7, 6),
            SchematicNumber("664", 9, 1),
            SchematicNumber("598", 9, 5),
            SchematicNumber("3", 9, 9),
        ],
        [
            SchematicSymbol("*", 1, 3),
            SchematicSymbol("#", 3, 6),
            SchematicSymbol("*", 4, 3),
            SchematicSymbol("+", 5, 5),
            SchematicSymbol("$", 8, 3),
            SchematicSymbol("*", 8, 5),
        ],
    )


def test_schematic_part_numbers():
    assert Schematic.parse(mock_input).part_numbers() == [
        (
            SchematicNumber("467", 0, 0),
            SchematicSymbol("*", 1, 3),
        ),
        (
            SchematicNumber("35", 2, 2),
            SchematicSymbol("*", 1, 3),
        ),
        (
            SchematicNumber("633", 2, 6),
            SchematicSymbol("#", 3, 6),
        ),
        (
            SchematicNumber("617", 4, 0),
            SchematicSymbol("*", 4, 3),
        ),
        (
            SchematicNumber("592", 6, 2),
            SchematicSymbol("+", 5, 5),
        ),
        (
            SchematicNumber("755", 7, 6),
            SchematicSymbol("*", 8, 5),
        ),
        (
            SchematicNumber("664", 9, 1),
            SchematicSymbol("$", 8, 3),
        ),
        (
            SchematicNumber("598", 9, 5),
            SchematicSymbol("*", 8, 5),
        ),
    ]


def test_solve_part_1():
    assert solve_part_1(mock_input) == 4361


def test_solve_part_2():
    assert solve_part_2(mock_input) == 467835
