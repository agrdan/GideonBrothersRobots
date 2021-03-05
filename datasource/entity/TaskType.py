from main import db
from enum import Enum

class TaskTypes(Enum):
    TRANSPORTATION = 200
    CHARGING = 201
    LIFTING = 202


class TaskType(db.Model):

    __tablename__ = 'task_type'
    id = db.Column(db.Integer(), primary_key=True)
    type = db.Column(db.Integer(), nullable=False, unique=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    tags = db.Column(db.String(255))

    @staticmethod
    def create(_type, name, *tags: str):
        taskType = TaskType()
        taskType.type = _type
        taskType.name = name
        taskType.tags = ""
        for t in tags:
            taskType.tags += "{};".format(t)
        return taskType