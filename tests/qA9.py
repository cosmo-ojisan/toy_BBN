OK_FORMAT = True

test = {
    "name": "qA9",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
>>> from tests._checker import _n
>>> _n(ans_A9_1, 0.15, 0.01)
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _n
>>> _n(ans_A9_2, 0.25, 0.01)
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _v
>>> _v(ans_A9_3, "4b68ab3847feda7d")
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _v
>>> _v(ans_A9_4, "4b68ab3847feda7d")
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
