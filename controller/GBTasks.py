from flask import request, Blueprint, Response

from service.GBTaskService import GBTaskService
from service.TaskExecutionService import TaskExecutionService

gbTask = Blueprint('gbTask', __name__)


class GBTasks:

    @staticmethod
    @gbTask.route('/', methods=['POST', 'PUT', 'GET', 'DELETE'])
    def taskCRUD():
        return GBTaskService.action(request.method, request.json, request.headers)


    @staticmethod
    @gbTask.route("/<string:id>", methods=['POST', 'PUT', 'GET', 'DELETE'])
    def taskCrud(id):
        return GBTaskService.action(request.method, request.json, request.headers, id)



    @staticmethod
    @gbTask.route("/<string:id>/execute", methods=['POST'])
    def executeTask(id):
        return TaskExecutionService.execute(id, request.args, request.headers)


    @staticmethod
    @gbTask.route("/executed", methods=['GET'])
    def getExecutedTasks():
        return TaskExecutionService.getAll(request.headers)

    @staticmethod
    @gbTask.route("/executed-f", methods=['GET'])
    def getExecutedTasksFilters():
        return TaskExecutionService.getAllF(request.args, request.headers)


    @staticmethod
    @gbTask.route("/executed-f/csv", methods=['GET'])
    def getExecutedTasksFiltersCSV():
        csv = TaskExecutionService.getAllF(request.args, request.headers, exportCsv=True)
        return Response(
                csv,
                mimetype="text/csv",
                headers={"Content-disposition":
                             "attachment; filename=filtered_tasks.csv"})