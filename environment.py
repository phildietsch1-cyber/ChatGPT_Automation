import platform
import sys

def get_environment():
    return {
        "python": sys.version.split()[0],
        "platform": platform.platform(),
    }
