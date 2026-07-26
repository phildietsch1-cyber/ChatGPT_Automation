"""Checkpoint management helpers."""

from datetime import datetime

def create_checkpoint(name, metadata=None):
    return {
        "name": name,
        "created": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "metadata": metadata or {},
    }
