# Crear un diccionario llamado informacion_personal
informacion_personal = {
    "nombre": "Matías Sarango",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Acceder y modificar el valor asociado con la clave "ciudad"
informacion_personal["ciudad"] = "Guayaquil"  # Cambiamos la ciudad a Guayaquil

# Agregar una nueva clave-valor para representar el "telefono"
informacion_personal["telefono"] = "612345678"  # Agregamos un número de teléfono ficticio

# Verificar existencia de la clave "telefono"
if 'telefono' not in informacion_personal:
    informacion_personal['telefono'] = "612345678"  # Si no existe, se agrega (aunque ya se agregó antes)

# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal['edad']  # Eliminamos la clave "edad"

# Imprimir el diccionario final
print(informacion_personal)