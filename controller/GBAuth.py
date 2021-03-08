from flask import request, Blueprint

from service.GBLoginService import LoginService

auth = Blueprint('auth', __name__)
login = LoginService()


class Auth:

    @staticmethod
    @auth.route('/registration', methods=['POST'])
    def registration():
        return login.register(request.json)


    @staticmethod
    @auth.route("/login", methods=['GET'])
    def login():
        login.getSessionTokens()
        return login.login(request.json)


