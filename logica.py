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
        self.modelo.predecir_nuevas_caracteristicas(nuevas_caracteristicas)


# Crear una instancia de Logica con la ruta de datos
logica_instancia = Logica(ruta_datos='icfes_bogota.csv')

# Entrenar el modelo
logica_instancia.entrenar_modelo()

# Nuevas características para predecir
nuevas_caracteristicas = {
    'FAMI_PERSONASHOGAR': [4],
    'FAMI_CUARTOSHOGAR': [3],
    'FAMI_EDUCACIONPADRE': [3],
    'FAMI_EDUCACIONMADRE': [5],
    'ESTU_NSE_INDIVIDUAL': [2],
    'FAMI_TIENEINTERNET': [1],
    'FAMI_TIENECOMPUTADOR': [1],
    'FAMI_TIENESERVICIOTV': [0],
    'FAMI_TIENEHORNOMICROOGAS': [1],
    'FAMI_TIENEAUTOMOVIL': [0],
    'FAMI_TIENECONSOLAVIDEOJUEGOS': [1],
    'FAMI_TIENEMOTOCICLETA': [0],
    'FAMI_COMELECHEDERIVADOS': [1],
    'FAMI_COMECARNEPESCADOHUEVO': [1],
    'FAMI_COMECEREALFRUTOSLEGUMBRE': [1],
    'ESTU_DEDICACIONLECTURADIARIA': [2],
    'ESTU_DEDICACIONINTERNET': [1],
    'ESTU_HORASSEMANATRABAJA': [5],
    'COLE_CARACTER': [0],
    'COLE_AREA_UBICACION': [1],
    'COLE_JORNADA': [1],
    'EDAD': [16]
}

# Realizar predicción con las nuevas características
logica_instancia.predecir_nuevas_caracteristicas(nuevas_caracteristicas) # Está imprimiendo el resultado de todos los parámetros pero solo necesitamos 1
