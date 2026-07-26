import time
from watcher import next_zip

def wait_for_batch(interval=5):
    while True:
        batch = next_zip()
        if batch:
            return batch
        time.sleep(interval)
