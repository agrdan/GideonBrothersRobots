from threading import Thread
from datetime import datetime as dt
from datetime import timedelta
from utils.Utils import Utils
from utils.DBUtil import DBUtil
from datasource.entity.RobotEntity import Robot
from datasource.entity.TaskEntity import Task
from datasource.entity.TaskExecutionEntity import TaskExecution
from datasource.dto.response.TaskExecutedResponseDto import TaskExecutedResponseDto

class ExecuteTasks(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        pass


ROBOT_ID = 'robot_id'
SIMULATED_TIME = 'simulated_length'
SIMULATED_STATUS = 'simulated_status'

FILTER_TASK_ID = 'taskId'
FILTER_ROBOT_ID = 'robotId'
FILTER_STATUS = 'status'

class TaskExecutionService:



    @staticmethod
    def execute(id, args):

        task = DBUtil.findById(Task, id)
        if task is None:
            return Utils.JsonMessage("Task ID[{}] does not exists!".format(id), 404)

        robotID = None
        simulatedTime = None
        simulatedStatus = None

        try:
            robotID = args.get(ROBOT_ID)
        except Exception as e:
            pass

        try:
            simulatedTime = args.get(SIMULATED_TIME)
        except:
            pass

        try:
            simulatedStatus = args.get(SIMULATED_STATUS)
        except:
            pass

        if robotID is None:
            Utils.JsonMessage("robot_id parameter is missing", 500)
        else:
            robot = DBUtil.findById(Robot, robotID)
            if robot is None:
                return Utils.JsonMessage("Robot ID[{}] does not exists!".format(robotID), 404)
            startTime = dt.now()
            d = startTime.date()
            t = startTime.time()
            ts = startTime.timestamp()
            execution = TaskExecution.create(int(id), int(robotID), d, t, str(int(ts)))
            if simulatedTime is not None:
                endTime = startTime + timedelta(seconds=int(simulatedTime))
            else:
                endTime = startTime + timedelta(seconds=30)
            duration = endTime - startTime
            s = True
            if simulatedStatus is not None:
                s = bool(int(simulatedStatus))


            execution.setEnd(endTime.time(), duration.seconds, s)
            status, model = DBUtil.insert(execution)
            if status:
                print(model)
                return Utils.JsonMessage("Task ID[{}] executed by robot ID[{}]!".format(id, robotID), 200)
            else:
                return Utils.JsonMessage("Task ID[{}] not executed!", 500)


    @staticmethod
    def getAll():

        entityList = DBUtil.findAll(TaskExecution)
        dtoList = []
        for e in entityList:
            dto = TaskExecutedResponseDto()
            dto.fromEntity(e)
            dtoList.append(dto.getJson())

        jsonList = {
            'executed': dtoList
        }

        return Utils.JsonResponse(jsonList, 200)

    @staticmethod
    def getAllF(args):

        # entityList = DBUtil.findAll(TaskExecution)
        taskID = None
        robotID = None
        status = None
        try:
            taskID = args.get(FILTER_TASK_ID)
        except:
            pass
        try:
            robotID = args.get(FILTER_ROBOT_ID)
        except:
            pass
        try:
            status = args.get(FILTER_STATUS)
        except:
            pass
        entityList = DBUtil.taskExecutionFilter(TaskExecution, taskId=taskID, robotId=robotID, status=status)
        dtoList = []
        for e in entityList:
            dto = TaskExecutedResponseDto()
            dto.fromEntity(e)
            dtoList.append(dto.getJson())

        jsonList = {
            'executed': dtoList
        }

        return Utils.JsonResponse(jsonList, 200)