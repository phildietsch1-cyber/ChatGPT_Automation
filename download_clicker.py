from playwright.sync_api import Page
from selectors import DOWNLOAD_SELECTORS

def click_download(page: Page):
    for selector in DOWNLOAD_SELECTORS:
        try:
            locator = page.locator(selector).first
            if locator.count():
                locator.click()
                return True
        except Exception:
            pass
    return False
