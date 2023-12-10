from schematic import Schematic, SchematicNumber, SchematicSymbol


def solve_pt_1(input: str) -> int:
    schematic = Schematic.parse(input)

    total = 0
    for part_number, _ in schematic.part_numbers():
        total += int(part_number.number)

    return total


def solve_pt_2(input: str) -> int:
    schematic = Schematic.parse(input)

    part_groups: dict[SchematicSymbol, list[SchematicNumber]] = {}

    for part_number, part_symbol in schematic.part_numbers():
        if part_symbol.symbol != "*":
            continue
        if part_symbol not in part_groups:
            part_groups[part_symbol] = []
        part_groups[part_symbol].append(part_number)

    gears = [
        part_numbers for part_numbers in part_groups.values() if len(part_numbers) == 2
    ]

    total = 0
    for gear_1, gear_2 in gears:
        gear_ratio = int(gear_1.number) * int(gear_2.number)
        total += gear_ratio

    return total
