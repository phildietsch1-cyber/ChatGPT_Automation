from pathlib import Path

def build_manifest(base: Path):
    return sorted(str(p.relative_to(base)) for p in base.rglob("*") if p.is_file())
