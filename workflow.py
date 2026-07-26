from pathlib import Path
from logger import log
from watcher import next_zip
from uploader import upload_file
from prompt import send_prompt
from waiter import wait_for_response
from download_clicker import click_download
from downloader import wait_for_download
from archive import archive_file
from config import DOWNLOADS

def run(page):
    batch = next_zip()
    if not batch:
        log("No ZIP files found.")
        return None

    log(f"Uploading {batch.name}")
    upload_file(page, batch)

    send_prompt(page)
    wait_for_response(page)

    if click_download(page):
        downloaded = wait_for_download(page, DOWNLOADS)
        archive_file(batch)
        log(f"Downloaded: {downloaded.name}")
        return downloaded

    log("Download button not found.")
    return None
