import tkinter as tk
from tkinter import ttk
from controllers.crud_operators import CRUDOperations

class ControladorVerDatos:
    def __init__(self, root):
        self.root = root
        self.root.title("Ver Datos")

        # Crear un árbol para mostrar los datos
        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = ("ID", "Nombre", "Apellido", "Dirección", "Teléfono", "Detalles")
        self.tree.heading("#0", text="ID")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Apellido", text="Apellido")
        self.tree.heading("Dirección", text="Dirección")
        self.tree.heading("Teléfono", text="Teléfono")
        self.tree.heading("Detalles", text="Detalles")

        self.tree.pack(expand=True, fill="both")

        # Llenar el árbol con datos
        self.llenar_datos()

    def llenar_datos(self):
        # Crear instancia de CRUDOperations
        crud_operations = CRUDOperations()

        # Obtener datos de clientes (puedes cambiar a otras entidades según sea necesario)
        clientes = crud_operations.obtener_clientes()

        # Insertar datos en el árbol
        for cliente in clientes:
            self.tree.insert("", "end", values=cliente)

        # Cerrar la conexión con la base de datos
        crud_operations.cerrar_conexion()

if __name__ == "__main__":
    root = tk.Tk()
    app = ControladorVerDatos(root)
    root.mainloop()
