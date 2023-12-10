from puzzle import solve_pt_1, solve_pt_2
from schematic_test import mock_input


def test_solve_pt_1():
    assert solve_pt_1(mock_input) == 4361


def test_solve_pt_2():
    assert solve_pt_2(mock_input) == 467835
