from pathlib import Path
from environment import get_environment
from healthcheck import run_healthcheck
from validator import validate_project

def generate_diagnostics():
    return {
        "environment": get_environment(),
        "health": run_healthcheck(),
        "project": validate_project(Path(".")),
    }
