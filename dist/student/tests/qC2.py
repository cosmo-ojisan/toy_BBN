OK_FORMAT = True

test = {
    "name": "qC2",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
>>> abs(Gamma_of_T(2.0, 3.0) - 96.0) < 1e-12
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
