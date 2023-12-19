from textwrap import dedent

import pytest
from frozendict import frozendict

from advent_of_code.network import Instruction, Network, solve_part_1, solve_part_2

mock_network = Network(
    (
        Instruction.Left,
        Instruction.Left,
        Instruction.Right,
    ),
    frozendict(
        {
            "AAA": ("BBB", "BBB"),
            "BBB": ("AAA", "ZZZ"),
            "ZZZ": ("ZZZ", "ZZZ"),
        }
    ),
)


def test_network_parse():
    mock_input = dedent(
        """\
        LLR

        AAA = (BBB, BBB)
        BBB = (AAA, ZZZ)
        ZZZ = (ZZZ, ZZZ)
        """
    )
    assert Network.parse(mock_input) == mock_network

    assert Network.parse("LR") == Network((Instruction.Left, Instruction.Right), {})

    with pytest.raises(ValueError):
        Network.parse("invalid\nAAA = (BBB, CCC)")

    with pytest.raises(ValueError):
        Network.parse("LR\n\ninvalid")


def test_network_traverse():
    assert mock_network.traverse("AAA") == "BBB"
    assert mock_network.traverse("BBB") == "ZZZ"

    with pytest.raises(Exception):
        network = Network(
            (Instruction.Left, Instruction.Left),
            frozendict({"AAA": ("BBB", "BBB")}),
        )
        network.traverse("AAA")


def test_network_distance():
    assert mock_network.distance("AAA", "ZZZ") == 6


def test_solve_part_1():
    assert (
        solve_part_1(
            dedent(
                """\
                RL

                AAA = (BBB, AAA)
                BBB = (CCC, BBB)
                CCC = (DDD, CCC)
                DDD = (ZZZ, DDD)
                ZZZ = (ZZZ, ZZZ)
                """
            )
        )
        == 8
    )


def test_solve_part_2():
    assert (
        solve_part_2(
            dedent(
                """\
                LR

                11A = (11B, XXX)
                11B = (XXX, 11Z)
                11Z = (11B, XXX)
                22A = (22B, XXX)
                22B = (22C, 22C)
                22C = (22Z, 22Z)
                22Z = (22B, 22B)
                XXX = (XXX, XXX)
                """
            )
        )
        == 6
    )
