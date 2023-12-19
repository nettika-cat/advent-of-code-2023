import pytest

from advent_of_code.scratchcards import Scratchcard, solve_part_1, solve_part_2

mock_inputs = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
]


def test_scratchcard_parse():
    assert Scratchcard.parse(mock_inputs[0]) == Scratchcard(
        1,
        {41, 48, 83, 86, 17},
        {83, 86, 6, 31, 17, 9, 48, 53},
    )

    with pytest.raises(ValueError):
        Scratchcard.parse("invalid")

    with pytest.raises(ValueError):
        Scratchcard.parse("Card 4: invalid | invalid")

    assert Scratchcard.parse("Card 5:") == Scratchcard(5, set(), set())
    assert Scratchcard.parse("Card 6: | ") == Scratchcard(6, set(), set())


def test_scratchcard_match_count():
    assert Scratchcard(1, {1, 2}, {3, 4}).match_count == 0
    assert Scratchcard(1, {1, 2}, {2, 3}).match_count == 1
    assert Scratchcard(1, set(), set()).match_count == 0


def test_scratchcard_points():
    card = Scratchcard(1, {41, 48, 83, 86, 17}, {83, 86, 6, 31, 17, 9, 48, 53})
    assert card.points == 8


def test_scratchcard_resolve_copies():
    cards = [Scratchcard.parse(mock_input) for mock_input in mock_inputs]
    assert Scratchcard.resolve_copies(cards) == [1, 2, 4, 8, 14, 1]


def test_solve_pt_1():
    assert solve_part_1("\n".join(mock_inputs)) == 13


def test_solve_pt_2():
    assert solve_part_2("\n".join(mock_inputs)) == 30
