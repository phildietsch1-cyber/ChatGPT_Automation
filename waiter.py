from playwright.sync_api import Page
import time

def wait_for_response(page: Page, timeout: int = 300):
    end = time.time() + timeout
    while time.time() < end:
        # Simple placeholder: waits until send button is available again.
        try:
            page.locator('textarea').first.wait_for(state="visible", timeout=1000)
            return True
        except Exception:
            pass
    raise TimeoutError("Timed out waiting for response.")
