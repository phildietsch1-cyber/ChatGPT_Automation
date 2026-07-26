
"""
Browser automation wrapper for ChatGPT Automation.
Uses the user's existing Chrome profile.
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

CHATGPT_URL="https://chatgpt.com"
USER_DATA=Path.home()/"AppData/Local/Google/Chrome/User Data"
PROFILE="Default"

class Browser:
    def __init__(self, headless=False):
        self.headless=headless
        self.playwright=None
        self.browser=None
        self.page=None

    def start(self):
        self.playwright=sync_playwright().start()
        args=[
            f"--profile-directory={PROFILE}",
            "--start-maximized",
        ]
        self.browser=self.playwright.chromium.launch(
            channel="chrome",
            headless=self.headless,
            args=args,
        )
        self.page=self.browser.new_page()
        self.page.goto(CHATGPT_URL, wait_until="domcontentloaded")
        return self.page

    def wait(self):
        input("\nBrowser running. Press ENTER to close...\n")

    def stop(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
