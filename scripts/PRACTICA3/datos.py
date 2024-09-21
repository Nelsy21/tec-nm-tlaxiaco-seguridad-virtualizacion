import mysql.connector
from mysql.connector import Error
import csv

# Configuración de conexión
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'secure_db'
}

def insert_data(csv_file):
    try:
        # Conectar a la base de datos MySQL
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        
        print("Conexión exitosa a la base de datos")

        # Crear tabla si no existe (opcional, si ya existe en la base de datos, puedes omitir esto)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INT NOT NULL AUTO_INCREMENT,
            customer_id VARCHAR(45) NOT NULL,
            first_name VARCHAR(45) NOT NULL,
            last_name VARCHAR(45) NOT NULL,
            subscription_date DATE NOT NULL,
            website VARCHAR(45) NOT NULL,
            PRIMARY KEY (id)
        ) ENGINE=InnoDB;
        ''')

        print("Tabla `customers` verificada o creada")

        # Insertar datos desde el archivo CSV
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    cursor.execute('''
                        INSERT INTO customers (customer_id, first_name, last_name, subscription_date, website)
                        VALUES (%s, %s, %s, %s, %s)
                    ''', (
                        row['Customer Id'],
                        row['First Name'],
                        row['Last Name'],
                        row['Subscription Date'],
                        row['Website']
                    ))
                    print(f"Fila insertada: {row}")  # Mensaje de depuración
                except Error as e:
                    print(f"Error al insertar fila: {e}")

        # Confirmar los cambios
        cnx.commit()
        print("Datos insertados correctamente")

    except Error as e:
        print(f"Error al conectar o realizar operaciones: {e}")

    finally:
        # Cerrar la conexión
        if cnx.is_connected():
            cursor.close()
            cnx.close()
            print("Conexión cerrada")

# Llamar a la función con el archivo CSV
insert_data('C:/Users/Nelsy/Desktop/ITT/SEPTIMO SEMESTRE/SEGURIDAD Y VIRTUALIZACION/Bases_de_datos_seguras/customers-2000000.csv')
