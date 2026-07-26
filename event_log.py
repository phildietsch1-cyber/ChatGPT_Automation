"""Structured event logging."""

from datetime import datetime

def create_event(event_type, message):
    return {
        "timestamp": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "type": event_type,
        "message": message,
    }
