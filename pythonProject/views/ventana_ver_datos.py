import tkinter as tk
from tkinter import ttk
#from controllers.controlador_ver_datos import ControladorVerDatos
class VentanaVerDatos(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        # Aquí puedes agregar widgets y elementos de interfaz para mostrar datos.
        label = tk.Label(self, text="Ventana Ver Datos")
        label.pack()

        # Puedes agregar tablas, listas o cualquier otro widget necesario.

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaVerDatos(root)
    app.mainloop()
