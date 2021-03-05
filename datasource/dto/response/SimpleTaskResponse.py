from utils.JSONSerializator import JSONSerializator


class SimpleTaskResponseDto(JSONSerializator):

    def __init__(self):
        self.id = None
        self.name = None
        self.type = None

    def fromEntity(self, entity):
        self.id = entity.id
        self.name = entity.name
        self.type = entity.type

    def getJson(self):
        dto = {
            'id': self.id,
            'name': self.name,
            'type': self.type
        }
        return dto
