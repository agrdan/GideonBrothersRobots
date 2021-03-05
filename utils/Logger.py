from main import app
from datetime import datetime as dt

class Logger:

    @staticmethod
    def log(message):
        app.logger.info("LOG[{}] | {}".format(dt.now(), message))