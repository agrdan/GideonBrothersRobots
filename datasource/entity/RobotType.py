from main import db
from enum import Enum

class RobotTypes(Enum):
    TRANSPORTER = 100
    FORKLIFT = 101
    MULTI = 102


class RobotType(db.Model):

    __tablename__ = 'robot_type'
    id = db.Column(db.Integer(), primary_key=True)
    type = db.Column(db.Integer(), nullable=False, unique=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    tags = db.Column(db.String(255))


    @staticmethod
    def create(_type, name, *tags: str):
        robotType = RobotType()
        robotType.type = _type
        robotType.name = name
        robotType.tags = ""
        for t in tags:
            robotType.tags += "{};".format(t)
        return robotType


    def __repr__(self):
        return str(self.__dict__)