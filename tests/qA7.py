OK_FORMAT = True

test = {
    "name": "qA7",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
>>> from tests._checker import _n
>>> _n(ans_A7_1, 10, 0.1)
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _v
>>> _v(ans_A7_2, "559aead08264d579")
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _n
>>> _n(ans_A7_3, 0.02, 0.005)
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _v
>>> _v(ans_A7_4, "4b68ab3847feda7d")
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
