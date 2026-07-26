from browser import Browser
from logger import log
from workflow import run

browser = Browser()

try:
    browser.start()
    input("Open the correct ChatGPT conversation, then press ENTER...")
    result = run(browser.page)
    if result:
        log("Workflow completed successfully.")
    else:
        log("Workflow did not complete.")
    input("Press ENTER to exit...")
finally:
    browser.stop()
