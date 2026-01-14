OK_FORMAT = True

test = {
    "name": "qC9",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
>>> from tests._checker import _v
>>> _v(ans_C9_Q1, "559aead08264d579")
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _v
>>> _v(ans_C9_Q1_detail, "559aead08264d579")
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _v
>>> _v(ans_C9_Q2, "559aead08264d579")
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _v
>>> _v(ans_C9_Q2_detail, "df7e70e5021544f4")
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _v
>>> _v(ans_C9_Q3, "559aead08264d579")
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _n
>>> _n(ans_C9_Q3_calc, 0.25, 0.01)
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _v
>>> _v(ans_C9_summary, "df7e70e5021544f4")
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
