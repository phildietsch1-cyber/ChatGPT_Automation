"""Health reporting utilities."""

def generate_health_report(checks):
    passed = sum(1 for ok in checks.values() if ok)
    total = len(checks)
    return {
        "passed": passed,
        "total": total,
        "percent": round((passed/total)*100,1) if total else 0.0,
        "checks": checks,
    }
