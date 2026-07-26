"""Playwright availability checks."""

import importlib.util

class PlaywrightChecker:
    @staticmethod
    def check():
        return {
            "installed": importlib.util.find_spec("playwright") is not None
        }
