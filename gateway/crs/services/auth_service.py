import requests

def register(username, password):
    '''funcion para registrar nuevo usuario'''
    url = f'direccion_url'

    payload = {
        username,
        password
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def login(username, password):
    '''funcion para autentificar usuario'''
    url = f'direccion_url'

    payload = {
        username,
        password
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return None