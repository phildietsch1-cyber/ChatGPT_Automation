"""Execution queue helpers."""

from collections import deque

class ExecutionQueue:
    def __init__(self):
        self._queue = deque()

    def add(self, item):
        self._queue.append(item)

    def next(self):
        return self._queue.popleft() if self._queue else None

    def size(self):
        return len(self._queue)
