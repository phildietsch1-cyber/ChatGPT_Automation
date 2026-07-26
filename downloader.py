from pathlib import Path
from playwright.sync_api import Page, Download

def wait_for_download(page: Page, download_dir: Path):
    with page.expect_download(timeout=300000) as d:
        print("Waiting for download...")
    download: Download = d.value
    target = download_dir / download.suggested_filename
    download.save_as(str(target))
    print(f"Saved: {target}")
    return target
