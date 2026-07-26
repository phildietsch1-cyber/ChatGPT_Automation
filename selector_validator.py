"""Placeholder selector validation helpers."""

REQUIRED_SELECTORS = [
    "chat_input",
    "send_button",
    "file_upload",
    "download_button",
]

def missing_selectors(selector_map):
    return [s for s in REQUIRED_SELECTORS if s not in selector_map]
