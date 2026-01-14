OK_FORMAT = True

test = {
    "name": "qC7",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
>>> "Yp" in run_student
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> 0.20 < float(run_student["Yp"]) < 0.30
True
""",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
>>> Xn = run_student["Xn"]
>>> not ((Xn <= 0.0).any() or (Xn >= 1.0).any())
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
