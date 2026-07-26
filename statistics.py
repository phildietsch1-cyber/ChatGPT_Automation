"""Aggregate runtime statistics."""

def summarize(values):
    if not values:
        return {"count": 0, "min": None, "max": None, "average": None}
    return {
        "count": len(values),
        "min": min(values),
        "max": max(values),
        "average": sum(values)/len(values),
    }
