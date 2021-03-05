from utils.JSONSerializator import JSONSerializator
from datasource.dto.response.RobotTypeResponseDto import RobotTypeResponseDto


class SimpleRobotResponseV2Dto(JSONSerializator):

    def __init__(self):
        self.id = None
        self.name = None
        self.typeId = None

    def fromEntity(self, entity):
        self.id = entity.id
        self.name = entity.name
        self.typeId = entity.type

    def getJson(self):
        dto = {
            'id': self.id,
            'name': self.name,
            'type': self.typeId
        }
        return dto
