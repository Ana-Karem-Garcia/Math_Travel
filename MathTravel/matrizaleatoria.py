import numpy as np

"""
Función para crear una matriz aleatoria de costos

"""

def generar_matriz(ciudades, rango_inicio=10, rango_fin=100):
    # Generar una matriz aleatoria cuadrada de enteros
    matriz = np.random.randint(rango_inicio, rango_fin, size=(ciudades, ciudades), dtype=int)

    # Hacer la matriz simétrica
    matriz_simetrica = (matriz + matriz.T) // 2

    # Establecer ceros en la diagonal
    np.fill_diagonal(matriz_simetrica, 0)

    return matriz_simetrica
