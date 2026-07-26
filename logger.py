from pathlib import Path
from datetime import datetime
from config import LOGS

LOG_FILE = LOGS / "automation.log"

def log(message:str):
    stamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with LOG_FILE.open("a",encoding="utf-8") as f:
        f.write(f"[{stamp}] {message}\n")
    print(message)
