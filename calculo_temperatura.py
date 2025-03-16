def calcular_temperatura_promedio(datos_temperatura):
    """
    Calcula la temperatura promedio de cada ciudad en un período de tiempo.

    :param datos_temperatura: ciudades y listas de temperaturas semanales.
    :return: la temperatura promedio de cada ciudad.
    """
    promedios = {}

    for ciudad, temperaturas in datos_temperatura.items():
        promedio = sum(temperaturas) / len(temperaturas)
        promedios[ciudad] = promedio

    return promedios


# Datos de ejemplo: 3 ciudades con temperaturas registradas durante 4 semanas
datos_temperatura = {
    "GUAYAQUIL": [30, 32, 29, 31],
    "SANTO DOMINGO": [25, 26, 27, 26],
    "QUITO": [20, 22, 21, 23]
}

# Calcular temperaturas promedio
resultado = calcular_temperatura_promedio(datos_temperatura)
print("Temperaturas promedio por ciudad:", resultado)
