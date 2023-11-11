import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

class ProcesadorDatos:
    def __init__(self, ruta_datos):
        self.datos = pd.read_csv(ruta_datos, sep=',', low_memory=False)
        self.model = None  # Inicializar el modelo en None

    def preprocesar_datos(self):
        columnas = {'ESTU_GENERACION-E',
                    'COLE_MCPIO_UBICACION',
                    'COLE_DEPTO_UBICACION',
                    'ESTU_MCPIO_PRESENTACION',
                    'ESTU_DEPTO_PRESENTACION',
                    'ESTU_TIPOREMUNERACION',
                    'ESTU_NACIONALIDAD',
                    'ESTU_PAIS_RESIDE',
                    'ESTU_DEPTO_RESIDE',
                    'ESTU_MCPIO_RESIDE',
                    'FAMI_ESTRATOVIVIENDA',
                    'FAMI_TRABAJOLABORPADRE',
                    'FAMI_TRABAJOLABORMADRE',
                    'FAMI_TIENELAVADORA',
                    'FAMI_NUMLIBROS',
                    'FAMI_SITUACIONECONOMICA'}

        self.datos.drop(columnas, axis=1, inplace=True)

    def regresion(self):
        columnas = ['FAMI_PERSONASHOGAR',
                    'FAMI_CUARTOSHOGAR',
                    'FAMI_EDUCACIONPADRE',
                    'FAMI_EDUCACIONMADRE',
                    'ESTU_NSE_INDIVIDUAL',
                    'FAMI_TIENEINTERNET',
                    'FAMI_TIENECOMPUTADOR',
                    'FAMI_TIENESERVICIOTV',
                    'FAMI_TIENEHORNOMICROOGAS',
                    'FAMI_TIENEAUTOMOVIL',
                    'FAMI_TIENECONSOLAVIDEOJUEGOS',
                    'FAMI_TIENEMOTOCICLETA',
                    'FAMI_COMELECHEDERIVADOS',
                    'FAMI_COMECARNEPESCADOHUEVO',
                    'FAMI_COMECEREALFRUTOSLEGUMBRE',
                    'ESTU_DEDICACIONLECTURADIARIA',
                    'ESTU_DEDICACIONINTERNET',
                    'ESTU_HORASSEMANATRABAJA',
                    'COLE_CARACTER',
                    'COLE_AREA_UBICACION',
                    'COLE_JORNADA',
                    'EDAD']

        datos = self.datos[(self.datos['EDAD'] >= 10) & (self.datos['EDAD'] <= 90)]

        # Codifica tus columnas categóricas
        datos_codificados = pd.get_dummies(datos)

        # Define tus características y etiquetas
        X = datos_codificados.drop('PUNT_GLOBAL', axis=1)
        datos_codificados['RESULTADO'] = pd.cut(datos_codificados['PUNT_GLOBAL'], bins=4,
                                                labels=['Bajo', 'Intermedio ', 'Alto', 'Sobresaliente'])
        y = datos_codificados['RESULTADO']

        # Divide tus datos en conjuntos de entrenamiento y prueba
        self.X_train, _, self.y_train, _ = train_test_split(X, y, test_size=0.4, random_state=0)

        # Crea y entrena tu modelo
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(self.X_train, self.y_train)

    def predecir_nuevas_caracteristicas(self, nuevas_caracteristicas):
        if self.model is None:
            print("Error: El modelo no ha sido entrenado. Por favor, llame al método 'regresion' primero.")
            return

        # Ajustar las nuevas características para que coincidan con las columnas utilizadas durante el entrenamiento
        nuevas_caracteristicas_ajustadas = pd.get_dummies(nuevas_caracteristicas)

        # Asegurarse de que todas las columnas utilizadas durante el entrenamiento estén presentes en las nuevas características
        nuevas_caracteristicas_ajustadas = nuevas_caracteristicas_ajustadas.reindex(columns=self.X_train.columns, fill_value=0)

        # Resultado de la predicción
        resultado_prediccion = self.model.predict(nuevas_caracteristicas_ajustadas)
        print(f'\nResultado de la Predicción: {resultado_prediccion}')


# PUREBA DEL MODELO

# Ruta de los datos
ruta_datos = 'icfes_bogota.csv'

# Instanciar el procesador de datos
procesador = ProcesadorDatos(ruta_datos)

# Cargar y preprocesar datos
procesador.preprocesar_datos()

# Llamar al método regresion y realizar una nueva predicción
procesador.regresion()




# Nueva predicción
nuevas_caracteristicas = pd.DataFrame({
'FAMI_PERSONASHOGAR': [4],
'FAMI_CUARTOSHOGAR': [3],
'FAMI_EDUCACIONPADRE': [3],  # Por ejemplo, supongamos que el padre tiene educación técnica
'FAMI_EDUCACIONMADRE': [5],  # Por ejemplo, supongamos que la madre tiene educación de posgrado
'ESTU_NSE_INDIVIDUAL': [2],  # Por ejemplo, supongamos que el estudiante tiene un NSE medio
'FAMI_TIENEINTERNET': [1],  # Por ejemplo, supongamos que la familia tiene acceso a Internet
'FAMI_TIENECOMPUTADOR': [1],  # Por ejemplo, supongamos que la familia tiene computadora
'FAMI_TIENESERVICIOTV': [0],  # Por ejemplo, supongamos que la familia no tiene servicio de TV
'FAMI_TIENEHORNOMICROOGAS': [1],  # Por ejemplo, supongamos que la familia tiene horno microondas
'FAMI_TIENEAUTOMOVIL': [0],  # Por ejemplo, supongamos que la familia no tiene automóvil
'FAMI_TIENECONSOLAVIDEOJUEGOS': [1],  # Por ejemplo, supongamos que la familia tiene consola de videojuegos
'FAMI_TIENEMOTOCICLETA': [0],  # Por ejemplo, supongamos que la familia no tiene motocicleta
'FAMI_COMELECHEDERIVADOS': [1],  # Por ejemplo, supongamos que la familia consume productos lácteos
'FAMI_COMECARNEPESCADOHUEVO': [1],  # Por ejemplo, supongamos que la familia consume carne, pescado y huevos
'FAMI_COMECEREALFRUTOSLEGUMBRE': [1],
# Por ejemplo, supongamos que la familia consume cereales, frutas y legumbres
'ESTU_DEDICACIONLECTURADIARIA': [2],
    # Por ejemplo, supongamos que el estudiante dedica 2 horas diarias a la lectura
'ESTU_DEDICACIONINTERNET': [1],  # Por ejemplo, supongamos que el estudiante dedica 1 hora diaria a Internet
'ESTU_HORASSEMANATRABAJA': [5],  # Por ejemplo, supongamos que el estudiante trabaja 5 horas a la semana
'COLE_CARACTER': [0],  # Por ejemplo, supongamos que el colegio es de carácter oficial
'COLE_AREA_UBICACION': [1],  # Por ejemplo, supongamos que el colegio está ubicado en área urbana
'COLE_JORNADA': [1],  # Por ejemplo, supongamos que el colegio tiene jornada de tarde
'EDAD': [16],  # Por ejemplo, supongamos que el estudiante tiene 16 años
})
# Predecir con nuevas características
procesador.predecir_nuevas_caracteristicas(nuevas_caracteristicas)




