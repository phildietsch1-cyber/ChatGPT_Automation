"""Historical scheduler optimization."""

from statistics import mean

def recommended_pause(upload_events):
    """Return recommended proactive pause threshold."""
    if not upload_events:
        return None
    uploads = [e["upload_count"] for e in upload_events if "upload_count" in e]
    if not uploads:
        return None
    return max(1, int(mean(uploads) * 0.9))

def recommended_cooldown(upload_events):
    cooldowns = [e["cooldown_minutes"] for e in upload_events if "cooldown_minutes" in e]
    if not cooldowns:
        return 120
    return int(mean(cooldowns))
