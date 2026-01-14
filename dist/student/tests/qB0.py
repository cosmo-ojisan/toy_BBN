OK_FORMAT = True

test = {
    "name": "qB0",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
>>> abs(kT_eV(1e8) - 8617) < 10
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> from tests._checker import _n
>>> _n(ans_B0_3, 10, 0.1)
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> abs(float(ans_B0_4) - 1e8) < 1e6
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
