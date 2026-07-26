"""Release candidate manifest."""

from dataclasses import dataclass, asdict

@dataclass
class ReleaseCandidate:
    version:str="1.0.0-rc1"
    integration_complete:bool=True
    validation_complete:bool=False
    documentation_complete:bool=False

    def summary(self):
        return asdict(self)
