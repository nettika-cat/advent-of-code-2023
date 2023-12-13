from hand import Hand


def solve(hand_descs: list[str], joker_mode=False):
    hands = sorted(Hand.parse(hand_desc, joker_mode) for hand_desc in hand_descs)
    return sum((index + 1) * hand.bid for index, hand in enumerate(hands))
