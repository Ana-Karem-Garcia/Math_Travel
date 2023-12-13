"""
Es la funcion principal del recorrido de agente y el costo que va acumulando
"""

def agente_viajero_poda(n, matriz_costo):
    #función principal, con n el número total de ciudades, matriz de costos entre ciudades
    opt_costo = None
    opt_ruta = ()
    def calcular_costo(ciudad1, ciudad2):
        return matriz_costo[ciudad1][ciudad2]

    def _av_aux(ruta, visitadas, costo_actual):
        nonlocal opt_costo, opt_ruta

        if len(ruta) == n:
            costo_actual += calcular_costo(ruta[-1], ruta[0])
            if opt_costo is None or costo_actual < opt_costo:
                opt_costo = costo_actual
                opt_ruta = ruta + (ruta[0],)
            return

        if len(ruta) == 0:
            for ciudad in range(n):
                _av_aux((ciudad,), {ciudad}, 0)
        else:
            for ciudad in range(n):
                if ciudad not in visitadas:
                    nuevo_costo = costo_actual + calcular_costo(ruta[-1], ciudad)
                    if opt_costo is None or nuevo_costo < opt_costo:
                        _av_aux(ruta + (ciudad,), visitadas.union({ciudad}), nuevo_costo)

    _av_aux((), set(), 0)

    return opt_costo, opt_ruta
