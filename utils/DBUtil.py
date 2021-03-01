from main import db

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
