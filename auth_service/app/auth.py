import jwt
import datetime

SECRET_KEY = 'admin'
ALGORITMO = 'HS256'
TOKEN_TIME = 15

def create_access_token(username):
    payload = {
        'username':username,
        'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=TOKEN_TIME)
    }

    token = jwt.encode(payload,SECRET_KEY,ALGORITMO)

    return token