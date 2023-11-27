import firebase_admin
from firebase_admin import db, credentials

# Authenticate to Firebase
cred = credentials.Certificate("credential.json")
firebase_admin.initialize_app(cred, {"databaseURL" : "null"})

# Reference to the root node
ref = db.reference("/")

# Function to update data in the database
def update_data(nombre, sexo, resultado):
    # Creating a new reference for the data
    data_ref = ref.child("usuarios").push()

    # Update the data with simplified structure
    data_ref.update({
        'Nombre': nombre,
        'Sexo': sexo,
        'Resultado': resultado
    })

# Example usage
nombre = "Benito A. Tocamelas"
sexo = "Masculino"
resultado = "Altísimo"

# Update data in the database
update_data(nombre, sexo, resultado)

# Closing the Firebase app when done
firebase_admin.delete_app(firebase_admin.get_app())

