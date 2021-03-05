from main import app, api
from flask import request, Blueprint, render_template, jsonify, Response
import json
from flask_restful import Resource
from service.GBRobotService import GBRobotService


gbRobot = Blueprint('gbRobot', __name__)



class GBRobots:

    @staticmethod
    @gbRobot.route('/', methods=['POST', 'PUT', 'GET', 'DELETE'])
    def robotCRUD():
        return GBRobotService.action(request.method, request.json)


    @staticmethod
    @gbRobot.route("/<string:id>", methods=['POST', 'PUT', 'GET', 'DELETE'])
    def robotCrud(id):
        return GBRobotService.action(request.method, request.json, id)


