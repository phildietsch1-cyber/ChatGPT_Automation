from pathlib import Path

BASE = Path(__file__).parent

INCOMING = BASE / "Incoming"
DOWNLOADS = BASE / "Downloads"
ARCHIVE = BASE / "Archive"
LOGS = BASE / "Logs"

for folder in (INCOMING, DOWNLOADS, ARCHIVE, LOGS):
    folder.mkdir(exist_ok=True)

CHATGPT_URL = "https://chatgpt.com"
