from pathlib import Path

REQUIRED = [
    "controller.py","workflow.py","browser.py","config.py"
]

def validate_project(base: Path):
    missing=[f for f in REQUIRED if not (base/f).exists()]
    return {"valid": not missing, "missing": missing}
