from fastapi import FastAPI
from models import cargar_info,ver_info
from schemas import Register_data

app = FastAPI()

@app.get('/')
def root_mensaje():
    return {"info API: API informacion sobre banda"}

@app.post('/cargar_datos')
def cargar_datos(datos: Register_data):
    if datos:
        mensage = cargar_info(datos.fecha, datos.tipo, datos.pago)
    return {"mensage": mensage}

@app.get('/ver_datos')
def ver_datos():
    info = ver_info()

    return info
