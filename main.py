from flask import Flask
from config.Config import Config
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt
from flask_restful import Api

BASE_URL = "/gideon-brothers"
app = Flask(__name__)
config = Config()
app.config.from_object(config)
api = Api(app)

db = SQLAlchemy(app)

from controller.GBRobots import gbRobot
app.register_blueprint(gbRobot, url_prefix="{}/robots".format(BASE_URL))

from controller.GBTasks import gbTask
app.register_blueprint(gbTask, url_prefix="{}/tasks".format(BASE_URL))

