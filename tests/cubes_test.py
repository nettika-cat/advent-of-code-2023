import pytest

from advent_of_code.cubes import Configuration, Game, solve_part_1, solve_part_2


def test_configuration_parse():
    assert Configuration.parse("1 red") == Configuration(red=1)
    assert Configuration.parse(" 2 blue, 4 green,") == Configuration(green=4, blue=2)
    assert Configuration.parse("") == Configuration()

    with pytest.raises(ValueError):
        Configuration.parse("invalid")


def test_configuration_parse_sequence():
    assert Configuration.parse_sequence("1 red; 2 blue, 4 green;") == [
        Configuration(red=1),
        Configuration(green=4, blue=2),
    ]
    assert Configuration.parse_sequence("") == []


def test_configuration_power():
    assert Configuration(red=2, blue=3, green=5).power() == 30


def test_game_parse_table():
    assert list(Game.parse_table("Game 1: 1 red\nGame 2: 1 blue")) == [
        Game(1, [{"red": 1}]),
        Game(2, [{"blue": 1}]),
    ]


def test_game_parse():
    assert Game.parse("Game 3: 1 green") == Game(3, [Configuration(green=1)])
    assert Game.parse(
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    ) == Game(
        1,
        [
            Configuration(blue=3, red=4),
            Configuration(red=1, green=2, blue=6),
            Configuration(green=2),
        ],
    )
    assert Game.parse("Game 4:") == Game(4, [])

    with pytest.raises(ValueError):
        assert Game.parse("invalid")

    with pytest.raises(ValueError):
        assert Game.parse(":")


def test_game_meets_configuration():
    bag = Configuration(red=5, green=5, blue=5)

    assert Game(
        1,
        [
            Configuration(red=3, blue=5),
            Configuration(green=2, blue=3),
            Configuration(red=4),
        ],
    ).meets_configuration(bag)
    assert Game(3, []).meets_configuration(bag)
    assert not Game(
        2,
        [
            Configuration(green=3),
            Configuration(red=6, blue=2),
            Configuration(blue=2),
        ],
    ).meets_configuration(bag)
    assert not Game(3, [Configuration(orange=1)]).meets_configuration(bag)


def test_game_minimum_configuration():
    assert Game(
        1,
        [
            Configuration(red=3, blue=5),
            Configuration(green=2, blue=3),
            Configuration(red=4),
        ],
    ).minimum_configuration() == Configuration(red=4, blue=5, green=2)

    assert Game(
        2,
        [
            Configuration(red=1),
            Configuration(blue=1),
            Configuration(green=1),
        ],
    ).minimum_configuration() == Configuration(red=1, blue=1, green=1)


mock_input = "\n".join(
    [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]
)


def test_solve_pt_1():
    assert solve_part_1(mock_input) == 8


def test_solve_pt_2():
    assert solve_part_2(mock_input) == 2286
