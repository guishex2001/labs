import tkinter as tk
from tkinter import ttk
from controllers.controlador_ingresar_datos import ControladorIngresarDatos

class VentanaIngresarDatos(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Ingresar Datos")

        self.tipo_datos_var = tk.StringVar()
        self.tipo_datos_var.set("Cliente")  # Valor predeterminado

        # Widget de selección para elegir el tipo de datos
        self.tipo_datos_combobox = ttk.Combobox(self, values=["Cliente", "Animal", "Análisis"], textvariable=self.tipo_datos_var)
        self.tipo_datos_combobox.grid(row=0, column=0, padx=10, pady=10)

        # Botón para mostrar el formulario de ingreso de datos
        self.mostrar_formulario_button = tk.Button(self, text="Mostrar Formulario", command=self.mostrar_formulario)
        self.mostrar_formulario_button.grid(row=1, column=0, padx=10, pady=10)

    def mostrar_formulario(self):
        tipo_datos = self.tipo_datos_var.get()

        # Crear instancia del controlador de ingreso de datos con el tipo seleccionado
        controlador_ingresar_datos = ControladorIngresarDatos(self, tipo_datos)

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaIngresarDatos(root)
    app.mainloop()


