"""Progress tracking utilities."""

def calculate_progress(completed, total):
    if total <= 0:
        return 0.0
    return round((completed / total) * 100.0, 1)
