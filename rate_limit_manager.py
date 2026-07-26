import time

class UploadRateLimiter:
    def __init__(self,cooldown_seconds=1800):
        self.cooldown_seconds=cooldown_seconds

    def wait(self):
        time.sleep(self.cooldown_seconds)

RECOVERY_NOTE=(
"If upload limits are reached, wait for the cooldown. "
"If uploads are still blocked, refresh the ChatGPT session "
"and then resume processing."
)
