"""Recovery management utilities."""

from datetime import datetime

def create_recovery_point(reason, state=None):
    return {
        "reason": reason,
        "state": state or {},
        "timestamp": datetime.utcnow().isoformat(timespec="seconds") + "Z",
    }
