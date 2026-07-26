from datetime import datetime
from pathlib import Path

def write_report(status:str):
    p = Path("run_report.txt")
    p.write_text(
        f"Run Status: {status}\nGenerated: {datetime.now()}\n",
        encoding="utf-8"
    )
    return p
