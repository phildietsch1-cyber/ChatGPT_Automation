from checkpoint_manager import create_checkpoint

class ServiceInitializer:
    def __init__(self, registry, logger):
        self.registry=registry
        self.logger=logger
    def initialize(self):
        cp=create_checkpoint('startup')
        self.registry.register('startup_checkpoint',cp)
        self.logger.info('Startup checkpoint created.')
        return cp
