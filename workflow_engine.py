"""Unified workflow engine skeleton."""

from enum import Enum

class Stage(Enum):
    PREPARE="prepare"
    UPLOAD="upload"
    WAIT_RESPONSE="wait_response"
    DOWNLOAD="download"
    CHECKPOINT="checkpoint"
    RECOVERY="recovery"

class WorkflowEngine:
    def __init__(self):
        self.stage=Stage.PREPARE

    def transition(self,stage:Stage):
        self.stage=stage
        return self.stage
