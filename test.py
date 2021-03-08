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
import jwt

login = {
    "username":"agrdan",
    "password":"test123"
}

encodeJwt = jwt.encode(login, "sikret-key")
print(encodeJwt)

decoded = jwt.decode(encodeJwt, "sikret-key", algorithms=["HS256"])
print(decoded)

import hashlib
import os
import binascii

def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

passwd = hash_password("testis")
print(passwd)
print(len(passwd))

print(verify_password(passwd, "testis1"))