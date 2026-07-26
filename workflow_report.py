from datetime import datetime

def create_report(status, steps):
    return {
        "timestamp": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "status": status,
        "steps": steps,
    }
