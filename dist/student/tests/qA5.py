OK_FORMAT = True

test = {
    "name": "qA5",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
>>> abs(remaining_fraction(2) - 0.25) < 0.01
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _n
>>> _n(ans_A5_2, 0.125, 0.01)
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _n
>>> _n(ans_A5_3, 10, 0.5)
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _v
>>> _v(ans_A5_4, "c4694f2e93d5c4e7")
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _v
>>> _v(ans_A5_5, "c4694f2e93d5c4e7")
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
