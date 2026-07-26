"""
Simple service registry for dependency management.
"""


class ServiceRegistry:
    def __init__(self):
        self._services = {}

    def register(self, name, service):
        self._services[name] = service

    def get(self, name):
        return self._services.get(name)

    def list_services(self):
        return sorted(self._services.keys())


    