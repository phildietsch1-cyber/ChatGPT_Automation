from pathlib import Path
from workflow import run
from replacer import replace_master
from config import DOWNLOADS

def process(page, master_zip: Path):
    downloaded = run(page)
    if downloaded:
        replace_master(downloaded, master_zip)
        return downloaded
    return None
