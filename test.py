"""
from datasource.dto.request.RobotRequestDto import RobotRequestDto
from utils.Utils import Utils
from utils.JSONSerializator import JSONSerializator
import json
from datetime import datetime as dt
from datasource.entity.TaskExecutionEntity import TaskExecution
from time import sleep as delay
from utils.DBUtil import DBUtil
"""
"""
test = {
    'name': 'test',
    'type': 'test',
    'asd': 'asd'
}

t = JSONSerializator().serialize(test)
print(t.getKeyList())

rr = RobotRequestDto().serialize(json.dumps(test), ignoreProperties=False)
print(rr.getKeyList())
diff = all(elem in t.getKeyList() for elem in rr.getKeyList())
print(diff)
"""
asd = bool(0)
print(asd)
"""
class Test:

    def __init__(self):
        pass


    def testRobotWork(self):
        n = dt.now()
        execution = TaskExecution.create(1, 1, n, str(int(n.timestamp())))
        delay(5)
        execution.setEnd(dt.now(), True)
        print(execution)
        DBUtil.insert(execution)

    def getTaskExecution(self):
        e = DBUtil.findById(TaskExecution, 1)
        print(e)
        print(str(e.end_time))







if __name__ == '__main__':
    t = Test()
    #t.testRobotWork()
    t.getTaskExecution()



"""