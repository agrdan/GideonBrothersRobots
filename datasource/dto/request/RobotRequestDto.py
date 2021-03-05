from utils.JSONSerializator import JSONSerializator


class RobotRequestDto(JSONSerializator):

    def __init__(self):
        self.name = None
        self.type = None


    def __repr__(self):
        return str(self.__dict__)