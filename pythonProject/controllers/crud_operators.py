from models.database import Database

class CRUDOperations:
    def __init__(self):
        self.db = Database(host="localhost", user="root", password="", database="laboratorio_veterinario")

    # CRUD para Cliente
    def crear_cliente(self, nombre, apellido, direccion, telefono, otros_detalles):
        query = "INSERT INTO Cliente (Nombre, Apellido, Direccion, Telefono, OtrosDetalles) VALUES (%s, %s, %s, %s, %s)"
        values = (nombre, apellido, direccion, telefono, otros_detalles)
        return self.db.execute_query(query, values)

    def obtener_clientes(self):
        query = "SELECT * FROM Cliente"
        return self.db.fetch_data(query)

    def obtener_cliente_por_id(self, cliente_id):
        query = "SELECT * FROM Cliente WHERE IdCliente = %s"
        values = (cliente_id,)
        return self.db.fetch_data(query, values)

    def actualizar_cliente(self, cliente_id, nombre, apellido, direccion, telefono, otros_detalles):
        query = "UPDATE Cliente SET Nombre = %s, Apellido = %s, Direccion = %s, Telefono = %s, OtrosDetalles = %s WHERE IdCliente = %s"
        values = (nombre, apellido, direccion, telefono, otros_detalles, cliente_id)
        return self.db.execute_query(query, values)

    def eliminar_cliente(self, cliente_id):
        query = "DELETE FROM Cliente WHERE IdCliente = %s"
        values = (cliente_id,)
        return self.db.execute_query(query, values)

    # CRUD para Animal
    def crear_animal(self, id_cliente, nombre_animal, especie, edad, otra_informacion):
        query = "INSERT INTO Animal (IdCliente, NombreAnimal, Especie, Edad, OtraInformacion) VALUES (%s, %s, %s, %s, %s)"
        values = (id_cliente, nombre_animal, especie, edad, otra_informacion)
        return self.db.execute_query(query, values)

    def obtener_animales(self):
        query = "SELECT * FROM Animal"
        return self.db.fetch_data(query)

    def obtener_animal_por_id(self, animal_id):
        query = "SELECT * FROM Animal WHERE IdAnimal = %s"
        values = (animal_id,)
        return self.db.fetch_data(query, values)

    def actualizar_animal(self, animal_id, id_cliente, nombre_animal, especie, edad, otra_informacion):
        query = "UPDATE Animal SET IdCliente = %s, NombreAnimal = %s, Especie = %s, Edad = %s, OtraInformacion = %s WHERE IdAnimal = %s"
        values = (id_cliente, nombre_animal, especie, edad, otra_informacion, animal_id)
        return self.db.execute_query(query, values)

    def eliminar_animal(self, animal_id):
        query = "DELETE FROM Animal WHERE IdAnimal = %s"
        values = (animal_id,)
        return self.db.execute_query(query, values)

    # CRUD para Analisis
    def crear_analisis(self, id_animal, tipo_analisis, resultados, fecha_analisis, observaciones):
        query = "INSERT INTO Analisis (IdAnimal, TipoAnalisis, Resultados, FechaAnalisis, Observaciones) VALUES (%s, %s, %s, %s, %s)"
        values = (id_animal, tipo_analisis, resultados, fecha_analisis, observaciones)
        return self.db.execute_query(query, values)

    def obtener_analisis(self):
        query = "SELECT * FROM Analisis"
        return self.db.fetch_data(query)

    def obtener_analisis_por_id(self, analisis_id):
        query = "SELECT * FROM Analisis WHERE IdAnalisis = %s"
        values = (analisis_id,)
        return self.db.fetch_data(query, values)

    def actualizar_analisis(self, analisis_id, id_animal, tipo_analisis, resultados, fecha_analisis, observaciones):
        query = "UPDATE Analisis SET IdAnimal = %s, TipoAnalisis = %s, Resultados = %s, FechaAnalisis = %s, Observaciones = %s WHERE IdAnalisis = %s"
        values = (id_animal, tipo_analisis, resultados, fecha_analisis, observaciones, analisis_id)
        return self.db.execute_query(query, values)

    def eliminar_analisis(self, analisis_id):
        query = "DELETE FROM Analisis WHERE IdAnalisis = %s"
        values = (analisis_id,)
        return self.db.execute_query(query, values)

    def cerrar_conexion(self):
        self.db.close_connection()

# Ejemplo de uso:
# crud_operations = CRUDOperations()
# clientes = crud_operations.obtener_clientes()
# animales = crud_operations.obtener_animales()
# analisis = crud_operations.obtener_analisis()
# print(clientes)
# print(animales)
# print(analisis)
# crud_operations.crear_cliente("Nuevo", "Cliente", "Dirección", "555-1234", "Detalles adicionales")
# crud_operations.crear_animal(id_cliente=1, nombre_animal="Mascota", especie="Perro", edad=3, otra_informacion="Detalles adicionales")
# crud_operations.crear_analisis(id_animal=1, tipo_analisis="Análisis de Sangre", resultados="Normal", fecha_analisis="2023-01-01", observaciones="Detalles adicionales")
# crud_operations.cerrar_conexion()