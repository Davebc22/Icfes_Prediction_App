import tkinter as tk

class InterfazPrediccion(tk.Tk):
    def __init__(self, logica, nuevas_caracteristicas, callback):
        super().__init__()

        self.title("Interfaz de Predicción")
        self.geometry("900x600")

        self.logica = logica
        self.nuevas_caracteristicas = nuevas_caracteristicas
        self.callback = callback

        self.crear_interfaz()

    def crear_interfaz(self):
        tk.Label(self, text="Por favor, ingrese los siguientes datos:").pack()

        frame1 = tk.Frame(self)
        frame1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        frame2 = tk.Frame(self)
        frame2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        opciones_valores = {
            'Trabajo del padre': ['Trabajo Autónomo, Empresarial o Administrativo',
                                  'Trabaja en el hogar, es pensionado, no trabaja o estudia',
                                  'Empresario o Gerencial / Otras Ocupaciones', 'Trabajo Profesional',
                                  'No sabe / No aplica'],
            'Nivel de educación del padre': ['Educación Primaria', 'Educación Secundaria',
                                             'Educación Profesional o superior', 'Educación Técnica o Tecnológica',
                                             'Ninguno, no aplica o no sabe'],
            'Trabajo de la madre': ['Trabajo Autónomo, Empresarial o Administrativo',
                                    'Trabaja en el hogar, es pensionado, no trabaja o estudia',
                                    'Empresario o Gerencial / Otras Ocupaciones', 'Trabajo Profesional',
                                    'No sabe / No aplica'],
            'Nivel de educación de la madre': ['Educación Primaria', 'Educación Secundaria',
                                               'Educación Profesional o superior', 'Educación Técnica o Tecnológica',
                                               'Ninguno, no aplica o no sabe'],
            'Cuántos cuartos tiene en el hogar': ['1', '2', '3', '4', '5', '6'],
            'Dedicación a la lectura diaria': ['30 minutos o menos', 'Entre 30 y 60 minutos', 'Entre 1 y 2 horas',
                                               'Más de 2 horas', 'No leo por entretenimiento'],
            'Tiempo dedicado en internet': ['30 minutos o menos', 'Entre 30 y 60 minutos', 'Entre 1 y 3 horas',
                                            'Más de 3 horas', 'No Navega Internet'],
            'Número de personas en el hogar': ['1 a 2', '3 a 4', '5 a 6', '7 a 8', '9 o más'],
            'Estrato de la vivienda': ['1', '2', '3', '4', '5', '6'],
            'Frecuencia con la que consume carne, pescado o huevo': ['Nunca o rara vez comemos eso',
                                                                     '1 o 2 veces por semana', '3 a 5 veces por semana',
                                                                     'Todos o casi todos los días'],
            'Frecuencia con la que consume leche o derivados': ['Nunca o rara vez comemos eso',
                                                                '1 o 2 veces por semana', '3 a 5 veces por semana',
                                                                'Todos o casi todos los días'],
            'Tiene consola de videojuegos': ['Si', 'No'],
            'Cual considera que es su nivel de inglés': ['A-', 'A1', 'A2', 'B1', 'B+'],
            'Género': ['Masculino', 'Femenino'],
            'Número de libros en el hogar': ['0 A 10 LIBROS', '11 A 25 LIBROS', '26 A 100 LIBROS', 'MÁS DE 100 LIBROS']
        }

        for idx, (caracteristica, mensaje) in enumerate(self.nuevas_caracteristicas.items(), start=1):
            if idx <= 11:
                frame = frame1
            else:
                frame = frame2

            tk.Label(frame, text=f"{idx}. {mensaje}").pack()

            # Revisar si la característica debe ser una lista desplegable
            if caracteristica in opciones_valores:
                valores_opcion = opciones_valores[caracteristica]
                variable_opcion = tk.StringVar(self)
                variable_opcion.set(valores_opcion[0])
                lista_desplegable = tk.OptionMenu(frame, variable_opcion, *valores_opcion)
                lista_desplegable.pack()
                self.nuevas_caracteristicas[caracteristica] = variable_opcion
            else:
                entry = tk.Entry(frame)
                entry.pack()
                self.nuevas_caracteristicas[caracteristica] = entry

        button = tk.Button(self, text="Realizar Predicción", command=self.obtener_valores)
        button.pack()

    def obtener_valores(self):
        respuestas = {}

        for caracteristica, valor in self.nuevas_caracteristicas.items():
            if isinstance(valor, tk.StringVar):
                respuestas[caracteristica] = valor.get()
            elif isinstance(valor, tk.Entry):
                respuestas[caracteristica] = valor.get()

        # Imprimir el DataFrame (puedes comentar esta línea si no quieres imprimirlo)
        print("Respuestas guardadas en DataFrame:")

        # Llamar a la función de devolución de llamada con los valores recopilados
        resultado = self.callback(respuestas)

        # Crear una nueva ventana para mostrar el resultado
        resultado_ventana = tk.Toplevel(self)
        resultado_ventana.title("Resultado de la Predicción")

        # Agregar un widget Label para mostrar el resultado
        resultado_label = tk.Label(resultado_ventana, text=f"El resultado de la predicción es: {resultado}")
        resultado_label.pack()

        # Agregar un botón para cerrar la ventana
        cerrar_boton = tk.Button(resultado_ventana, text="Cerrar", command=resultado_ventana.destroy)
        cerrar_boton.pack()
