from utils.JSONSerializator import JSONSerializator


class TaskExecutedResponseDto(JSONSerializator):

    def __init__(self):
        self.id = None
        self.uuid = None
        self.taskId = None
        self.robotId = None
        self.date = None
        self.startTime = None
        self.endTime = None
        self.duration = None
        self.status = None

    def fromEntity(self, entity):
        self.id = entity.id
        self.uuid = entity.uuid
        self.taskId = entity.task_id
        self.robotId = entity.robot_id
        self.date = str(entity.date)
        self.startTime = str(entity.start_time)
        self.endTime = str(entity.end_time)
        self.duration = entity.duration
        self.status = entity.status

    def getJson(self):
        dto = {
            'id': self.id,
            'uuid': self.uuid,
            'task_id': self.taskId,
            'robot_id': self.robotId,
            'date': self.date,
            'start_time': self.startTime,
            'end_time': self.endTime,
            'duration': self.duration,
            'successful': self.status
        }
        return dto
