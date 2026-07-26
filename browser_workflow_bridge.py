"""Bridge between workflow engine and browser automation."""

from workflow_engine import WorkflowEngine, Stage

class BrowserWorkflowBridge:
    def __init__(self, browser):
        self.browser = browser
        self.engine = WorkflowEngine()

    def start(self):
        self.engine.transition(Stage.PREPARE)

    def begin_upload(self):
        self.engine.transition(Stage.UPLOAD)

    def wait_for_response(self):
        self.engine.transition(Stage.WAIT_RESPONSE)

    def begin_download(self):
        self.engine.transition(Stage.DOWNLOAD)
