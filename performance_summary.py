"""Performance summary utilities."""

def summarize(total_runs, successful_runs, avg_duration):
    success_rate = (successful_runs / total_runs * 100) if total_runs else 0.0
    return {
        "total_runs": total_runs,
        "successful_runs": successful_runs,
        "success_rate": round(success_rate, 2),
        "average_duration_seconds": avg_duration,
    }
