from card import Card
from card_test import mock_input
from puzzle import _resolve_copies, solve_pt_1, solve_pt_2


def test_solve_pt_1():
    assert solve_pt_1(mock_input) == 13


def test_solve_pt_2():
    assert solve_pt_2(mock_input) == 30


def test_resolve_copies():
    copies = _resolve_copies([Card.parse(card_desc) for card_desc in mock_input])
    assert copies == [1, 2, 4, 8, 14, 1]
