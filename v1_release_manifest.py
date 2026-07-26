"""Version 1.0 release manifest."""

from dataclasses import dataclass

@dataclass
class VersionManifest:
    version:str="1.0.0"
    release_status:str="ready_for_validation"
    build:int=56

    def to_dict(self):
        return self.__dict__.copy()
