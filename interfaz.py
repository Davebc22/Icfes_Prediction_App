import tkinter as tk

class InterfazPrediccion(tk.Tk):
    def __init__(self, nuevas_caracteristicas, callback):
        super().__init__()

        self.title("Interfaz de Predicción")
        self.geometry("400x400")

        self.nuevas_caracteristicas = nuevas_caracteristicas
        self.callback = callback

        self.crear_interfaz()

    def crear_interfaz(self):
        tk.Label(self, text="Por favor, ingrese los siguientes datos:").pack()

        for idx, (caracteristica, mensaje) in enumerate(self.nuevas_caracteristicas.items(), start=1):
            tk.Label(self, text=f"{idx}. {mensaje}").pack()

            entry = tk.Entry(self)
            entry.pack()

            self.nuevas_caracteristicas[caracteristica] = entry

        button = tk.Button(self, text="Realizar Predicción", command=self.obtener_valores)
        button.pack()

    def obtener_valores(self):
        for caracteristica, entry in self.nuevas_caracteristicas.items():
            valor = entry.get()
            while not valor.isdigit():
                print("Por favor, ingrese un valor numérico.")
                valor = entry.get()
            self.nuevas_caracteristicas[caracteristica] = (int(valor),)

        # Llamar a la función de devolución de llamada con los valores recopilados
        self.callback(self.nuevas_caracteristicas)

        self.destroy()  # Cerrar la interfaz después de obtener los valores


