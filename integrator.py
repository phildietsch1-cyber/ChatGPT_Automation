from startup import startup
from workflow import run

def execute(page):
    startup()
    return run(page)
