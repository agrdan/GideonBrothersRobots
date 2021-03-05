from datasource.entity.TaskEntity import Task
from datasource.entity.TaskType import TaskType
from datasource.dto.response.SimpleTaskResponse import SimpleTaskResponseDto
from datasource.dto.request.TaskRequestDto import TaskRequestDto
from service.GenericHelperService import GenericHelperService
from datetime import datetime as dt
from utils.DBUtil import DBUtil
from utils.Utils import Utils
from utils.JSONSerializator import JSONSerializator


class GBTaskService:

    def __init__(self):
        pass

    @staticmethod
    def action(method, modelDto, id=None):
        if id is not None:
            status, result = GenericHelperService.handleMethod(Task, method, modelDto, id)
            if status:
                taskResponse = SimpleTaskResponseDto()
                taskResponse.fromEntity(result)
                return Utils.JsonResponse(taskResponse.getJson(), 200)
            else:
                return Utils.JsonMessage("Entity with id [{}] not found!".format(id), 404)
        else:
            if modelDto is not None:
                taskRequestDto = TaskRequestDto().serialize(modelDto, ignoreProperties=False)
                print(taskRequestDto)
                serialized = JSONSerializator().serialize(modelDto)
                if Utils.check_object_propertis(TaskRequestDto(), serialized):
                    entity = Task.createFromRequestDto(taskRequestDto, str(int(dt.now().timestamp())))
                    status, model = GenericHelperService.handleMethod(Task, method, entity, id)
                    if status:
                        e = DBUtil.findByName(Task, entity.name)
                        taskResponse = SimpleTaskResponseDto()
                        taskResponse.fromEntity(e)
                        #robotResponseDto = RobotResponseDto()
                        #robotResponseDto.fromEntity(e)
                        #robotType = DBUtil.findByType(RobotType, robotResponseDto.typeId)
                        #robotTypeDto = RobotTypeResponseDto()
                        #robotTypeDto.fromEntity(robotType)
                        #robotResponseDto.setTypeDto(robotTypeDto)
                        return Utils.JsonResponse(taskResponse.getJson(), 201)
                    else:
                        return Utils.JsonMessage("Task not created! {} not valid or already exists!".format(serialized), 500)
                else:
                    return Utils.JsonMessage("JSON format is not valid. Check properties".format(id), 500)
            else:
                return Utils.JsonMessage("ID and body cannot be empty!".format(id), 500)



    @staticmethod
    def getTaskTypeByValue(typeValue):
        entity = DBUtil.findByType(TaskType, typeValue)
        #dto = TaskTypeResponseDto()
        #dto.fromEntity(entity)
        #print(dto.dumpModel())


    @staticmethod
    def getTaskById(id):
        taskEntity = GenericHelperService.getModelById(Task, id)
        return taskEntity

