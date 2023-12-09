from game import Game


def solve_pt_1(input: list[str]):
    total = 0
    for game_desc in input:
        game = Game.parse(game_desc)
        if game.meets_configuration({"red": 12, "green": 13, "blue": 14}):
            total += game.id
    return total


def solve_pt_2(input: list[str]):
    total = 0
    for game_desc in input:
        game = Game.parse(game_desc)
        total += _configuration_power(game.minimum_configuration())
    return total


def _configuration_power(bag: dict[str, int]) -> int:
    return bag.get("blue", 0) * bag.get("green", 0) * bag.get("red", 0)
