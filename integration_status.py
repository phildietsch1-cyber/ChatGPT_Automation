"""Integration status tracking."""

INTEGRATION_PROGRESS = {
    "architecture": 100,
    "module_scaffolding": 100,
    "integration": 25,
    "testing": 0,
    "release": 0,
}

def overall_progress():
    weights = {
        "architecture": 0.30,
        "module_scaffolding": 0.30,
        "integration": 0.25,
        "testing": 0.10,
        "release": 0.05,
    }
    return round(sum(INTEGRATION_PROGRESS[k] * w for k, w in weights.items()), 1)
