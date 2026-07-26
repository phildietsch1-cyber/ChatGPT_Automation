"""Configuration validation."""

REQUIRED_KEYS = ["browser", "download_dir", "incoming_dir"]

def validate(config):
    missing = [k for k in REQUIRED_KEYS if k not in config]
    return {"valid": not missing, "missing": missing}
