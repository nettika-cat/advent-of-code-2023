import pytest
from hand import Card, Hand, Strength


def test_card_parse():
    assert Card.parse("2") == Card.Two
    assert Card.parse("3") == Card.Three
    assert Card.parse("4") == Card.Four
    assert Card.parse("5") == Card.Five
    assert Card.parse("6") == Card.Six
    assert Card.parse("7") == Card.Seven
    assert Card.parse("8") == Card.Eight
    assert Card.parse("9") == Card.Nine
    assert Card.parse("T") == Card.Ten
    assert Card.parse("J") == Card.Jack
    assert Card.parse("Q") == Card.Queen
    assert Card.parse("K") == Card.King
    assert Card.parse("A") == Card.Ace

    with pytest.raises(ValueError):
        Card.parse("X")


def test_hand_parse():
    assert Hand.parse("32T3K 765") == Hand(
        (
            Card.Three,
            Card.Two,
            Card.Ten,
            Card.Three,
            Card.King,
        ),
        765,
    )
    with pytest.raises(ValueError):
        Hand.parse("invalid")


def test_hand_groups():
    assert Hand(
        (
            Card.Five,
            Card.Two,
            Card.Five,
            Card.Two,
            Card.Ace,
        ),
        0,
    )._groups == {
        Card.Five: 2,
        Card.Two: 2,
        Card.Ace: 1,
    }
    assert Hand(
        (
            Card.Two,
            Card.Eight,
            Card.Nine,
            Card.Queen,
            Card.Jack,
        ),
        0,
    )._groups == {
        Card.Two: 1,
        Card.Eight: 1,
        Card.Nine: 1,
        Card.Queen: 1,
        Card.Jack: 1,
    }


def test_hand_counts():
    assert Hand(
        (
            Card.Five,
            Card.Two,
            Card.Five,
            Card.Two,
            Card.Ace,
        ),
        0,
    )._counts == [2, 2, 1]
    assert Hand(
        (
            Card.Four,
            Card.Four,
            Card.Seven,
            Card.Four,
            Card.Seven,
        ),
        0,
    )._counts == [3, 2]
    assert Hand(
        (
            Card.Two,
            Card.Three,
            Card.Four,
            Card.Five,
            Card.Six,
        ),
        0,
    )._counts == [1, 1, 1, 1, 1]
    assert Hand(
        (
            Card.Two,
            Card.Joker,
            Card.Four,
            Card.Joker,
            Card.Six,
        ),
        0,
    )._counts == [1, 1, 1]
    assert (
        Hand(
            (
                Card.Joker,
                Card.Joker,
                Card.Joker,
                Card.Joker,
                Card.Joker,
            ),
            0,
        )._counts
        == []
    )


def test_hand_card_strength():
    assert (
        Hand(
            (Card.Ace, Card.Ace, Card.Ace, Card.Ace, Card.Ace),
            0,
        ).strength
        == Strength.FiveOfAKind
    )
    assert (
        Hand(
            (Card.Ace, Card.Ace, Card.Ace, Card.Ace, Card.Joker),
            0,
        ).strength
        == Strength.FiveOfAKind
    )
    assert (
        Hand(
            (Card.Ace, Card.Joker, Card.Ace, Card.Ace, Card.Joker),
            0,
        ).strength
        == Strength.FiveOfAKind
    )
    assert (
        Hand(
            (Card.Joker, Card.Joker, Card.Ace, Card.Ace, Card.Joker),
            0,
        ).strength
        == Strength.FiveOfAKind
    )
    assert (
        Hand(
            (Card.Joker, Card.Joker, Card.Ace, Card.Joker, Card.Joker),
            0,
        ).strength
        == Strength.FiveOfAKind
    )
    assert (
        Hand(
            (Card.Joker, Card.Joker, Card.Joker, Card.Joker, Card.Joker),
            0,
        ).strength
        == Strength.FiveOfAKind
    )
    assert (
        Hand(
            (Card.King, Card.King, Card.King, Card.King, Card.Five),
            0,
        ).strength
        == Strength.FourOfAKind
    )
    assert (
        Hand(
            (Card.King, Card.Joker, Card.King, Card.King, Card.Five),
            0,
        ).strength
        == Strength.FourOfAKind
    )
    assert (
        Hand(
            (Card.Joker, Card.Joker, Card.King, Card.King, Card.Five),
            0,
        ).strength
        == Strength.FourOfAKind
    )
    assert (
        Hand(
            (Card.Joker, Card.Joker, Card.King, Card.Joker, Card.Five),
            0,
        ).strength
        == Strength.FourOfAKind
    )
    assert (
        Hand(
            (Card.King, Card.Six, Card.King, Card.King, Card.Six),
            0,
        ).strength
        == Strength.FullHouse
    )
    assert (
        Hand(
            (Card.King, Card.Six, Card.Joker, Card.King, Card.Six),
            0,
        ).strength
        == Strength.FullHouse
    )
    assert (
        Hand(
            (Card.Ace, Card.Ace, Card.Two, Card.Five, Card.Ace),
            0,
        ).strength
        == Strength.ThreeOfAKind
    )
    assert (
        Hand(
            (Card.Joker, Card.Ace, Card.Two, Card.Five, Card.Ace),
            0,
        ).strength
        == Strength.ThreeOfAKind
    )
    assert (
        Hand(
            (Card.Joker, Card.Ace, Card.Two, Card.Five, Card.Joker),
            0,
        ).strength
        == Strength.ThreeOfAKind
    )
    assert (
        Hand(
            (Card.Five, Card.Two, Card.Five, Card.Two, Card.Ace),
            0,
        ).strength
        == Strength.TwoPair
    )
    assert (
        Hand(
            (Card.Five, Card.Two, Card.Five, Card.Nine, Card.Ace),
            0,
        ).strength
        == Strength.OnePair
    )
    assert (
        Hand(
            (Card.Five, Card.Two, Card.Joker, Card.Nine, Card.Ace),
            0,
        ).strength
        == Strength.OnePair
    )
    assert (
        Hand(
            (Card.Five, Card.Two, Card.Jack, Card.Nine, Card.Ace),
            0,
        ).strength
        == Strength.HighCard
    )


def test_hand_comparison():
    hand_a = Hand((Card.Two, Card.Three, Card.Five, Card.Eight, Card.Ace), 1)
    hand_b = Hand((Card.Ace, Card.Ace, Card.Ace, Card.Ace, Card.Ace), 1)
    assert hand_a < hand_b
    assert hand_b > hand_a
    assert hand_a == hand_a
