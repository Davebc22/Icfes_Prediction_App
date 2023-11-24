import tkinter as tk

class InterfazPrediccion(tk.Tk):
    def __init__(self, nuevas_caracteristicas, callback):
        super().__init__()

        self.title("Interfaz de Predicción")
        self.geometry("800x600")

        self.nuevas_caracteristicas = nuevas_caracteristicas
        self.callback = callback

        self.crear_interfaz()

    def crear_interfaz(self):
        tk.Label(self, text="Por favor, ingrese los siguientes datos:").pack()

        frame1 = tk.Frame(self)
        frame1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        frame2 = tk.Frame(self)
        frame2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        for idx, (caracteristica, mensaje) in enumerate(self.nuevas_caracteristicas.items(), start=1):
            if idx <= 11:
                frame = frame1
            else:
                frame = frame2

            tk.Label(frame, text=f"{idx}. {mensaje}").pack()
            entry = tk.Entry(frame)
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
        resultado = self.callback(self.nuevas_caracteristicas)

        # Crear una nueva ventana para mostrar el resultado
        resultado_ventana = tk.Toplevel(self)
        resultado_ventana.title("Resultado de la Predicción")

        # Agregar un widget Label para mostrar el resultado
        resultado_label = tk.Label(resultado_ventana, text=f"El resultado de la predicción es: {resultado}")
        resultado_label.pack()

        # Agregar un botón para cerrar la ventana
        cerrar_boton = tk.Button(resultado_ventana, text="Cerrar", command=resultado_ventana.destroy)
        cerrar_boton.pack()
