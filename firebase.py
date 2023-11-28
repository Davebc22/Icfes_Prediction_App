# firebase.py
import firebase_admin
from firebase_admin import db, credentials

# Initialize Firebase
cred = credentials.Certificate("credential.json")
firebase_admin.initialize_app(cred, {"databaseURL" : "https://fir-tutorial1-1e305-default-rtdb.firebaseio.com/"})
ref = db.reference("/usuarios")

def update_data(nombre, sexo, resultado_modelo):
    # Crear una nueva referencia para el usuario
    user_ref = ref.push()

    # Actualizar la información del usuario, incluyendo el resultado del modelo
    user_ref.update({
        'Nombre': nombre,
        'Sexo': sexo,
        'Resultado_Modelo': resultado_modelo  # Cambiado a 'Resultado_Modelo' para distinguirlo del 'Resultado' original
    })

    # Cerrar la aplicación de Firebase cuando haya terminado
    firebase_admin.delete_app(firebase_admin.get_app())
