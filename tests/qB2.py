OK_FORMAT = True

test = {
    "name": "qB2",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
>>> from tests._checker import _v
>>> _v(str(ans_B2_2).upper(), "dfe88090c5ed7ac2")
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _v
>>> _v(str(ans_B2_3).upper(), "dfe88090c5ed7ac2")
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _v
>>> _v(str(ans_B2_4).upper(), "4e523a5ae5b4636c")
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
