from pathlib import Path
from playwright.sync_api import Page

def upload_file(page: Page, file_path: Path):
    chooser = page.locator('input[type="file"]')
    chooser.set_input_files(str(file_path))
    print(f"Uploaded {file_path.name}")
