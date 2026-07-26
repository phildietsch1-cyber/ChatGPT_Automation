"""
Configuration loader for ChatGPT Automation.
"""
from pathlib import Path
import json

DEFAULT_CONFIG = {
    "log_level": "INFO",
    "download_dir": "downloads",
    "upload_dir": "uploads",
    "archive_dir": "archive",
    "headless": False
}

class ConfigLoader:
    def __init__(self, filename="config.json"):
        self.path = Path(filename)

    def load(self):
        if not self.path.exists():
            self.path.write_text(json.dumps(DEFAULT_CONFIG, indent=2), encoding="utf-8")
            return DEFAULT_CONFIG.copy()
        return json.loads(self.path.read_text(encoding="utf-8"))
