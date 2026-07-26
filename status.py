from dataclasses import dataclass

@dataclass
class RunStatus:
    uploaded: bool = False
    prompt_sent: bool = False
    response_complete: bool = False
    download_started: bool = False
    download_completed: bool = False
