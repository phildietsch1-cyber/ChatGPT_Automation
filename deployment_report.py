"""Deployment reporting utilities."""

from datetime import datetime

def generate(stage, success, notes=None):
    return {
        "stage": stage,
        "success": success,
        "notes": notes or [],
        "generated": datetime.utcnow().isoformat(timespec="seconds")+"Z",
    }
