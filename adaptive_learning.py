"""Adaptive upload-limit learning."""

from datetime import datetime

def record_upload_event(upload_count, file_size, cooldown_minutes, refreshed):
    return {
        "timestamp": datetime.utcnow().isoformat(timespec="seconds")+"Z",
        "upload_count": upload_count,
        "file_size": file_size,
        "cooldown_minutes": cooldown_minutes,
        "refresh_required": refreshed,
    }

def predict_next_pause(history):
    if not history:
        return None
    avg = sum(h["upload_count"] for h in history)/len(history)
    return int(avg*0.9)
