# InterfazInicio.py
import tkinter as tk
from firebase import update_data

class InterfazInicio(tk.Tk):
    def __init__(self, resultado=None):
        super().__init__()

        self.title("Interfaz de Inicio")
        self.geometry("400x200")

        self.resultado = resultado

        self.crear_interfaz()

    def crear_interfaz(self):
        tk.Label(self, text="Por favor, ingrese los siguientes datos:").pack()

        tk.Label(self, text="Nombre:").pack()
        entry_nombre = tk.Entry(self)
        entry_nombre.pack()

        tk.Label(self, text="Sexo:").pack()
        opciones_genero = ["Femenino", "Masculino"]
        variable_genero = tk.StringVar(self)
        variable_genero.set(opciones_genero[0])

        menu_genero = tk.OptionMenu(self, variable_genero, *opciones_genero)
        menu_genero.pack()

        button_continuar = tk.Button(self, text="Continuar", command=lambda: self.predecir_y_guardar(entry_nombre.get(), variable_genero.get()))
        button_continuar.pack()

    def predecir_y_guardar(self, nombre, genero):
        # Realizar predicción con las nuevas características
        resultado_modelo = self.resultado
        print(f"Resultado del modelo: {resultado_modelo}")

        # Guardar datos en Firebase
        update_data(nombre, genero, resultado_modelo)

        # Cerrar la ventana después de guardar los datos
        self.destroy()
