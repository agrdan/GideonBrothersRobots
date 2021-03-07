from main import db
import uuid

class TaskExecution(db.Model):

    __tablename__ = 'task_execution'

    id = db.Column(db.Integer(), primary_key=True)
    uuid = db.Column(db.String(36), unique=True, nullable=False)
    task_id = db.Column(db.Integer(), db.ForeignKey('task.id'))
    robot_id = db.Column(db.Integer(), db.ForeignKey('robot.id'))
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    duration = db.Column(db.Integer(), nullable=False)
    status = db.Column(db.Boolean)
    created = db.Column(db.String(20))

    @staticmethod
    def create(taskId, robotId, date, startTime, timestamp):
        task = TaskExecution()
        task.uuid = str(uuid.uuid4())
        task.task_id = taskId
        task.date = date
        task.robot_id = robotId
        task.start_time = startTime
        task.created = timestamp
        return task

    def setEnd(self, endTime, duration, status):
        self.end_time = endTime
        self.duration = duration
        self.status = status

    @staticmethod
    def createFromRequestDto(requestDto, timestamp):
        #return TaskExecution.create(requestDto.name, requestDto.type, timestamp)
        pass


    def __repr__(self):
        return str(self.__dict__)
