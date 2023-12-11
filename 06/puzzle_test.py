from puzzle import Race, solve


def test_solve_pt_1():
    assert (
        solve(
            [
                Race(7, 9),
                Race(15, 40),
                Race(30, 200),
            ]
        )
        == 288
    )


def test_solve_pt_2():
    assert solve([Race(71530, 940200)]) == 71503
