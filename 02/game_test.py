import pytest
from game import Game


def test_parse_games():
    assert Game.parse("Game 3: 1 red") == Game(3, [{"red": 1}])
    assert Game.parse(
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    ) == Game(
        1,
        [
            {
                "blue": 3,
                "red": 4,
            },
            {
                "red": 1,
                "green": 2,
                "blue": 6,
            },
            {
                "green": 2,
            },
        ],
    )

    with pytest.raises(ValueError):
        assert Game.parse("Game 1")

    with pytest.raises(ValueError):
        assert Game.parse(":")


def test_meets_configuration():
    bag = {"red": 5, "green": 5, "blue": 5}

    assert Game(
        1,
        [
            {"red": 3, "blue": 5},
            {"green": 2, "blue": 3},
            {"red": 4},
        ],
    ).meets_configuration(bag)

    assert not Game(
        2,
        [
            {"green": 3},
            {"red": 6, "blue": 2},
            {"blue": 2},
        ],
    ).meets_configuration(bag)

    assert not Game(
        3,
        [{"orange": 1}],
    ).meets_configuration(bag)


def test_minimum_configuration():
    assert Game(
        1,
        [
            {"red": 3, "blue": 5},
            {"green": 2, "blue": 3},
            {"red": 4},
        ],
    ).minimum_configuration() == {"red": 4, "blue": 5, "green": 2}

    assert Game(
        2,
        [
            {"red": 1},
            {"blue": 1},
            {"green": 1},
        ],
    ).minimum_configuration() == {
        "red": 1,
        "blue": 1,
        "green": 1,
    }
