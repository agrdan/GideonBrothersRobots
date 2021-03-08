from main import app
from datetime import datetime as dt
import logging

logging.basicConfig(filename='output.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

class Logger:

    @staticmethod
    def info(message):
        app.logger.info("LOG[{}] | {}".format(dt.now(), message))