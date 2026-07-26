from startup import startup
from integrator import execute

def main(page):
    startup()
    return execute(page)

if __name__ == "__main__":
    print("Controller entry point initialized.")
