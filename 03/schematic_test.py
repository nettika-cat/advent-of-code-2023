from schematic import Schematic, SchematicNumber, SchematicSymbol

mock_input = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".strip()


def test_schematic_number_extend_digit():
    sn = SchematicNumber("", 1, 2)
    assert sn.number == ""
    sn = sn.extend_digit("3")
    assert sn.number == "3"
    sn = sn.extend_digit("5")
    assert sn.number == "35"
    sn = sn.extend_digit("1")
    assert sn.number == "351"


def test_parse_schematic():
    assert Schematic.parse(mock_input) == Schematic(
        [
            SchematicNumber("467", 0, 0),
            SchematicNumber("114", 0, 5),
            SchematicNumber("35", 2, 2),
            SchematicNumber("633", 2, 6),
            SchematicNumber("617", 4, 0),
            SchematicNumber("58", 5, 7),
            SchematicNumber("592", 6, 2),
            SchematicNumber("755", 7, 6),
            SchematicNumber("664", 9, 1),
            SchematicNumber("598", 9, 5),
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
