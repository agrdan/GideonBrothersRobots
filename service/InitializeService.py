from main import db
from datetime import datetime as dt
from datasource.changelog.changelog import ChangeLog as cl
from datasource.entity.RobotType import RobotType, RobotTypes
from datasource.entity.RobotEntity import Robot
from datasource.entity.TaskType import TaskType, TaskTypes
from datasource.entity.TaskEntity import Task
from datasource.entity.TaskExecutionEntity import TaskExecution
from datasource.entity.LoginEntity import Login

class InitializeService:

    def __init__(self):
        pass

    @staticmethod
    def initialize():
        db.create_all()


        # types with default init values controlled by changelog
        taskCharging = TaskType.create(TaskTypes.CHARGING.value, TaskTypes.CHARGING.name, "charging", "driving")
        taskTransporting = TaskType.create(TaskTypes.TRANSPORTATION.value, TaskTypes.TRANSPORTATION.name, "transport", "driving")
        taskLifting = TaskType.create(TaskTypes.LIFTING.value, TaskTypes.LIFTING.name, "lifting", "driving")

        robotTransporter = RobotType.create(RobotTypes.TRANSPORTER.value, RobotTypes.TRANSPORTER.name, "charging", "driving", "transport")
        robotForklift = RobotType.create(RobotTypes.FORKLIFT.value, RobotTypes.FORKLIFT.name, "charging", "transport", "driving", "lifting")
        robotMulti = RobotType.create(RobotTypes.MULTI.value, RobotTypes.MULTI.name, "charging", "transport", "driving", "lifting", "anything")

        # by changelog this will execute only once
        cl.add_params('task_types-1', taskCharging, taskTransporting, taskLifting)
        cl.add_params('robot_types-1', robotTransporter, robotForklift, robotMulti)


        robot1 = Robot.create("robot-2", RobotTypes.MULTI.value, str(int(dt.now().timestamp())))
        cl.add_params('robot-1', robot1)

