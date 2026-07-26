"""Integration planning utilities."""

INTEGRATION_STEPS = [
    "Validate Playwright selectors",
    "Wire controller to workflow",
    "Run end-to-end upload/download tests",
    "Package Version 1.0",
]

def get_plan():
    return list(INTEGRATION_STEPS)
