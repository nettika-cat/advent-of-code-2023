from card import Card


def solve_pt_1(input: list[str]):
    total = 0

    for card_desc in input:
        card = Card.parse(card_desc)
        total += card.points

    return total


def solve_pt_2(input: list[str]):
    cards = [Card.parse(card_desc) for card_desc in input]
    copies = _resolve_copies(cards)

    total = 0
    for copy in copies:
        total += copy

    return total


def _resolve_copies(cards: list[Card]) -> list[int]:
    copies = [1] * len(cards)
    for i in range(len(cards)):
        for j in range(cards[i].match_count):
            copies[i + j + 1] += copies[i]
    return copies
