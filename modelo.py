import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

class Modelo:
    def __init__(self, ruta_datos):
        self.datos = pd.read_csv(ruta_datos, sep=',', low_memory=False)
        self.model = None

    import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

class Modelo:
    def __init__(self, ruta_datos):
        self.datos = pd.read_csv(ruta_datos, sep=',', low_memory=False)
        self.model = None

    def preprocesar_datos(self):
        columnas = ['ESTU_GENERACION-E',
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
                    'FAMI_SITUACIONECONOMICA']

        self.datos.drop(columnas, axis='columns', inplace=True)

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

        # Codificar columnas categóricas
        datos_codificados = pd.get_dummies(datos)

        # Definir características y etiquetas
        X = datos_codificados.drop('PUNT_GLOBAL', axis=1)
        datos_codificados['RESULTADO'] = pd.cut(datos_codificados['PUNT_GLOBAL'], bins=4,
                                                labels=['Bajo', 'Intermedio ', 'Alto', 'Sobresaliente'])
        y = datos_codificados['RESULTADO']

        # Dividir  datos en conjuntos de entrenamiento y prueba
        self.X_train, _, self.y_train, _ = train_test_split(X, y, test_size=0.4, random_state=0)

        # Crear y entrenar modelo
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(self.X_train, self.y_train)

    def predecir_nuevas_caracteristicas(self, nuevas_caracteristicas):
        if self.model is None:
            raise ValueError('Error: El modelo no ha sido entrenado. Por favor, llamar al método regresión primero')

        # Convertir listas a tuplas
        nuevas_caracteristicas = {key: tuple(value) for key, value in nuevas_caracteristicas.items()}

        # Ajustar las nuevas características para que coincidan con las columnas utilizadas durante el entrenamiento
        nuevas_caracteristicas_ajustadas = pd.get_dummies(nuevas_caracteristicas)

        # Asegurarse de que todas las columnas utilizadas durante el entrenamiento estén presentes en las nuevas características
        nuevas_caracteristicas_ajustadas = nuevas_caracteristicas_ajustadas.reindex(columns=self.X_train.columns,
                                                                                    fill_value=0)

        # Resultado de la predicción
        resultado_prediccion = self.model.predict(nuevas_caracteristicas_ajustadas)
        print(f'\nResultado de la Predicción: {resultado_prediccion[0]}')
                     fill_value=0)

        # Resultado de la predicción
        resultado_prediccion = self.model.predict(nuevas_caracteristicas_ajustadas)
        print(f'\nResultado de la Predicción: {resultado_prediccion[0]}')
