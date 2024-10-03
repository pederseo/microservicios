from pydantic import BaseModel

class Register_data(BaseModel):
    fecha: str
    tipo: str
    pago: str
