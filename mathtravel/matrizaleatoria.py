"""Funcion que hace una matriz aleatoria"""

def generar_matriz(ciudades, rango_inicio=10, rango_fin=100):
    """Crea una matriz aleatoria de costos"""
    matriz = numpy.np.random.randint(rango_inicio, rango_fin, size=(ciudades, ciudades), dtype=int)
    matriz_simetrica = (matriz + matriz.T) // 2
    numpy.np.fill_diagonal(matriz_simetrica, 0)
    return matriz_simetrica
