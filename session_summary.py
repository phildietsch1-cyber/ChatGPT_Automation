"""Session summary utilities."""

from datetime import datetime

def summarize(session_id, processed_batches):
    return {
        "session_id": session_id,
        "processed_batches": processed_batches,
        "generated": datetime.utcnow().isoformat(timespec="seconds") + "Z",
    }
