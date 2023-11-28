from modelo import Modelo

# En el módulo logica
class Logica:
    def __init__(self, ruta_datos):
        # Crear una instancia del modelo
        self.modelo = Modelo(ruta_datos=ruta_datos)
        self.resultado_prediccion = None  # Aquí almacenarás el resultado de la predicción

    def entrenar_modelo(self):
        # Llamar al método de regresión para entrenar el modelo
        self.modelo.regresion()

    def predecir_nuevas_caracteristicas(self, nuevas_caracteristicas):
        # Realizar predicción con las nuevas características
        self.resultado_prediccion = self.modelo.predecir_nuevas_caracteristicas(nuevas_caracteristicas)
        return self.resultado_prediccion

    def obtener_resultado(self):
        # Devolver el resultado de la predicción
        return self.resultado_prediccion


