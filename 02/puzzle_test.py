from game import Game
from puzzle import _configuration_power, solve_pt_1, solve_pt_2

mock_input = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]


def test_solve_pt_1():
    assert solve_pt_1(mock_input) == 8


def test_solve_pt_2():
    assert solve_pt_2(mock_input) == 2286


def test_configuration_power():
    assert [
        _configuration_power(Game.parse(game_desc).minimum_configuration())
        for game_desc in mock_input
    ] == [48, 12, 1560, 630, 36]
