from datetime import date
import datetime
from datetime import datetime as dt
from flask import Response
import json
from utils.Logger import Logger


class Utils:

    @staticmethod
    def parseStringDtToDate(string_date):
        try:
            date_formate = datetime.datetime.strptime(string_date, '%Y-%m-%d')
            parsedDate = date_formate.strftime("%Y-%m-%d")
            return parsedDate
        except Exception as e:
            Logger.info(e)

    @staticmethod
    def parseTimestamp(timestamp):
        date = dt.fromtimestamp(int(timestamp))
        parsedDate = date.strftime("%Y-%m-%d")
        return parsedDate


    @staticmethod
    def JsonResponse(dto, code):
        return Response(json.dumps(dto), status=code, mimetype='application/json')


    @staticmethod
    def JsonMessage(message, code):
        response = {
            'message': message
        }
        return Response(json.dumps(response), status=code, mimetype='application/json')

    @staticmethod
    def validate_json_list(model, *keys: str):
        for k in keys:
            if not hasattr(model, k):
                return False

        return True

    @staticmethod
    def validate_json(model, key):
        if not hasattr(model, key):
            return False
        return True

    @staticmethod # both params need to be generated or extended by JSONSerializator
    def check_object_propertis(objectProperties, jsonProperties):
        return all(elem in objectProperties.getKeyList() for elem in jsonProperties.getKeyList())