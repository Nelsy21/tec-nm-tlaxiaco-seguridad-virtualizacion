import mysql.connector
from mysql.connector import Error

# Configuración de conexión
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'secure_db',
    'connection_timeout': 300  
}

def sql_injection_example():
    try:
        # Conectar a la base de datos MySQL
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        
        print("Conexión exitosa a la base de datos")

        # Ejemplo de inyección SQL
        print("Introduce para realizar una: ' OR '1'='1 ")
        user_input = input("Intenta una inyección SQL: ")

        # Consulta vulnerable (NO HACER EN PRODUCCIÓN)
        query = f"SELECT * FROM users WHERE email = '{user_input}' OR 1=1 -- '"

        print(f"Ejecutando consulta: {query}")  # Para que veas la consulta que se ejecuta
        cursor.execute(query)
        rows = cursor.fetchall()

        if rows:
            print("\nDatos Encontrados:")
            for row in rows:
                print(f"ID={row[0]}, Email={row[1]}, Password={row[2]}, Customer ID={row[3]}")
        else:
            print("No se encontraron datos.")

    except Error as e:
        print(f"Error al conectar o realizar operaciones: {e}")

    finally:
        # Cerrar la conexión correctamente
        if cnx.is_connected():
            cursor.close()
            cnx.close()
            print("Conexión cerrada")

# Llamar a la función
sql_injection_example()

