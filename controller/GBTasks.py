from flask import request, Blueprint
from service.GBTaskService import GBTaskService
from service.TaskExecutionService import TaskExecutionService

gbTask = Blueprint('gbTask', __name__)


class GBTasks:

    @staticmethod
    @gbTask.route('/', methods=['POST', 'PUT', 'GET', 'DELETE'])
    def taskCRUD():
        return GBTaskService.action(request.method, request.json)


    @staticmethod
    @gbTask.route("/<string:id>", methods=['POST', 'PUT', 'GET', 'DELETE'])
    def taskCrud(id):
        return GBTaskService.action(request.method, request.json, id)



    @staticmethod
    @gbTask.route("/<string:id>/execute", methods=['POST'])
    def executeTask(id):
        return TaskExecutionService.execute(id, request.args)


    @staticmethod
    @gbTask.route("/executed", methods=['GET'])
    def getExecutedTasks():
        return TaskExecutionService.getAll()

    @staticmethod
    @gbTask.route("/executed-f", methods=['GET'])
    def getExecutedTasksFilters():
        return TaskExecutionService.getAllF(request.args)



