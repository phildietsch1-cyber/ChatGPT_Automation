"""
Browser service wrapper.
"""

from browser import Browser


class BrowserService:
    def __init__(self, logger, headless: bool = False):
        self.logger = logger
        self.headless = headless
        self.browser = None

    def initialize(self):
        try:
            self.browser = Browser(headless=self.headless)
            self.browser.start()
        except Exception as e:
            self.logger.exception("Browser initialization failed")
            print("\nBrowser initialization failed:")
            print(repr(e))
            return False

        self.logger.info("Browser service initialized.")
        return True

    def stop(self):
        if self.browser is not None:
            try:
                self.browser.stop()
            except Exception:
                self.logger.exception("Browser shutdown failed")