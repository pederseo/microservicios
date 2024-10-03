from config import Conexion

def ver_info():
    '''verificar si el usuario ya esta registrado, retorna tru si ya esta verificado'''

    cursor = Conexion.conn.cursor()
    cursor.execute("SELECT * FROM eventos;")
    resultados = cursor.fetchall()
    cursor.close()

    return resultados

def cargar_info(fecha_eventos: str, tipo_evento: str, monto_evento: str):
    '''funcion para registrar un nuevo usuario'''
    cursor = Conexion.conn.cursor()
    cursor.execute('''
                   INSERT INTO eventos 
                   (fecha_eventos, tipo_evento, monto_evento) VALUES (%s, %s, %s);''',
                   (fecha_eventos, tipo_evento, monto_evento))
    Conexion.conn.commit()
    cursor.close()

    return 'evento creado con exito'


# TRUNCATE TABLE users CASCADE;