## Instalación
1. Clonar el repositorio.       `python -m venv venv`
2. Crear un entorno virtual.    `venv\Scripts\activate`
3. Instalar las dependencias:   `pip install -r src/requirements.txt`.
4. Ejecutar la aplicación:      `python src/app.py`.

uvicorn main:app --reload --host localhost --port 5001


fastapi: Framework para desarrollar APIs de manera rápida.
uvicorn: Para ejecutar la aplicación FastAPI.
pyjwt: Para trabajar con JSON Web Tokens (JWT).
passlib[bcrypt]: Para hashear y verificar contraseñas utilizando bcrypt, un algoritmo de hashing seguro.


pip install passlib