import psycopg2

class Conexion:
    conn = psycopg2.connect(
        dbname='auth_service',
        user='olaf',
        password='12345',
        host='localhost',
    )

