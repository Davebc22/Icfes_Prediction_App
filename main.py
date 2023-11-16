from logica import Logica

# Nuevas características para predecir
# Nuevas características para predecir
nuevas_caracteristicas = {
    'FAMI_PERSONASHOGAR': 'Ingrese el número de personas en el hogar: ',
    'FAMI_CUARTOSHOGAR': 'Ingrese el número de cuartos en el hogar: ' ,
    'FAMI_EDUCACIONPADRE': 'Ingrese el nivel de educación del padre (1-5): ' ,
    'FAMI_EDUCACIONMADRE': 'Ingrese el nivel de educación de la madre (1-5): ' ,
    'ESTU_NSE_INDIVIDUAL': 'Ingrese el NSE individual (1-5): ' ,
    'FAMI_TIENEINTERNET': '¿Tiene acceso a Internet? Ingrese 1 si sí, 0 si no: ' ,
    'FAMI_TIENECOMPUTADOR': '¿Tiene computador en casa? Ingrese 1 si sí, 0 si no: ' ,
    'FAMI_TIENESERVICIOTV': '¿Tiene servicio de TV? Ingrese 1 si sí, 0 si no: ' ,
    'FAMI_TIENEHORNOMICROOGAS': '¿Tiene horno microondas o gas? Ingrese 1 si sí, 0 si no: ' ,
    'FAMI_TIENEAUTOMOVIL': '¿Tiene automóvil? Ingrese 1 si sí, 0 si no: ' ,
    'FAMI_TIENECONSOLAVIDEOJUEGOS': '¿Tiene consola de videojuegos? Ingrese 1 si sí, 0 si no: ' ,
    'FAMI_TIENEMOTOCICLETA': '¿Tiene motocicleta? Ingrese 1 si sí, 0 si no: ' ,
    'FAMI_COMELECHEDERIVADOS': '¿Consume productos lácteos? Ingrese 1 si sí, 0 si no: ' ,
    'FAMI_COMECARNEPESCADOHUEVO': '¿Consume carne, pescado o huevos? Ingrese 1 si sí, 0 si no: ' ,
    'FAMI_COMECEREALFRUTOSLEGUMBRE': '¿Consume cereales, frutas o legumbres? Ingrese 1 si sí, 0 si no: ' ,
    'ESTU_DEDICACIONLECTURADIARIA': 'Ingrese la dedicación diaria a la lectura (1-5): ' ,
    'ESTU_DEDICACIONINTERNET': 'Ingrese la dedicación diaria a Internet (1-5): ' ,
    'ESTU_HORASSEMANATRABAJA': 'Ingrese las horas semanales de trabajo: ' ,
    'COLE_CARACTER': 'Ingrese el carácter de la institución educativa (1-5): ' ,
    'COLE_AREA_UBICACION': 'Ingrese el área de ubicación de la institución educativa (1-5): ' ,
    'COLE_JORNADA': 'Ingrese la jornada de la institución educativa (1-5): ' ,
    'EDAD': 'Ingrese la edad: '
}


# Crear una instancia de Logica con la ruta de datos
logica_instancia = Logica(ruta_datos='icfes_bogota.csv')

# Entrenar el modelo
logica_instancia.entrenar_modelo()

# Solicitar valores para las nuevas características
for caracteristica, mensaje in nuevas_caracteristicas.items():
    valor = input(mensaje)
    while not valor.isdigit():
        print("Por favor, ingrese un valor numérico.")
        valor = input(mensaje)
    nuevas_caracteristicas[caracteristica] = (int(valor),)

# Realizar predicción con las nuevas características
logica_instancia.predecir_nuevas_caracteristicas(nuevas_caracteristicas)