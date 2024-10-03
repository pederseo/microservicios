import psycopg2

class Conexion:
    conn = psycopg2.connect(
        dbname='band_info',
        user='olaf',
        password='12345',
        host='localhost',
    )

