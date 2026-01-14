OK_FORMAT = True

test = {
    "name": "qA6",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
>>> abs(float(t_ratio) - 100) < 1
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> abs(float(Gamma_ratio) - 0.00001) < 0.000001
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _n
>>> _n(ans_A6_3, 0.5, 0.01)
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _n
>>> _n(ans_A6_4, 0.1, 0.01)
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _n
>>> _n(ans_A6_5, 10, 0.1)
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
