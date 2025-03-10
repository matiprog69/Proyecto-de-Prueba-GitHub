# Definir las ciudades y los días de la semana
ciudades = ['Esmeraldas', 'Guayaquil', 'Manabí']
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = 4

# Inicializar la matriz 3D con temperaturas dadas
temperaturas = [
    [[30] * 7, [31] * 7, [33] * 7, [25] * 7],  # Esmeraldas
    [[35] * 7, [27] * 7, [28] * 7, [29] * 7],  # Guayaquil
    [[28] * 7, [29] * 7, [24] * 7, [32] * 7]   # Manabí
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad_idx, ciudad in enumerate(ciudades):
    print(f"\nPromedios de temperaturas para {ciudad}:")
    for semana in range(semanas):
        # Extraer las temperaturas para la ciudad y semana específicas
        temperaturas_semana = temperaturas[ciudad_idx][semana]
        
        # Calcular el promedio de temperaturas para la semana
        promedio_semana = sum(temperaturas_semana) / len(temperaturas_semana)
        
        print(f"Semana {semana+1}: {promedio_semana:.2f}°C")