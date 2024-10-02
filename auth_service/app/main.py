from fastapi import FastAPI
from models import registro_usuario, verificacion_usuario
from schemas import Register_data, Login_data
from auth import create_access_token

app = FastAPI()

@app.get('/')
def root_mensaje():
    return {"info API: API Authentification con JWT"}

@app.post('/registro')
def registro(datos: Register_data):
    if datos:
        mensage = registro_usuario(datos.username, datos.password)
    return {"mensage": mensage}

@app.post('/login')
def login(datos: Login_data):
    verificacion, mensage = verificacion_usuario(datos.username, datos.password)
    if verificacion == True:
        access_token = create_access_token(datos.username)
        return {"mensage":mensage,"acces_token": access_token, "token_type": "bearer"}
    
    elif verificacion == False:
        return {"mensage":mensage}