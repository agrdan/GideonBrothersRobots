from datasource.entity.RobotEntity import Robot
from datasource.entity.RobotType import RobotType
from service.GenericHelperService import GenericHelperService
from datasource.dto.request.RobotRequestDto import RobotRequestDto
from datasource.dto.response.RobotResponseDto import RobotResponseDto, RobotTypeResponseDto
from datasource.dto.response.SimpleRobotResponseDto import SimpleRobotResponseDto
from utils.Logger import Logger
from datetime import datetime as dt
from utils.DBUtil import DBUtil
from utils.Utils import Utils
from utils.JSONSerializator import JSONSerializator


class GBRobotService:

    def __init__(self):
        pass

    @staticmethod
    def action(method, modelDto, id=None):
        if id is not None:
            model = None
            if modelDto is not None:
                model = JSONSerializator().serialize(modelDto, ignoreProperties=True)
            status, result, message, code = GenericHelperService.handleMethod(Robot, method, model, id)
            if status:
                robotResponse = SimpleRobotResponseDto()
                robotResponse.fromEntity(result)
                return Utils.JsonResponse(robotResponse.getJson(), 200)
            else:
                if code is None:
                    code = 500
                return Utils.JsonMessage(message, code)
        else:
            if modelDto is not None:
                robotRequestDto = RobotRequestDto().serialize(modelDto, ignoreProperties=False)
                print(robotRequestDto)
                serialized = JSONSerializator().serialize(modelDto)
                if Utils.check_object_propertis(RobotRequestDto(), serialized):
                    entity = Robot.createFromRequestDto(robotRequestDto, str(int(dt.now().timestamp())))
                    status, model, message, code = GenericHelperService.handleMethod(Robot, method, entity, id)
                    if status:
                        e = DBUtil.findByName(Robot, entity.name)
                        robotResponseDto = RobotResponseDto()
                        robotResponseDto.fromEntity(e)
                        robotType = DBUtil.findByType(RobotType, robotResponseDto.typeId)
                        robotTypeDto = RobotTypeResponseDto()
                        robotTypeDto.fromEntity(robotType)
                        robotResponseDto.setTypeDto(robotTypeDto)
                        return Utils.JsonResponse(robotResponseDto.getJson(), 201)
                    else:
                        return Utils.JsonMessage(message, code)
                else:
                    return Utils.JsonMessage("JSON format is not valid. Check properties".format(id), 500)
            else:
                if method == 'GET':
                    status, result, message, code = GenericHelperService.handleMethod(Robot, method, None, None)

                return Utils.JsonMessage("ID and body cannot be empty!".format(id), 500)



    @staticmethod
    def getRobotTypeByValue(typeValue):
        entity = DBUtil.findByType(RobotType, typeValue)
        dto = RobotTypeResponseDto()
        dto.fromEntity(entity)
        print(dto.dumpModel())


    @staticmethod
    def getRobotById(id):
        robotEntity = GenericHelperService.getModelById(Robot, id)
        return robotEntity

