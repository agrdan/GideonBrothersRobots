from datetime import datetime as dt
from utils.DBUtil import DBUtil
from utils.Utils import Utils
from utils.JSONSerializator import JSONSerializator
from datasource.dto.request.LoginDto import LoginDto
from datasource.entity.LoginEntity import Login
from datasource.dto.response.TokenDto import TokenDto
from datasource.dto.response.LoginResponseDto import LoginResponseDto
import jwt
from main import app
from utils.Logger import Logger

sessionTokens = set()


class LoginService:

    @staticmethod
    def register(loginDto):
        model = JSONSerializator().serialize(loginDto)
        if Utils.check_object_propertis(LoginDto(), model):
            e = Login().create(model.username, model.password, str(int(dt.now().timestamp())))
            DBUtil.insert(e)
            entity = DBUtil.findByUsername(Login, model.username)
            responseDto = LoginResponseDto()
            responseDto.fromEntity(entity)
            return Utils.JsonResponse(responseDto.getJson(), 201)
        else:
            return Utils.JsonMessage("JSON format is not valid. Check properties", 500)

    @staticmethod
    def login(loginDto):
        model = JSONSerializator().serialize(loginDto)
        if Utils.check_object_propertis(LoginDto(), model):
            e = DBUtil.findByUsername(Login, model.username)
            if e is not None:
                validate = Login.verify_password(e.password, model.password)
                if validate:
                    token = LoginService.generateJWTToken(model)
                    sessionTokens.add(token)
                    tokenDto = TokenDto()
                    tokenDto.token = token
                    return Utils.JsonResponse(tokenDto.getJson(), 200)
                else:
                    return Utils.JsonMessage("Unauthorized", 401)
            else:
                return Utils.JsonMessage("User does not exists", 404)
        else:
            return Utils.JsonMessage("JSON format is not valid. Check properties", 500)

    @staticmethod
    def generateJWTToken(model):
        m = {
            "username": model.username,
            "password": model.password
        }
        return str(jwt.encode(m, app.config["salt"]), "utf-8")

    @staticmethod
    def decodeJWTToken(token):
        return jwt.decode(token, app.config["salt"], algorithms=["HS256"])

    @staticmethod
    def getSessionTokens():
        Logger.info(sessionTokens)
        print("Active tokens in session: {}".format(len(sessionTokens)))

    @staticmethod
    def validateJWTToken(token):
        for t in sessionTokens:
            if t == token:
                return True
        return False
