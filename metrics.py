from dataclasses import dataclass

@dataclass
class Metrics:
    uploads: int = 0
    downloads: int = 0
    retries: int = 0
    successful_runs: int = 0
    failed_runs: int = 0
