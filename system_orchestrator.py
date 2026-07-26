"""System orchestrator.

Coordinates startup and shutdown of the integrated automation.
"""

class SystemOrchestrator:
    def __init__(self, controller):
        self.controller = controller

    def startup(self):
        return self.controller.initialize()

    def execute(self):
        return self.controller.run()

    def shutdown(self):
        return {"status": "clean_shutdown"}
