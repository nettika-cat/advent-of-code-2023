from __future__ import annotations

import re
from copy import copy
from dataclasses import dataclass
from enum import IntEnum
from functools import cached_property


class Strength(IntEnum):
    FiveOfAKind = 6
    FourOfAKind = 5
    FullHouse = 4
    ThreeOfAKind = 3
    TwoPair = 2
    OnePair = 1
    HighCard = 0


class Card(IntEnum):
    Joker = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14

    @classmethod
    def parse(cls, symbol: str, joker_mode=False) -> Card:
        match symbol:
            case "2":
                return Card.Two
            case "3":
                return Card.Three
            case "4":
                return Card.Four
            case "5":
                return Card.Five
            case "6":
                return Card.Six
            case "7":
                return Card.Seven
            case "8":
                return Card.Eight
            case "9":
                return Card.Nine
            case "T":
                return Card.Ten
            case "J":
                return Card.Joker if joker_mode else Card.Jack
            case "Q":
                return Card.Queen
            case "K":
                return Card.King
            case "A":
                return Card.Ace
        raise ValueError(f'The symbol "{symbol}" does not correspond to a valid card.')


hand_pattern = re.compile(r"^([2-9TJQKA]{5}) (\d+)$")


@dataclass(frozen=True)
class Hand:
    cards: tuple[Card, Card, Card, Card, Card]
    bid: int

    @cached_property
    def _groups(self) -> dict[Card, int]:
        groups: dict[Card, int] = {}
        for card in self.cards:
            groups[card] = groups.get(card, 0) + 1
        return groups

    @cached_property
    def _counts(self) -> list[int]:
        groups = copy(self._groups)
        if Card.Joker in groups:
            del groups[Card.Joker]
        return list(
            reversed(
                sorted(count for count in groups.values()),
            ),
        )

    @cached_property
    def _jokers(self) -> int:
        return self._groups.get(Card.Joker, 0)

    @cached_property
    def strength(self):
        match (self._counts, self._jokers):
            case ([5], 0) | ([4], 1) | ([3], 2) | ([2], 3) | ([1], 4) | ([], 5):
                return Strength.FiveOfAKind
            case ([4, 1], 0) | ([3, 1], 1) | ([2, 1], 2) | ([1, 1], 3):
                return Strength.FourOfAKind
            case ([3, 2], 0) | ([2, 2], 1):
                return Strength.FullHouse
            case ([3, 1, 1], 0) | ([2, 1, 1], 1) | ([1, 1, 1], 2):
                return Strength.ThreeOfAKind
            case ([2, 2, 1], 0):
                return Strength.TwoPair
            case ([2, 1, 1, 1], 0) | ([1, 1, 1, 1], 1):
                return Strength.OnePair
            case _:
                return Strength.HighCard

    @classmethod
    def parse(self, hand_desc: str, joker_mode=False) -> Hand:
        match = hand_pattern.match(hand_desc)
        if not match:
            raise ValueError(f'Invalid hand description: "{hand_desc}"')
        return Hand(
            tuple(Card.parse(symbol, joker_mode) for symbol in match.group(1)),  # type: ignore
            int(match.group(2)),
        )

    def __lt__(self, other: Hand) -> bool:
        if self.strength < other.strength:
            return True
        if self.strength > other.strength:
            return False
        return self.cards < other.cards

    def __gt__(self, other: Hand) -> bool:
        if self.strength > other.strength:
            return True
        if self.strength < other.strength:
            return False
        return self.cards > other.cards

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Hand):
            return False
        if self.strength != other.strength:
            return False
        return self.cards == other.cards
