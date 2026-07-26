"""Archive indexing helpers."""

from pathlib import Path

def build_index(folder):
    folder = Path(folder)
    return sorted(p.name for p in folder.glob("*.zip"))
