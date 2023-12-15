
from tkinter import ttk
from controllers.controlador_ingresar_datos import ControladorIngresarDatos
import tkinter as tk

class VentanaIngresarDatos(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Ingresar Datos")  # Establecer el título en la ventana secundaria

        self.controlador_ingresar_datos = ControladorIngresarDatos(self)   # Línea corregida

        self.tipo_dato = tk.StringVar()
        self.tipo_dato.set("Cliente")  # Valor predeterminado

        label_tipo_dato = tk.Label(self, text="Seleccione el tipo de dato:")  # Corrección aquí
        label_tipo_dato.pack()

        opciones_tipo_dato = ["Cliente", "Animal", "Análisis"]
        menu_tipo_dato = ttk.Combobox(self, textvariable=self.tipo_dato, values=opciones_tipo_dato)  # Corrección aquí
        menu_tipo_dato.pack()

        self.frame_cliente = FrameCliente(self)  # Corrección aquí
        self.frame_animal = FrameAnimal(self)  # Corrección aquí
        self.frame_analisis = FrameAnalisis(self)  # Corrección aquí

        # Botón para mostrar el formulario respectivo
        btn_mostrar_formulario = tk.Button(self, text="Mostrar Formulario", command=self.mostrar_formulario)  # Corrección aquí
        btn_mostrar_formulario.pack()

    # Resto del código sin cambios


    def mostrar_formulario(self):
        if self.tipo_dato.get() == "Cliente":
            self.frame_cliente.mostrar()
            self.frame_animal.ocultar()
            self.frame_analisis.ocultar()
        elif self.tipo_dato.get() == "Animal":
            self.frame_cliente.ocultar()
            self.frame_animal.mostrar()
            self.frame_analisis.ocultar()
        elif self.tipo_dato.get() == "Análisis":
            self.frame_cliente.ocultar()
            self.frame_animal.ocultar()
            self.frame_analisis.mostrar()


class FormularioBase:
    def __init__(self, master, titulo):
        self.master = master
        self.frame = tk.Toplevel(master)
        self.frame.title(titulo)
        self.frame.withdraw()  # Ocultar el frame al inicio

        # Crear etiquetas y campos de entrada para datos
        # Ejemplo: self.label_nombre = tk.Label(self.frame, text="Nombre:")
        #          self.label_nombre.grid(row=0, column=0, padx=10, pady=10)
        #          self.entry_nombre = tk.Entry(self.frame)
        #          self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        # Agrega más etiquetas y campos según tus necesidades

    def mostrar(self):
        self.frame.deiconify()  # Mostrar el frame

    def ocultar(self):
        self.frame.withdraw()  # Ocultar el frame


# En la clase FrameCliente
class FrameCliente(FormularioBase):
    def __init__(self, master):
        super().__init__(master, "Formulario Cliente")

        self.label_nombre = tk.Label(self.frame, text="Nombre:")
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)
        self.entry_nombre = tk.Entry(self.frame)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        self.label_apellido = tk.Label(self.frame, text="Apellido:")
        self.label_apellido.grid(row=1, column=0, padx=10, pady=10)
        self.entry_apellido = tk.Entry(self.frame)
        self.entry_apellido.grid(row=1, column=1, padx=10, pady=10)

        self.label_direccion = tk.Label(self.frame, text="Dirección:")
        self.label_direccion.grid(row=2, column=0, padx=10, pady=10)
        self.entry_direccion = tk.Entry(self.frame)
        self.entry_direccion.grid(row=2, column=1, padx=10, pady=10)

        self.label_telefono = tk.Label(self.frame, text="Teléfono:")
        self.label_telefono.grid(row=3, column=0, padx=10, pady=10)
        self.entry_telefono = tk.Entry(self.frame)
        self.entry_telefono.grid(row=3, column=1, padx=10, pady=10)

        self.label_detalles = tk.Label(self.frame, text="Otros Detalles:")
        self.label_detalles.grid(row=4, column=0, padx=10, pady=10)
        self.entry_detalles = tk.Entry(self.frame)
        self.entry_detalles.grid(row=4, column=1, padx=10, pady=10)

        # Agrega más campos según la estructura de la base de datos


# En la clase FrameAnimal
class FrameAnimal(FormularioBase):
    def __init__(self, master):
        super().__init__(master, "Formulario Animal")

        self.label_nombre_animal = tk.Label(self.frame, text="Nombre del Animal:")
        self.label_nombre_animal.grid(row=0, column=0, padx=10, pady=10)
        self.entry_nombre_animal = tk.Entry(self.frame)
        self.entry_nombre_animal.grid(row=0, column=1, padx=10, pady=10)

        self.label_especie = tk.Label(self.frame, text="Especie:")
        self.label_especie.grid(row=1, column=0, padx=10, pady=10)
        self.entry_especie = tk.Entry(self.frame)
        self.entry_especie.grid(row=1, column=1, padx=10, pady=10)

        self.label_edad = tk.Label(self.frame, text="Edad:")
        self.label_edad.grid(row=2, column=0, padx=10, pady=10)
        self.entry_edad = tk.Entry(self.frame)
        self.entry_edad.grid(row=2, column=1, padx=10, pady=10)

        self.label_otra_informacion_animal = tk.Label(self.frame, text="Otra Información:")
        self.label_otra_informacion_animal.grid(row=3, column=0, padx=10, pady=10)
        self.entry_otra_informacion_animal = tk.Entry(self.frame)
        self.entry_otra_informacion_animal.grid(row=3, column=1, padx=10, pady=10)

        # Agrega más campos según la estructura de la base de datos


# En la clase FrameAnalisis
class FrameAnalisis(FormularioBase):
    def __init__(self, master):
        super().__init__(master, "Formulario Análisis")

        self.label_tipo_analisis = tk.Label(self.frame, text="Tipo de Análisis:")
        self.label_tipo_analisis.grid(row=0, column=0, padx=10, pady=10)
        self.entry_tipo_analisis = tk.Entry(self.frame)
        self.entry_tipo_analisis.grid(row=0, column=1, padx=10, pady=10)

        self.label_resultados = tk.Label(self.frame, text="Resultados:")
        self.label_resultados.grid(row=1, column=0, padx=10, pady=10)
        self.entry_resultados = tk.Entry(self.frame)
        self.entry_resultados.grid(row=1, column=1, padx=10, pady=10)

        self.label_fecha_analisis = tk.Label(self.frame, text="Fecha del Análisis:")
        self.label_fecha_analisis.grid(row=2, column=0, padx=10, pady=10)
        self.entry_fecha_analisis = tk.Entry(self.frame)
        self.entry_fecha_analisis.grid(row=2, column=1, padx=10, pady=10)

        self.label_observaciones = tk.Label(self.frame, text="Observaciones:")
        self.label_observaciones.grid(row=3, column=0, padx=10, pady=10)
        self.entry_observaciones = tk.Entry(self.frame)
        self.entry_observaciones.grid(row=3, column=1, padx=10, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaIngresarDatos(root)
    root.mainloop()
