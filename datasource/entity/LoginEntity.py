from main import db
import hashlib
import os
import binascii


class Login(db.Model):
    __tablename__ = 'login'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(192), nullable=False)
    created = db.Column(db.String(20))

    @staticmethod
    def hash_password(password):
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                      salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    @staticmethod
    def verify_password(stored_password, provided_password):
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512',
                                      provided_password.encode('utf-8'),
                                      salt.encode('ascii'),
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password

    @staticmethod
    def create(username, password, timestamp):
        login = Login()
        login.username = username
        login.password = Login.hash_password(password)
        login.created = timestamp
        return login

    @staticmethod
    def createFromRequestDto(requestDto, timestamp):
        return Login.create(requestDto.username, requestDto.password, timestamp)

    def __repr__(self):
        return str(self.__dict__)
