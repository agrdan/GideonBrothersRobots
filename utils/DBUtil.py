from main import db
from utils.Logger import Logger
from utils.Utils import Utils

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
            Logger.info("Query executed successfuly!")
            return True, model
        except Exception as e:
            db.session.rollback()
            Logger.info("Query rollbacked!")
            Logger.info(e)
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
            query = query.filter_by(task_id=taskId)
        if robotId is not None:
            query = query.filter_by(robot_id=robotId)
        if status is not None:
            query = query.filter_by(status=status)
        if dateFrom is not None:
            query = query.filter(clazz.date >= dateFrom)
        if durationFrom is not None:
            query = query.filter(clazz.duration >= durationFrom)
        if durationTo is not None:
            query = query.filter(clazz.duration <= durationTo)
        if dateFrom is not None:
            d = Utils.parseStringDtToDate(dateFrom)
            query = query.filter(clazz.date >= d)
        if dateTo is not None:
            d = Utils.parseStringDtToDate(dateTo)
            query = query.filter(clazz.date <= d)

        entityList = query.all()
        return entityList