from zipfile import ZipFile

def verify_zip(path):
    with ZipFile(path) as z:
        bad = z.testzip()
    return {"valid": bad is None, "first_error": bad}
