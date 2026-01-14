OK_FORMAT = True

test = {
    "name": "qB5",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
>>> abs(t_of_T_B5(2.0, 0.738) - 0.1845) < 0.01
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> abs(Gamma_of_T_B5(2.0, 3.0) - 96.0) < 0.1
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _v
>>> _v(ans_B5_3, "dfe88090c5ed7ac2")
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _v
>>> _v(ans_B5_4, "dfe88090c5ed7ac2")
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
