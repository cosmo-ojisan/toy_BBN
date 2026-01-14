OK_FORMAT = True

test = {
    "name": "qB6",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
>>> abs(Gamma_over_H(100, 10) - 10) < 0.01
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> abs(euler_step(0.5, 0.1, 1.0) - 0.6) < 0.01
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _v
>>> _v(ans_B6_4, "dfe88090c5ed7ac2")
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _v
>>> _v(ans_B6_5, "dfe88090c5ed7ac2")
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
