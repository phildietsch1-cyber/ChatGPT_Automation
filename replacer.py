from pathlib import Path
import shutil

def replace_master(downloaded: Path, master: Path):
    if master.exists():
        backup = master.with_suffix(".bak.zip")
        shutil.copy2(master, backup)
    shutil.copy2(downloaded, master)
    return master
