import time

def retry(fn, attempts=3, delay=2):
    last=None
    for _ in range(attempts):
        try:
            return fn()
        except Exception as e:
            last=e
            time.sleep(delay)
    raise last
