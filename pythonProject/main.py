import tkinter as tk
from tkinter import ttk
from views.ventana_ver_datos import VentanaVerDatos
from views.ventana_ingresar_datos import VentanaIngresarDatos

class VentanaMain:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Laboratorio Veterinario")

        # Crear pestañas
        self.tabControl = ttk.Notebook(root)

        # Pestaña Ver Datos
        self.tab_ver_datos = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab_ver_datos, text="Ver Datos")
        VentanaVerDatos(self.tab_ver_datos)  # Debes implementar VentanaVerDatos

        # Pestaña Ingresar Datos
        self.tab_ingresar_datos = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab_ingresar_datos, text="Ingresar Datos")
        VentanaIngresarDatos(self.tab_ingresar_datos)  # Debes implementar VentanaIngresarDatos

        self.tabControl.pack(expand=1, fill="both")

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaMain(root)
    root.mainloop()