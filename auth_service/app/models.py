from config import Conexion

def verificacion_usuario(username: str, password: str):
    '''verificar si el usuario ya esta registrado, retorna tru si ya esta verificado'''
    try:
        cursor = Conexion.conn.cursor()
        cursor.execute('''
                       SELECT * FROM 
                       users WHERE username = %s;''',
                       (username,))
        usuario_existente = cursor.fetchone()
        if username in usuario_existente and password in usuario_existente:
            return True, f"{username} se a logeado"
        else:
            return False, "usuario o contraseña incorrectos"
    except:
        return "error de autentificacion"
    
    finally:
        cursor.close()

def registro_usuario(username: str, password: str):
    '''funcion para registrar un nuevo usuario'''
    cursor = Conexion.conn.cursor()
    cursor.execute('''
                   INSERT INTO users 
                   (username, password) VALUES (%s, %s);''',
                   (username, password))
    Conexion.conn.commit()
    cursor.close()

    return 'usuario registrado con exito'


# TRUNCATE TABLE users CASCADE;
