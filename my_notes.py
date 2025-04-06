# Escritura de Archivo de Texto
# Crear un archivo llamado my_notes.txt y escribir tres líneas de notas personales.
file_name = 'my_notes.txt'
notes = [
    "estudiante de tecnologia de la información en la UEA.\n",
    "Me gustan las matemáticas.\n",
    "Me gustaria estudiar veterinaria.\n"
]

# Abrir el archivo en modo escritura ('w') y escribir las líneas
with open(file_name, 'w') as file:
    for note in notes:
        file.write(note)
print(f"Archivo '{file_name}' creado y se han escrito las notas.")

# Lectura de Archivo de Texto
# Abrir el archivo en modo lectura ('r') y leerlo línea por línea
with open(file_name, 'r') as file:
    lines = file.readlines()

print("Contenido del archivo leído línea por línea:")
for line in lines:
    print(line.strip())

# El cierre del archivo está garantizado automáticamente al usar 'with'.