OK_FORMAT = True

test = {
    "name": "qC8",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
>>> from tests._checker import _v
>>> _v(ans_C8_1, "df7e70e5021544f4")
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _v
>>> _v(ans_C8_2, "559aead08264d579")
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _v
>>> _v(ans_C8_3, "559aead08264d579")
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
