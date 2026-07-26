from pathlib import Path
from config import INCOMING, DOWNLOADS, ARCHIVE, LOGS

def run_healthcheck():
    return {
        "incoming_exists": INCOMING.exists(),
        "downloads_exists": DOWNLOADS.exists(),
        "archive_exists": ARCHIVE.exists(),
        "logs_exists": LOGS.exists(),
    }
