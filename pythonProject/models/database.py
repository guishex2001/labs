import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, values=None):
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def fetch_data(self, query, values=None):
        try:
            self.cursor.execute(query, values)
            result = self.cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

# Configuración de la base de datos
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""
DB_NAME = "laboratorio_veterinario"

# Crear una instancia de la clase Database
db = Database(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)

if __name__ == "__main__":
    # Prueba de la conexión y ejecución de consultas
    query_select_data = "SELECT * FROM Cliente"
    result = db.fetch_data(query_select_data)
    print(result)

    # Cerrar la conexión
    db.close_connection()
