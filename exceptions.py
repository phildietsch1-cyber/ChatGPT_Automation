class AutomationError(Exception):
    pass

class UploadError(AutomationError):
    pass

class DownloadError(AutomationError):
    pass

class WorkflowError(AutomationError):
    pass
