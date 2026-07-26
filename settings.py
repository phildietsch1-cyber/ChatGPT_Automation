from dataclasses import dataclass

@dataclass
class Settings:
    prompt: str = "Add the next batch to this project and return the updated ZIP."
    retries: int = 3
    timeout_seconds: int = 300
