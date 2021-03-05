from utils.DBUtil import DBUtil
from utils.Logger import Logger

class GenericHelperService:


    # model should always be entity
    @staticmethod
    def handleMethod(clazz, method, model, id=None):
        result = None
        status = False
        currentEntity = None
        if id is not None:
            currentEntity = DBUtil.findById(clazz, id)
            # will be used later
        if method == 'POST':
            s, model = DBUtil.insert(model)
            status = s
            result = model
        elif method == 'PUT':
            entity = DBUtil.findByName(clazz, model.name)
            if entity is not None:
                entity = model
                DBUtil.commit()
        elif method == 'GET':
            if id is not None:
                result = DBUtil.findById(clazz, id)
            else:
                result = DBUtil.findByName(clazz, model.name)

            if result is None:
                status = False
            else:
                status = True
        elif method == 'DELETE':
            success = True
            if id is not None:
                entity = DBUtil.findById(clazz, id)
                DBUtil.delete(entity)
            else:
                try:
                    DBUtil.delete(model)
                except:
                    success = False

            if not success:
                pass

        return status, result

    @staticmethod
    def getModelById(clazz, id):
        e = DBUtil.findById(clazz, id)
        return e