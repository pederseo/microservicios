import requests
import jwt

SECRET_KEY = 'admin'
ALGORITMO = 'HS256'

def registro_usuario(username, password):
    '''funcion para registrar nuevo usuario'''
    url = "http://localhost:5000/registro"

    datos_registro = {
        "username":username,
        "password":password
    }

    response = requests.post(url, json=datos_registro)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "en la consulta a la api"}
    
def login_usuario(username, password):
    '''funcion para autentificar usuario'''
    url = "http://localhost:5000/login"

    datos_login = {
        "username":username,
        "password":password
    }

    response = requests.post(url, json=datos_login)

    if response.status_code == 200:
        token = response.json()
        return token['acces_token']
    else:
        return {"error": "en la consulta a la api"}


def decode_token(token):
    try:
        decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITMO])
        print(f"token decodificado: {decoded_payload}")
        return decoded_payload
    except jwt.ExpiredSignatureError:
        print("El token ha expirado.")
    except jwt.InvalidTokenError:
        print("Token inválido.")
