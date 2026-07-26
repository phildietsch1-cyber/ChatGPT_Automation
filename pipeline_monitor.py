"""Pipeline monitoring helpers."""

from datetime import datetime

def snapshot(stage, active_task=None):
    return {
        "timestamp": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "stage": stage,
        "active_task": active_task,
    }
