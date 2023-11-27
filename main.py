from logica import Logica
from interfaz import InterfazPrediccion

# Crear una instancia de Logica con la ruta de datos
logica_instancia = Logica(ruta_datos='icfes_bogota.csv')

# Entrenar el modelo
logica_instancia.entrenar_modelo()

def callback(valores):
    # Definir resultado_prediccion
    resultado_prediccion = logica_instancia.predecir_nuevas_caracteristicas(valores)
    print(f"Resultado en callback: {resultado_prediccion}")
    return resultado_prediccion


# Crea una instancia de la interfaz y pasa la lógica y la función de devolución de llamada
nuevas_caracteristicas = {'Trabajo del padre': 'Ingrese el trabajo del padre:',
                          'Nivel de educación del padre': 'Ingrese el nivel de educación del padre:',
                          'Trabajo de la madre' : 'Ingrese el trabajo de la madre:',
                          'Nivel de educación de la madre' : 'Ingrese el nivel de educación de la madre:',
                          'Cuántos cuartos tiene en el hogar': 'Ingrese el número de cuartos en el hogar:',
                          'Dedicación a la lectura diaria': 'Ingrese la dedicación diaria a la lectura:',
                          'Tiempo dedicado en internet': 'Ingrese el tiempo dedicado en internet:',
                          'Número de personas en el hogar': 'Ingrese el número de personas en el hogar:',
                          'EDAD': 'Ingrese la edad: ',
                          'Estrato de la vivienda': 'Ingrese el estrato de la vivienda:',
                          'Frecuencia con la que consume carne, pescado o huevo': 'Ingrese la frecuencia con la que consume carne, pescado o huevo:',
                          'Frecuencia con la que consume leche o derivados' : 'Ingrese la frecuencia con la que consume leche o derivados:',
                          'Tiene consola de videojuegos' : 'Ingrese si tiene consola de videojuegos:',
                          'Cual considera que es su nivel de inglés' : 'Ingrese el nivel de inglés que considera que tiene:',
                          'Género' : 'Ingrese su género:',
                          'Número de libros en el hogar' : 'Ingrese el número de libros en el hogar:'
                          # Agrega más características según sea necesario
}

app = InterfazPrediccion(logica_instancia, nuevas_caracteristicas, callback)
app.mainloop()