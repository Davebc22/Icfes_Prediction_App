from modelo import Modelo

class Logica:
    def __init__(self, ruta_datos):
        # Crear una instancia del modelo
        self.modelo = Modelo(ruta_datos=ruta_datos)

    def entrenar_modelo(self):
        # Llamar al método de regresión para entrenar el modelo
        self.modelo.regresion()

    def predecir_nuevas_caracteristicas(self, nuevas_caracteristicas):
        # Realizar predicción con las nuevas características
        resultado_prediccion = self.modelo.predecir_nuevas_caracteristicas(nuevas_caracteristicas)
        return resultado_prediccion
