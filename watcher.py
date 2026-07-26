from config import INCOMING

def next_zip():
    files=sorted(INCOMING.glob("*.zip"))
    return files[0] if files else None
