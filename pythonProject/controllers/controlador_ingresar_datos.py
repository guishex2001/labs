

from tkinter import Tk, Toplevel, Label, Entry, Button, StringVar, messagebox
from controllers.crud_operators import CRUDOperations

class ControladorIngresarDatos:
    def __init__(self, master):
        self.master = master
        self.ventana_ingreso = Toplevel(master)
        self.ventana_ingreso.title("Ingresar Datos de Cliente")

        self.nombre_var = StringVar()
        self.apellido_var = StringVar()
        self.direccion_var = StringVar()
        self.telefono_var = StringVar()
        self.detalles_var = StringVar()

        self.create_ui()

    def create_ui(self):
        # Crear etiquetas y campos de entrada
        Label(self.ventana_ingreso, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
        Entry(self.ventana_ingreso, textvariable=self.nombre_var).grid(row=0, column=1, padx=10, pady=10)

        Label(self.ventana_ingreso, text="Apellido:").grid(row=1, column=0, padx=10, pady=10)
        Entry(self.ventana_ingreso, textvariable=self.apellido_var).grid(row=1, column=1, padx=10, pady=10)

        Label(self.ventana_ingreso, text="Dirección:").grid(row=2, column=0, padx=10, pady=10)
        Entry(self.ventana_ingreso, textvariable=self.direccion_var).grid(row=2, column=1, padx=10, pady=10)

        Label(self.ventana_ingreso, text="Teléfono:").grid(row=3, column=0, padx=10, pady=10)
        Entry(self.ventana_ingreso, textvariable=self.telefono_var).grid(row=3, column=1, padx=10, pady=10)

        Label(self.ventana_ingreso, text="Detalles:").grid(row=4, column=0, padx=10, pady=10)
        Entry(self.ventana_ingreso, textvariable=self.detalles_var).grid(row=4, column=1, padx=10, pady=10)

        # Botón para ingresar datos
        Button(self.ventana_ingreso, text="Ingresar Datos", command=self.ingresar_datos).grid(row=5, column=0, columnspan=2, pady=10)

    def ingresar_datos(self):
        # Obtener datos de las variables
        nombre = self.nombre_var.get()
        apellido = self.apellido_var.get()
        direccion = self.direccion_var.get()
        telefono = self.telefono_var.get()
        detalles = self.detalles_var.get()

        # Validar que los campos no estén vacíos
        if not nombre or not apellido or not direccion or not telefono:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        # Crear instancia de CRUDOperations
        crud_operations = CRUDOperations()

        # Intentar agregar el cliente a la base de datos
        if crud_operations.crear_cliente(nombre, apellido, direccion, telefono, detalles):
            messagebox.showinfo("Éxito", "Datos ingresados correctamente.")
        else:
            messagebox.showerror("Error", "No se pudieron ingresar los datos.")

        # Cerrar la conexión con la base de datos
        crud_operations.cerrar_conexion()

if __name__ == "__main__":
    root = Tk()
    app = ControladorIngresarDatos(root)
    root.mainloop()
