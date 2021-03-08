from flask import request, Blueprint

from service.GBRobotService import GBRobotService

gbRobot = Blueprint('gbRobot', __name__)


class GBRobots:

    @staticmethod
    @gbRobot.route('/', methods=['POST', 'PUT', 'GET', 'DELETE'])
    def robotCRUD():
        return GBRobotService.action(request.method, request.json, request.headers)

    @staticmethod
    @gbRobot.route("/<string:id>", methods=['POST', 'PUT', 'GET', 'DELETE'])
    def robotCrud(id):
        return GBRobotService.action(request.method, request.json, request.headers, id)
