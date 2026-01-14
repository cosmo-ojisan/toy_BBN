OK_FORMAT = True

test = {
    "name": "qA10",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
>>> from tests._checker import _v
>>> _v(ans_A10_1, "c4694f2e93d5c4e7")
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _v
>>> _v(ans_A10_2, "4b68ab3847feda7d")
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _v
>>> _v(ans_A10_3, "6b23c0d5f35d1b11")
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _v
>>> _v(ans_A10_4, "4b68ab3847feda7d")
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _v
>>> _v(ans_A10_5, "559aead08264d579")
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _v
>>> _v(ans_A10_6, "df7e70e5021544f4")
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
