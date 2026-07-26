"""Execution history utilities."""

from datetime import datetime

def record_run(batch, status):
    return {
        "batch": batch,
        "status": status,
        "timestamp": datetime.utcnow().isoformat(timespec="seconds") + "Z",
    }
