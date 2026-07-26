"""Artifact catalog utilities."""

from pathlib import Path

def catalog(directory):
    directory = Path(directory)
    return sorted(
        {"name": p.name, "size": p.stat().st_size}
        for p in directory.glob("*") if p.is_file()
    )
