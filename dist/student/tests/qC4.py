OK_FORMAT = True

test = {
    "name": "qC4",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
>>> from tests._checker import _v
>>> _v(ans_C4_1, "c4694f2e93d5c4e7")
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _v
>>> _v(ans_C4_2, "4b68ab3847feda7d")
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> # exponential_relaxation should return values in [0, 1] for Xn
>>> x_test = exponential_relaxation(0.5, 0.1, 10.0, 1.0)
>>> 0.0 <= x_test <= 1.0
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
