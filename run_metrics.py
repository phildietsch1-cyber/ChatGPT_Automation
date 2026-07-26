"""Runtime metrics helpers."""

def metrics(duration_seconds, retries, success):
    return {
        "duration_seconds": duration_seconds,
        "retries": retries,
        "success": success,
    }
