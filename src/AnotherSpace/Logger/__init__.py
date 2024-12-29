import logging
import sys
import os
from datetime import datetime

class InterceptHandler(logging.Handler):
    def __init__(self, file_name=None):
        super().__init__()
        self.file_name = file_name

    def emit(self, record):
        try:
            msg = self.format(record)
            if self.file_name:
                if not os.path.exists("logs/"):
                    os.mkdir("logs/")

                with open(f"logs/{self.file_name}", 'a', encoding='utf-8') as f:
                    f.write(msg + '\n')
            else:
                stream = getattr(sys.stderr, 'buffer', sys.stderr)
                stream.write((msg + '\n').encode())
                self.flush()

        except Exception:
            self.handleError(record)


class Logger:
    def __init__(self, level=logging.INFO, file_name: str = None):
        self.level = level
        self.logger = logging.getLogger(file_name)
        self.logger.setLevel(level)
        self.handler = InterceptHandler(file_name)
        self.formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(message)s ',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)

    def add(self, level, message, *args, **kwargs):
        if len(args) > 0 or len(kwargs) > 0:
            message = message.format(*args, **kwargs)
        self.logger.log(level, message)

    def trace(self, message, *args, **kwargs):
        self.add(logging.DEBUG, message, *args, **kwargs)

    def debug(self, message, *args, **kwargs):
        self.add(logging.DEBUG, message, *args, **kwargs)

    def info(self, message, *args, **kwargs):
        self.add(logging.INFO, message, *args, **kwargs)

    def success(self, message, *args, **kwargs):
        self.add(logging.INFO, message, *args, **kwargs)

    def warning(self, message, *args, **kwargs):
        self.add(logging.WARNING, message, *args, **kwargs)

    def error(self, message, *args, **kwargs):
        self.add(logging.ERROR, message, *args, **kwargs)

    def critical(self, message, *args, **kwargs):
        self.add(logging.CRITICAL, message, *args, **kwargs)

    @staticmethod
    def catch(exc_info=None):
        exc_type, exc_value, exc_traceback = sys.exc_info() if exc_info is None else exc_info
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger = logging.getLogger('myloguru')
        logger.error(now + " | " + repr(exc_value))

    def __call__(self, *args, **kwargs):
        self.info(*args, **kwargs)


logger = Logger()