import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

class Modelo:
    def __init__(self, ruta_datos):
        self.datos = pd.read_csv(ruta_datos, sep=',', low_memory=False)
        self.model = None
        self.X_train = None
        self.y_train = None

    def regresion(self):
        columnas_a_mantener = ['Trabajo del padre', 'Nivel de educación del padre',
    'Trabajo de la madre', 'Nivel de educación de la madre', 'Cuántos cuartos tiene en el hogar',
    'Dedicación a la lectura diaria', 'Tiempo dedicado en internet', 'Número de personas en el hogar',
    'Estrato de la vivienda', 'Frecuencia con la que consume carne, pescado o huevo',
    'Frecuencia con la que consume leche o derivados','Tiene consola de videojuegos',
    'Cual considera que es su nivel de inglés','Género','Número de libros en el hogar',
    'PUNT_GLOBAL']


        # Codificar columnas categóricas
        datos_codificados = pd.get_dummies(self.datos)

        # Definir características y etiquetas
        X = datos_codificados.drop('PUNT_GLOBAL', axis=1)
        y = pd.cut(datos_codificados['PUNT_GLOBAL'], bins=3, labels=['Bajo', 'Alto', 'Sobresaliente'])

        # Dividir datos en conjuntos de entrenamiento y prueba
        self.X_train, _, self.y_train, _ = train_test_split(X, y, test_size=0.4, random_state=0)

        # Crear y entrenar modelo
        self.model = RandomForestClassifier(max_depth = None, min_samples_leaf = 4, min_samples_split = 10, n_estimators = 100)
        self.model.fit(self.X_train, self.y_train)

    def predecir_nuevas_caracteristicas(self, nuevas_caracteristicas):
        if self.model is None:
            raise ValueError('Error: El modelo no ha sido entrenado. Por favor, llamar al método regresión primero')

        # Convertir las nuevas características en un DataFrame
        df_nuevas_caracteristicas = pd.DataFrame([nuevas_caracteristicas])

        # Aplicar codificación one-hot a las nuevas características
        df_nuevas_codificadas = pd.get_dummies(df_nuevas_caracteristicas)

        # Obtener la lista de columnas utilizadas durante el entrenamiento
        columnas_entrenamiento = self.X_train.columns.tolist()

        # Reindexar el DataFrame resultante con las columnas de entrenamiento y llenar con ceros las columnas faltantes
        df_nuevas_codificadas = df_nuevas_codificadas.reindex(columns=columnas_entrenamiento, fill_value=0)

        # Realizar la predicción con el modelo
        resultado_prediccion = self.model.predict(df_nuevas_codificadas)
        print(f'Tus resultados serán: {resultado_prediccion[0]}')
        return resultado_prediccion[0]