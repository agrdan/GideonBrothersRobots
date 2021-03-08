from utils.JSONSerializator import JSONSerializator


class LoginResponseDto(JSONSerializator):

    def __init__(self):
        self.id = None
        self.username = None

    def fromEntity(self, entity):
        self.id = entity.id
        self.username = entity.username

    def getJson(self):
        dto = {
            'id': self.id,
            'username': self.username,
        }
        return dto
