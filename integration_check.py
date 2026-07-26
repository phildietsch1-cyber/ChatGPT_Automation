from validator import validate_project
from pathlib import Path
from healthcheck import run_healthcheck

def run_checks():
    return {
        "project": validate_project(Path(".")),
        "health": run_healthcheck(),
    }
