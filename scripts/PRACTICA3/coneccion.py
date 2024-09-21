import mysql.connector
from mysql.connector import Error

# Configuración de conexión
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',  # o la IP del servidor MySQL
    'database': 'secure_db'
}

try:
    # Intentar la conexión
    cnx = mysql.connector.connect(**config)

    # Verificar si la conexión fue exitosa
    if cnx.is_connected():
        print("Conexión exitosa a la base de datos")
    
    # Aquí podrías ejecutar tus consultas

except Error as e:
    print(f"Error al conectarse a la base de datos: {e}")

finally:
    # Cerrar la conexión si está abierta
    if cnx.is_connected():
        cnx.close()
        print("Conexión cerrada")
