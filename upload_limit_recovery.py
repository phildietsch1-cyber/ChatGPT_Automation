"""Upload limit detection and recovery policy."""

DEFAULT_COOLDOWN_HOURS = 2

UPLOAD_LIMIT_MESSAGES = [
    "try again in 2 hours",
    "upload limit reached",
    "maximum uploads",
]

def recovery_policy():
    return {
        "cooldown_hours": DEFAULT_COOLDOWN_HOURS,
        "actions": [
            "Save workflow state",
            "Pause processing",
            "Wait for cooldown",
            "Refresh ChatGPT session",
            "Verify login",
            "Resume from last completed batch"
        ]
    }
