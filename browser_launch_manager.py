"""Browser launch manager."""

class BrowserLaunchManager:
    def __init__(self, browser_service, logger):
        self.browser_service=browser_service
        self.logger=logger

    def launch(self):
        ok=self.browser_service.initialize()
        if ok:
            self.logger.info("Browser service ready for launch.")
        else:
            self.logger.warning("Browser launch deferred.")
        return ok
