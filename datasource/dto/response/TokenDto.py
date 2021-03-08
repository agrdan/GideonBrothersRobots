from utils.JSONSerializator import JSONSerializator


class TokenDto(JSONSerializator):

    def __init__(self):
        self.token = None


    def getJson(self):
        token = {
            'token': self.token
        }
        return token

    def __repr__(self):
        return str(self.__dict__)