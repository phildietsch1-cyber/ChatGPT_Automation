"""Checkpoint recovery integration."""

class CheckpointRecoveryEngine:
    def __init__(self, checkpoint_manager, workflow):
        self.checkpoint_manager=checkpoint_manager
        self.workflow=workflow

    def save(self,state):
        return self.checkpoint_manager.save(state)

    def resume(self):
        state=self.checkpoint_manager.load()
        if state:
            self.workflow.restore(state)
        return state
