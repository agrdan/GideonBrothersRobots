from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from config.Config import Config

BASE_URL = "/gideon-brothers"
app = Flask(__name__)
config = Config()
app.config.from_object(config)
api = Api(app)
app.config["salt"] = config.salt
app.url_map.strict_slashes = False


db = SQLAlchemy(app)

from controller.GBRobots import gbRobot
app.register_blueprint(gbRobot, url_prefix="{}/robots".format(BASE_URL))

from controller.GBTasks import gbTask
app.register_blueprint(gbTask, url_prefix="{}/tasks".format(BASE_URL))

from controller.GBAuth import auth
app.register_blueprint(auth, url_prefix="{}/auth".format(BASE_URL))