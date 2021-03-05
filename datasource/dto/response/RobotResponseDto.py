from utils.JSONSerializator import JSONSerializator
from datasource.dto.response.RobotTypeResponseDto import RobotTypeResponseDto


class RobotResponseDto(JSONSerializator):

    def __init__(self):
        self.id = None
        self.name = None
        self.typeId = None
        self.type: RobotTypeResponseDto = None


    def fromEntity(self, entity):
        self.id = entity.id
        self.name = entity.name
        self.typeId = entity.type


    def setTypeDto(self, typeDto):
        self.type = typeDto


    def getJson(self):
        dto = {
            'id': self.id,
            'name': self.name,
            'type': self.type.getJson()
        }
        return dto

    def __repr__(self):
        return str(self.__dict__)