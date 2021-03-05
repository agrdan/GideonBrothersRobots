from main import app, api
from flask import request, Blueprint, render_template, jsonify, Response
import json
from flask_restful import Resource
from service.GBTaskService import GBTaskService


gbTask = Blueprint('gbTask', __name__)


class GBTasks:

    @staticmethod
    @gbTask.route('/', methods=['POST', 'PUT', 'GET', 'DELETE'])
    def robotCRUD():
        return GBTaskService.action(request.method, request.json)


    @staticmethod
    @gbTask.route("/<string:id>", methods=['POST', 'PUT', 'GET', 'DELETE'])
    def robotCrud(id):
        return GBTaskService.action(request.method, request.json, id)


