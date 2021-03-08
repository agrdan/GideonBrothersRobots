from datasource.entity.TaskEntity import Task
from datasource.entity.TaskType import TaskType
from datasource.dto.response.SimpleTaskResponse import SimpleTaskResponseDto
from datasource.dto.request.TaskRequestDto import TaskRequestDto
from service.GenericHelperService import GenericHelperService
from datetime import datetime as dt
from utils.DBUtil import DBUtil
from utils.Utils import Utils
from utils.JSONSerializator import JSONSerializator
from service.GBLoginService import LoginService


AUTH_TOKEN = 'Auth-Token'

class GBTaskService:

    def __init__(self):
        pass

    @staticmethod
    def action(method, modelDto, header, id=None):

        token = None
        try:
            token = header.get(AUTH_TOKEN)
        except:
            pass

        if token is None:
            return Utils.JsonMessage("Token parameter not found!", 500)

        if not LoginService.validateJWTToken(token):
            return Utils.JsonMessage("Unauthorized", 401)

        if id is not None:
            model = None
            if modelDto is not None:
                model = JSONSerializator().serialize(modelDto)
            status, result, message, code = GenericHelperService.handleMethod(Task, method, model, id)
            if status:
                taskResponse = SimpleTaskResponseDto()
                taskResponse.fromEntity(result)
                return Utils.JsonResponse(taskResponse.getJson(), 200)
            else:
                if code is None:
                    code = 500
                return Utils.JsonMessage(message, code)
        else:
            if modelDto is not None:
                taskRequestDto = TaskRequestDto().serialize(modelDto)
                serialized = JSONSerializator().serialize(modelDto)
                if Utils.check_object_propertis(TaskRequestDto(), serialized):
                    entity = Task.createFromRequestDto(taskRequestDto, str(int(dt.now().timestamp())))
                    status, model, message, code = GenericHelperService.handleMethod(Task, method, entity, id)
                    if status:
                        e = DBUtil.findByName(Task, entity.name)
                        taskResponseDto = SimpleTaskResponseDto()
                        taskResponseDto.fromEntity(e)
                        return Utils.JsonResponse(taskResponseDto.getJson(), 201)
                    else:
                        return Utils.JsonMessage(message, code)
                else:
                    return Utils.JsonMessage("JSON format is not valid. Check properties".format(id), 500)
            else:
                if method == 'GET':
                    status, result, message, code = GenericHelperService.handleMethod(Task, method, None, None)
                    dtoList = []
                    for e in result:
                        dto = SimpleTaskResponseDto()
                        dto.fromEntity(e)
                        dtoList.append(dto.getJson())

                    listResponse = {
                        'tasks': dtoList
                    }

                    return Utils.JsonResponse(listResponse, 200)
                return Utils.JsonMessage("ID and body cannot be empty!".format(id), 500)



    @staticmethod
    def getTaskById(id):
        taskEntity = GenericHelperService.getModelById(Task, id)
        return taskEntity