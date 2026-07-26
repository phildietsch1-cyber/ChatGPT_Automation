"""Live testing plan for Version 1.0."""

TEST_PHASES = [
    "Launch browser",
    "Upload master ZIP",
    "Submit prompt",
    "Wait for completion",
    "Download updated ZIP",
    "Verify archive integrity",
]

def get_test_plan():
    return TEST_PHASES.copy()
