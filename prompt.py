from playwright.sync_api import Page

DEFAULT_PROMPT = (
    "Add the next batch to this project and return the updated ZIP."
)

def send_prompt(page: Page, text: str = DEFAULT_PROMPT):
    box = page.locator('textarea').first
    box.wait_for(state="visible", timeout=30000)
    box.fill(text)
    box.press("Enter")
    print("Prompt sent.")
