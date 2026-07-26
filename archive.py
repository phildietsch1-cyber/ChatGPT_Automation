from pathlib import Path
import shutil
from config import ARCHIVE

def archive_file(path: Path):
    dest = ARCHIVE / path.name
    shutil.copy2(path, dest)
    return dest
