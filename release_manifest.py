"""Release manifest generation."""

from pathlib import Path

def create_manifest(project_root):
    root = Path(project_root)
    return sorted(str(p.relative_to(root)) for p in root.rglob("*") if p.is_file())
