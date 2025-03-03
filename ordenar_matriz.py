def ordenar_fila(matriz, fila):
    matriz[fila] = sorted(matriz[fila])
    return matriz

# Matriz de ejemplo
matriz = [
    [3, 2, 1],
    [4, 5, 6],
    [9, 8, 7]
]

fila_a_ordenar = 0

print(f"Matriz original:\n{matriz}")
matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)
print(f"Matriz con la fila {fila_a_ordenar+1} ordenada:\n{matriz_ordenada}")