from puzzle import solve

mock_hand_descriptions = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483",
]


def test_solve():
    assert solve(mock_hand_descriptions, False) == 6440
    assert solve(mock_hand_descriptions, True) == 5905
