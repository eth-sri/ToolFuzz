import logging

logging.basicConfig(level=logging.INFO)


class LoggingMixin:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def log_info(self, msg):
        self.logger.info(msg)

    def log_debug(self, msg):
        self.logger.debug(msg)

    def log_error(self, msg):
        self.logger.error(msg)
