# Band Manager Microservices Gateway

## Descripción

Este proyecto es el gateway para el sistema de gestión de bandas. Orquesta los servicios de autenticación, información de bandas y pagos.

## Tecnologías

- **Python**
- **Flask**
- **FastAPI**
- **PostgreSQL**

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/pederseo/microservicios
    cd microservicios
    ```

2. Crea un entorno virtual y actívalo:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Inicia los servidores:

    - Gateway:

        ```bash
        python gateway/crs/app.py
        ```

    - Servicio de Autenticación:

        ```bash
        cd auth_service/app
        uvicorn main:app --reload --host localhost --port 5000
        ```

    - Servicio de Información de Bandas:

        ```bash
        cd info_service/app
        uvicorn main:app --reload --host localhost --port 5001
        ```

## Uso

Accede a la aplicación en `http://192.168.20.95:80`.

---

