from main import db

class Task(db.Model):

    __tablename__ = 'task'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    type = db.Column(db.Integer(), db.ForeignKey('task_type.type'))
    created = db.Column(db.String(20))

    @staticmethod
    def create(name, _type, timestamp):
        task = Task()
        task.name = name
        task.type = _type
        task.created = timestamp
        return task

    @staticmethod
    def createFromRequestDto(requestDto, timestamp):
        return Task.create(requestDto.name, requestDto.type, timestamp)