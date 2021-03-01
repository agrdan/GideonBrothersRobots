from flask import Flask
from config.Config import Config
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt
from flask_restplus import Api

app = Flask(__name__)
config = Config()
app.config.from_object(config)
api = Api(app=app)
ns = api.namespace('main', description='Main APIs')

db = SQLAlchemy(app)

from controller.GBRobots import gbRobot
app.register_blueprint(gbRobot, url_prefix="/gideon-brothers")

