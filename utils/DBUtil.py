from main import db
from utils.Logger import Logger

class DBUtil:

    @staticmethod
    def findByUsername(clazz, username):
        entity = clazz.query.filter_by(username=username).one_or_none()
        return entity

    @staticmethod
    def insert(model):
        try:
            db.session.add(model)
            db.session.commit()
            print("Query executed successfuly!")
            return True, model
        except Exception as e:
            db.session.rollback()
            print("Query rollbacked!")
            print(e)
            return False, str(e)



    @staticmethod
    def commit():
        db.session.commit()

    @staticmethod
    def findAll(clazz):
        eList = clazz.query.all()
        return eList


    @staticmethod
    def findById(clazz, id):
        entity = clazz.query.filter_by(id=id).one_or_none()
        return entity


    @staticmethod
    def delete(model):
        try:
            db.session.delete(model)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False


    @staticmethod
    def findByMac(clazz, mac):
        entity = clazz.query.filter_by(mac=mac).one_or_none()
        return entity


    @staticmethod
    def findByName(clazz, name):
        entity = clazz.query.filter_by(name=name).one_or_none()
        return entity


    @staticmethod
    def findByToken(clazz, token):
        entity = clazz.query.filter_by(token=token).one_or_none()
        return entity


    @staticmethod
    def findByType(clazz, _type):
        entity = clazz.query.filter_by(type=_type).one_or_none()
        return entity


    @staticmethod
    def taskExecutionFilter(clazz, taskId=None, robotId=None, dateFrom=None, dateTo=None,
                            timeFrom=None, timeTo=None, durationFrom=None,
                            durationTo=None, status=None):
        query = clazz.query
        if taskId is not None:
            query = clazz.query.filter_by(task_id=taskId)
        if robotId is not None:
            query = query.filter_by(robot_id=robotId)
        if status is not None:
            query = query.filter_by(status=status)
        if timeFrom is not None and timeTo is not None:
            query = query.filter_by()

        entityList = query.all()
        return entityList