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

def insert_data():
    try:
        # Conectar a la base de datos MySQL
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        
        print("Conexión exitosa a la base de datos")

        # Crear tabla si no existe (opcional)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INT NOT NULL AUTO_INCREMENT,
            email VARCHAR(100) NOT NULL,
            password VARCHAR(100) NOT NULL,
            customer_id VARCHAR(45) NOT NULL,
            PRIMARY KEY (id),
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        ) ENGINE=InnoDB;
        ''')

        print("Tabla `users` verificada o creada")

        # Solicitar datos del usuario
        while True:
            email = input("Introduce el email: ")
            password = input("Introduce el password: ")
            customer_id = input("Introduce el customer_id: ")

            try:
                # Insertar datos en la tabla
                cursor.execute('''
                    INSERT INTO users (email, password, customer_id)
                    VALUES (%s, %s, %s)
                ''', (
                    email,
                    password,
                    customer_id
                ))

                # Confirmar los cambios
                cnx.commit()
                
                print(f"Datos insertados: Email={email}, Customer ID={customer_id}")
                
                # Recuperar y mostrar los datos recién insertados
                cursor.execute("SELECT * FROM users WHERE email = %s AND customer_id = %s", (email, customer_id))
                inserted_row = cursor.fetchone()
                
                if inserted_row:
                    print(f"Datos insertados en la base de datos: ID={inserted_row[0]}, Email={inserted_row[1]}, Password={inserted_row[2]}, Customer ID={inserted_row[3]}")
                else:
                    print("No se pudo recuperar la fila insertada.")

            except Error as e:
                print(f"Error al insertar los datos: {e}")
                print(f"SQLSTATE: {e.sqlstate}, Error Code: {e.errno}")

            # Preguntar si el usuario quiere insertar otra fila
            another = input("¿Deseas insertar otro usuario? (s/n): ")
            if another.lower() != 's':
                break

        # Mostrar todos los datos de la tabla 'users' después de terminar las inserciones
        cursor.execute("SELECT * FROM users")
        all_rows = cursor.fetchall()

        print("\n----- ---------------------'users'--------------------- ---------")
        for row in all_rows:
            print(f"ID={row[0]}, Email={row[1]}, Password={row[2]}, Customer ID={row[3]}")
        print("\n--------------------------------------------- -------------------")

    except Error as e:
        print(f"Error al conectar o realizar operaciones: {e}")

    finally:
        # Cerrar la conexión correctamente
        if cnx.is_connected():
            cursor.close()
            cnx.close()
            print("Conexión cerrada")

# Llamar a la función
insert_data()
