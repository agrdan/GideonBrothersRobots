from utils.DBUtil import DBUtil
from utils.Logger import Logger

class GenericHelperService:


    @staticmethod
    def handleMethod(clazz, method, model, id=None):
        result = None
        status = False
        message = None
        code = None
        entityById = None
        if id is not None:
            entityById = DBUtil.findById(clazz, id)
        if method == 'POST':
            s, model = DBUtil.insert(model)
            status = s
            result = model
            if not status:
                code = 500
                message = "Robot not created [{}]".format(model)
        elif method == 'PUT':
            if entityById is not None:
                GenericHelperService.compareWithCurrent(entityById, model)
                status = True
                result = entityById
            else:
                status = False
                result = None
                if id is None:
                    message = "PUT method [PATH param ID is missing]"
                    code = 500
                else:
                    message = "Entity not found"
                    code = 404
        elif method == 'GET':
            if id is not None:
                result = DBUtil.findById(clazz, id)
            else:
                result = DBUtil.findAll(clazz)
            if result is None:
                status = False
                code = 404
                message = "Entity not found"
            else:
                status = True
        elif method == 'DELETE':
            success = True
            if entityById is not None:
                DBUtil.delete(entityById)
            else:
                try:
                    DBUtil.delete(model)
                except:
                    success = False

            if not success:
                pass

        return status, result, message, code

    @staticmethod
    def getModelById(clazz, id):
        e = DBUtil.findById(clazz, id)
        return e


    @staticmethod
    def compareWithCurrent(toCompare, current):
        changed = False
        if not toCompare.name == current.name:
            toCompare.name = current.name
            changed = True

        if not toCompare.type == current.type:
            toCompare.type = current.type
            changed = True

        if changed:
            DBUtil.commit()