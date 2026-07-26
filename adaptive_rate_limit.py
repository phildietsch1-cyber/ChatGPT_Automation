"""Adaptive upload limit recovery."""

import re
from datetime import timedelta

DEFAULT_HOURS=2

_PATTERNS=[
    r"try again in (\d+) hour",
    r"try again in (\d+) hours",
    r"try again in (\d+) minute",
    r"try again in (\d+) minutes",
]

def parse_cooldown(message:str)->timedelta:
    m=message.lower()
    for p in _PATTERNS:
        r=re.search(p,m)
        if r:
            n=int(r.group(1))
            if "hour" in p:
                return timedelta(hours=n)
            return timedelta(minutes=n)
    return timedelta(hours=DEFAULT_HOURS)

RECOVERY_SEQUENCE=[
    "Save state",
    "Parse cooldown from message",
    "Sleep until cooldown expires",
    "Refresh ChatGPT session",
    "Verify authenticated session",
    "Resume from saved checkpoint",
    "Apply exponential backoff if still limited"
]
