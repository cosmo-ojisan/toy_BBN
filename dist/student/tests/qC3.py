OK_FORMAT = True

test = {
    "name": "qC3",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
>>> import math
>>> x = Xn_eq(1.0, Q=1.293)
>>> 0.0 < x < 0.5
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
