OK_FORMAT = True

test = {
    "name": "qA4",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
>>> N_H, N_He = solve_NH_NHe(0.10)
>>> abs(N_He - 0.05) < 0.01 and abs(N_H - 0.80) < 0.01
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _n
>>> _n(ans_A4_2, 0.12, 0.01)
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _n
>>> _n(ans_A4_3, 0.12, 0.01)
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _v
>>> _v(ans_A4_4, "4b68ab3847feda7d")
True
""",
                    "hidden": False,
                    "locked": False,
                },
            ],
            "scored": True,
            "setup": "",
            "teardown": "",
            "type": "doctest"
        }
    ]
}
