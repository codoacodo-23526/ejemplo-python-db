# Son librerias que se importan para que funcione el proyecto
# algunas opciones son:

# PyMySql connection --> pip install PyMySQL
# SQL Alchemy connection --> pip install SQLAlchemy
# Flask mysql connection --> pip install flask-mysqldb


# MySQL connection --> pip install mysql-connector-python

# CRUD : CREATE / READ / UPDATE / DELETE  -> Clasico ABM C Comun de datos

# import pymysql.connections
import mysql.connector
# localhost = 127.0.0.1 ip de la maquina local
# host = 'ip del servidor de bd'

def conectar_db():
    conexion = mysql.connector.connect(
        host = 'localhost', 
        user = 'root',
        password = '',
        port = 3306,
        database = 'cac-persona'
    )    
    return conexion

def crear_persona(nombre, edad):
    conexion = conectar_db() # Abrimos la conexion  al DB 
    try:
        cursor = conexion.cursor() # cursor para ejecutar las consultas
        sql = "INSERT INTO personas (nombre,edad) VALUES ('" + nombre + "'," + str(edad) + ");"
        cursor.execute(sql) # ejecutar la consulta
        conexion.commit() # guardar los cambios en la base de datos
    except ConnectionError:
        print("Error de conexion")
    except Exception as e:
        print("Ha ocurrido un error no previsto", type(e).__name__)
    finally:
        conexion.close()  # Cerramos la conexion a la BD
        

def borrar_persona(id):
    conexion = conectar_db() # Abrimos la conexion  al DB 
    try:
        cursor = conexion.cursor() # cursor para ejecutar las consultas        
        sql = "DELETE FROM `cac-persona`.`personas` WHERE  id =" + str(id) + ";"
        cursor.execute(sql) # ejecutar la consulta
        conexion.commit() # guardar los cambios en la base de datos
    except ConnectionError:
        print("Error de conexion")
    except Exception as e:
        print("Ha ocurrido un error no previsto", type(e).__name__)
    finally:
        conexion.close() # Cerramos la conexion a la BD
        

def modificar_persona(id, nombre, edad):
    conexion = conectar_db()    
    try:
        cursor = conexion.cursor() # cursor para ejecutar las consultas        
        sql = "UPDATE `cac-persona`.`personas` SET `nombre` = '" + nombre + "', `edad` = " + str(edad) + " WHERE id= " + str(id) + ";"
        cursor.execute(sql)
        conexion.commit() # Conexion comiteamos
    except ConnectionError:
        print("Error de conexion")
    except Exception as e:
        print("Ha ocurrido un error no previsto", type(e).__name__)
    finally:
        conexion.close()
        

def leer_personas():
    conexion = conectar_db()    
    try:
        cursor = conexion.cursor() # cursor para ejecutar las consultas        
        sql = "SELECT * FROM `cac-persona`.personas;"
        cursor.execute(sql)
        listado_de_personas = cursor.fetchall()
        return listado_de_personas
    except ConnectionError:
        print("Error de conexion")
    except Exception as e:
        print("Ha ocurrido un error no previsto", type(e).__name__)
    finally:
        conexion.close()



# Programa Principal

crear_persona("Juan", 20)

borrar_persona(1)

modificar_persona(4, "PIRULO", 30)

personas = leer_personas()
for persona in personas:
    print(persona)