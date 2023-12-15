import tkinter as tk
from tkinter import ttk
from controllers.controlador_ingresar_datos import ControladorIngresarDatos

class VentanaIngresarDatos(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Ingresar Datos")

        # Widget de selección para elegir el tipo de datos
        self.tipo_datos_label = tk.Label(self, text="Seleccionar tipo de datos:")
        self.tipo_datos_combobox = ttk.Combobox(self, values=["Cliente", "Animal", "Análisis"])
        self.tipo_datos_combobox.set("Cliente")  # Establecer el valor predeterminado
        self.tipo_datos_label.pack(pady=5)
        self.tipo_datos_combobox.pack(pady=5)

        # Botón para iniciar la entrada de datos
        self.ingresar_datos_button = tk.Button(self, text="Ingresar Datos", command=self.iniciar_ingreso_datos)
        self.ingresar_datos_button.pack(pady=10)

        self.controlador_ingresar_datos = ControladorIngresarDatos(self)

    def iniciar_ingreso_datos(self):
        tipo_datos = self.tipo_datos_combobox.get()
        self.controlador_ingresar_datos.mostrar_ventana_ingreso_datos(tipo_datos)

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaIngresarDatos(root)
    app.mainloop()


