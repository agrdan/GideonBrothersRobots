from threading import Thread
from datetime import datetime as dt
from datetime import timedelta
from utils.Utils import Utils
from utils.DBUtil import DBUtil
from datasource.entity.RobotEntity import Robot
from datasource.entity.TaskEntity import Task
from datasource.entity.TaskExecutionEntity import TaskExecution
from datasource.dto.response.TaskExecutedResponseDto import TaskExecutedResponseDto
from service.GBLoginService import LoginService
from io import StringIO

class ExecuteTasks(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        pass


ROBOT_ID = 'robot_id'
SIMULATED_TIME = 'simulated_time_seconds'
SIMULATED_STATUS = 'simulated_status'

FILTER_TASK_ID = 'taskId'
FILTER_ROBOT_ID = 'robotId'
FILTER_STATUS = 'status'
FILTER_DURATION_FROM = 'durationFrom'
FILTER_DURATION_TO = 'durationTo'
FILTER_DATE_FROM = 'dateFrom'
FILTER_DATE_TO = 'dateTo'

AUTH_TOKEN = 'Auth-Token'


class TaskExecutionService:

    @staticmethod
    def checkToken(token):

        if token is None:
            return Utils.JsonMessage("Token parameter not found!", 500)
        if not LoginService.validateJWTToken(token):
            return Utils.JsonMessage("Unauthorized", 401)

        return None

    @staticmethod
    def execute(id, args, header):

        try:
            token = header.get(AUTH_TOKEN)
            status = TaskExecutionService.checkToken(token)
            if status is not None:
                return status
        except:
            return Utils.JsonMessage("Internal server error", 500)

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
    def getAll(header):
        try:
            token = header.get(AUTH_TOKEN)
            status = TaskExecutionService.checkToken(token)
            if status is not None:
                return status
        except:
            return Utils.JsonMessage("Internal server error", 500)

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
    def getAllF(args, header, exportCsv=False):
        try:
            token = header.get(AUTH_TOKEN)
            status = TaskExecutionService.checkToken(token)
            if status is not None:
                return status
        except:
            return Utils.JsonMessage("Internal server error", 500)

        taskID = args.get(FILTER_TASK_ID)
        robotID = args.get(FILTER_ROBOT_ID)
        status = args.get(FILTER_STATUS)
        durationFrom = args.get(FILTER_DURATION_FROM)
        durationTo = args.get(FILTER_DURATION_TO)
        dateFrom = args.get(FILTER_DATE_FROM)
        dateTo = args.get(FILTER_DATE_TO)

        entityList = DBUtil.taskExecutionFilter(TaskExecution, taskId=taskID, robotId=robotID, status=status, durationFrom=durationFrom, durationTo=durationTo, dateFrom=dateFrom, dateTo=dateTo)
        dtoList = []
        for e in entityList:
            dto = TaskExecutedResponseDto()
            dto.fromEntity(e)
            dtoList.append(dto.getJson())

        jsonList = {
            'executed': dtoList
        }
        if exportCsv:
            csvData = ""#StringIO()
            for e in entityList:
                csvData += "{};{};{};{};{};{};{};{};{};{}\n".format(e.id, e.uuid, e.task_id, e.robot_id, e.date, e.start_time, e.end_time, e.duration, e.status, e.created)
            print(csvData)
            return csvData
        else:
            return Utils.JsonResponse(jsonList, 200)
