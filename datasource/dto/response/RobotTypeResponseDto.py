from utils.JSONSerializator import JSONSerializator


class RobotTypeResponseDto(JSONSerializator):

    def __init__(self):
        self.id = None
        self.robotType = None
        self.name = None
        self.tags = None

    def fromEntity(self, entity):
        self.id = entity.id
        self.robotType = entity.type
        self.name = entity.name
        self.tags = entity.tags


    def getJson(self):
        tagList = self.tags.split(";")

        dto = {
            'id': self.id,
            'type': self.robotType,
            'name': self.name,
            'tags': tagList
        }
        return dto


    def __repr__(self):
        return str(self.__dict__)