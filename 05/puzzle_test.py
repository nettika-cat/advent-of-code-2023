from puzzle import (RangeConversion, resolve_destination, resolve_source,
                    solve_pt_1, solve_pt_2)

mock_seeds = [79, 14, 55, 13]
mock_destinations = [81, 14, 57, 13]
mock_maps = [
    [
        RangeConversion(50, 98, 2),
        RangeConversion(52, 50, 48),
    ],
    [
        RangeConversion(0, 15, 37),
        RangeConversion(37, 52, 2),
        RangeConversion(39, 0, 15),
    ],
    [
        RangeConversion(49, 53, 8),
        RangeConversion(0, 11, 42),
        RangeConversion(42, 0, 7),
        RangeConversion(57, 7, 4),
    ],
    [
        RangeConversion(88, 18, 7),
        RangeConversion(18, 25, 70),
    ],
    [
        RangeConversion(45, 77, 23),
        RangeConversion(81, 45, 19),
        RangeConversion(68, 64, 13),
    ],
    [
        RangeConversion(0, 69, 1),
        RangeConversion(1, 0, 69),
    ],
    [
        RangeConversion(60, 56, 37),
        RangeConversion(56, 93, 4),
    ],
]


def test_range_convevrsion_resolve():
    r = mock_maps[0][0]
    assert r.resolve(97) is None
    assert r.resolve(98) == 50
    assert r.resolve(99) == 51
    assert r.resolve(100) is None


def test_range_conversion_reverse_resolve():
    r = mock_maps[0][0]
    assert r.reverse_resolve(49) is None
    assert r.reverse_resolve(50) == 98
    assert r.reverse_resolve(51) == 99
    assert r.reverse_resolve(52) is None


def test_resolve_destination():
    assert [
        resolve_destination(seed, mock_maps[0]) for seed in mock_seeds
    ] == mock_destinations


def test_resolve_source():
    assert [
        resolve_source(dest, mock_maps[0]) for dest in mock_destinations
    ] == mock_seeds


def test_solve_1():
    assert solve_pt_1(mock_seeds, mock_maps) == 35


def test_solve_2():
    assert solve_pt_2(mock_seeds, mock_maps) == 46
