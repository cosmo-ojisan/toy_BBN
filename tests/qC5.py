OK_FORMAT = True

test = {
    "name": "qC5",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
>>> x1 = step_Xn(0.4, 10.0, 9.0)
>>> 0.0 <= x1 <= 1.0
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
