from pathlib import Path
import shutil

class PlaywrightInstallerCheck:
    @staticmethod
    def browser_binary_found():
        candidates=[
            Path.home()/".cache/ms-playwright",
            Path.home()/"AppData/Local/ms-playwright"
        ]
        return any(p.exists() for p in candidates)

    @staticmethod
    def install_hint():
        return "Run: python -m playwright install"
