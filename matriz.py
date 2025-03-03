def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f"Valor encontrado en la posición ({i+1}, {j+1})"
    return "Valor no encontrado"

# Matriz de ejemplo
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

valor_a_buscar = 5

print(f"Matriz original:\n{matriz}")
print(buscar_valor(matriz, valor_a_buscar))