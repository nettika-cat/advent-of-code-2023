"Day 9: Mirage Maintenance"

Sequence = tuple[int, ...]


def parse_sequence(desc: str) -> Sequence:
    return tuple(int(num) for num in desc.split(" "))


def extrapolate_sequence(sequence: tuple[int, ...]) -> int:
    if any(sequence):
        difference_sequence = tuple(
            right - left for left, right in zip(sequence, sequence[1:])
        )
        next_difference = extrapolate_sequence(difference_sequence)
        return sequence[-1] + next_difference
    return 0


def solve_part_1(input: str) -> int:
    sequences = (parse_sequence(desc) for desc in input.split("\n"))
    return sum(extrapolate_sequence(sequence) for sequence in sequences)


def solve_part_2(input: str) -> int:
    sequences = (parse_sequence(desc) for desc in input.split("\n"))
    reversed_sequences = (tuple(reversed(sequence)) for sequence in sequences)
    return sum(extrapolate_sequence(sequence) for sequence in reversed_sequences)
