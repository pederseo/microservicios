import requests


def ver_datos():
    '''funcion para autentificar usuario'''
    url = "http://localhost:5001/ver_datos"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {"error": "en la consulta a la api"}
