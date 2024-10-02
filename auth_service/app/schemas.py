from pydantic import BaseModel

class Register_data(BaseModel):
    username: str
    password: str

class Login_data(BaseModel):
    username: str
    password: str

# class 