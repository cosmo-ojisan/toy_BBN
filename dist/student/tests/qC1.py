OK_FORMAT = True

test = {
    "name": "qC1",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
>>> import math
>>> abs(t_of_T(2.0, 0.8) - 0.2) < 1e-12
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> abs(t_of_T(10.0, 0.738) - 0.00738) < 1e-12
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
