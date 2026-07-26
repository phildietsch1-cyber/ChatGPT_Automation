from datetime import datetime

BUILD_TIMESTAMP = datetime.utcnow().isoformat(timespec="seconds") + "Z"
BUILD_PHASE = "Integration"
