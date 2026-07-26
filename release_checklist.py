"""Release readiness checklist."""

CHECKLIST = [
    "All modules integrated",
    "Selectors validated",
    "End-to-end workflow passes",
    "Logging verified",
    "Documentation complete",
]

def pending(completed):
    return [item for item in CHECKLIST if item not in completed]
