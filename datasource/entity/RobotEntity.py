from main import db


class Robot(db.Model):
    __tablename__ = 'robot'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    type = db.Column(db.Integer(), db.ForeignKey('robot_type.type'), nullable=False)
    created = db.Column(db.String(20))

    @staticmethod
    def create(name, _type, timestamp):
        robot = Robot()
        robot.name = name
        robot.type = _type
        robot.created = timestamp
        return robot

    @staticmethod
    def createFromRequestDto(requestDto, timestamp):
        return Robot.create(requestDto.name, requestDto.type, timestamp)

    def __repr__(self):
        return str(self.__dict__)
