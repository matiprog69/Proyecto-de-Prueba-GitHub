# calculo_descuento.py

def calcular_descuento(monto_total, porcentaje_descuento=15):
    """
    Esta función calcula el descuento basado en el monto total y el porcentaje de descuento.
    
    Parámetros:
    monto_total: El monto total de la compra.
    porcentaje_descuento: El porcentaje de descuento a aplicar (por defecto 1%).
    
    Retorna:
    El monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamada a la función con solo el monto total
monto_1 = 500
descuento_1 = calcular_descuento(monto_1)
monto_final_1 = monto_1 - descuento_1
print(f"Compra de {monto_1}, Descuento: {descuento_1}, Monto final: {monto_final_1}")

# Llamada a la función con el monto total y un porcentaje de descuento específico
monto_2 = 800
descuento_2 = calcular_descuento(monto_2, 15)  # Aplicando un 15% de descuento
monto_final_2 = monto_2 - descuento_2
print(f"Compra de {monto_2}, Descuento: {descuento_2}, Monto final: {monto_final_2}")

