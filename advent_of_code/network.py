"Day 8: Haunted Wasteland"

from __future__ import annotations

import re
from dataclasses import dataclass
from enum import Enum
from functools import cache
from math import lcm
from typing import ClassVar, NamedTuple

from frozendict import frozendict


class Instruction(Enum):
    Left = "L"
    Right = "R"


@dataclass(frozen=True)
class Network:
    instructions: tuple[Instruction, ...]
    nodes: frozendict[str, tuple[str, str]]

    node_pattern: ClassVar[re.Pattern] = re.compile(
        r"([0-9A-Z]{3}) = \(([0-9A-Z]{3}), ([0-9A-Z]{3})\)$"
    )

    @staticmethod
    def _parse_instructions(instructions_segment: str) -> tuple[Instruction, ...]:
        try:
            return tuple(Instruction(symbol) for symbol in instructions_segment)
        except:
            raise ValueError("Network instructions are invalid")

    @staticmethod
    def _parse_node(node_desc) -> tuple[str, tuple[str, str]]:
        node_match = Network.node_pattern.match(node_desc)
        if not node_match:
            raise ValueError("Network node description is invalid")
        return (
            node_match.group(1),
            (
                node_match.group(2),
                node_match.group(3),
            ),
        )

    @classmethod
    def parse(cls, network_desc: str) -> Network:
        instructions_segment, _, node_desc_segment = network_desc.partition("\n\n")

        instructions = cls._parse_instructions(instructions_segment)
        nodes = frozendict(
            cls._parse_node(node_desc)
            for node_desc in node_desc_segment.split("\n")
            if node_desc != ""
        )

        return Network(instructions, nodes)

    @cache
    def traverse(self, start_node: str) -> str:
        cursor = start_node
        for instruction in self.instructions:
            if cursor not in self.nodes:
                raise Exception(f"Dead end: node {cursor} not found")
            left, right = self.nodes[cursor]
            match instruction:
                case Instruction.Left:
                    cursor = left
                case Instruction.Right:
                    cursor = right
        return cursor

    @cache
    def distance(self, start_node: str, stop_flag: str) -> int:
        cursor = start_node
        cycles = 0
        while not cursor.endswith(stop_flag):
            cursor = self.traverse(cursor)
            cycles += 1
        return cycles * len(self.instructions)

    @cache
    def linked_distance(self, start_flag: str, stop_flag: str) -> int:
        return lcm(
            *(
                self.distance(node, stop_flag)
                for node in self.nodes.keys()
                if node.endswith(start_flag)
            )
        )


def solve_part_1(input: str) -> int:
    network = Network.parse(input)
    return network.distance("AAA", "ZZZ")


def solve_part_2(input: str) -> int:
    network = Network.parse(input)
    return network.linked_distance("A", "Z")
