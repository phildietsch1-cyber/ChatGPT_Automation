"""Safe uploaded-file cleanup policy."""

class SafeStorageCleanup:
    def __init__(self, keep_recent=5):
        self.keep_recent = keep_recent

    def select_for_deletion(self, uploaded_files):
        """Return oldest uploaded files excluding the newest keep_recent."""
        if len(uploaded_files) <= self.keep_recent:
            return []
        ordered = sorted(uploaded_files, key=lambda f: f.get("created_at",""))
        return ordered[:-self.keep_recent]

    def delete_in_batches(self, files, batch_size=10):
        for i in range(0, len(files), batch_size):
            yield files[i:i+batch_size]
