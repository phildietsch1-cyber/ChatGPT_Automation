from datetime import datetime
from pathlib import Path
from version import VERSION

def save_summary(success: bool, processed: str = ""):
    out = Path("summary.txt")
    out.write_text(
        f"Version: {VERSION}\n"
        f"Time: {datetime.now()}\n"
        f"Success: {success}\n"
        f"Processed: {processed}\n",
        encoding="utf-8"
    )
    return out
