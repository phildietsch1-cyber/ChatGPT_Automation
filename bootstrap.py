from integration_check import run_checks

def bootstrap():
    results = run_checks()
    if not results["project"]["valid"]:
        raise RuntimeError("Project validation failed.")
    return results
