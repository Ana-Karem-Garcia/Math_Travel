"""
Es la funcion principal del recorrido de agente y el costo que va acumulando
"""

def agente_viajero_poda(n, matriz_costo):
    #función principal, con n el número total de ciudades, matriz de costos entre ciudades
    opt_costo = None
    #almacena el mejor costo
    opt_ruta = ()
    #almacena la mejor ruta encontrada
    def calcular_costo(ciudad1, ciudad2):
        return matriz_costo[ciudad1][ciudad2]

    def _av_aux(ruta, visitadas, costo_actual):
      #ruta es una tupla que representa la ruta actual que ha sido recorrida
      #visitadas un conjunto que almacena las ciudades ya visitadas
      #costo_actual es la costo acumulada recorrida hasta ahora
      #realiza la busqueda recursiva
        nonlocal opt_costo, opt_ruta
        #no se consideran como variables locales en esta función

        if len(ruta) == n:
            # comprueba que se han visitado todas las ciudades
            costo_actual += calcular_costo(ruta[-1], ruta[0])
             #El simbolo += significa que al numero que ya esta almacenado en la variable de la izquierda, se le suma el nuevo numero que esta a la derecha del mismo
             #agregamos el costo de la ultima ciudad en la ruta de vuelta al punto de inicio
            if opt_costo is None or costo_actual < opt_costo:
                #comprueba si el costo actual es el mejor costo encontrado hasta ahora
                opt_costo = costo_actual
                #actualiza el mejor costo actual
                opt_ruta = ruta + (ruta[0],)
                #actualiza la mejor ruta agregando la ciudad del inicio al final de la ruta actual
                #ya que tenemos que formar un ciclo que regrese al punto incial
            return

        # Tratar el caso especial cuando la longitud de la ruta es cero
        if len(ruta) == 0:
            for ciudad in range(n):
                _av_aux((ciudad,), {ciudad}, 0)
        else:
            for ciudad in range(n):
              #este for recorre las ciudades en un rango de 0 a n-1
                if ciudad not in visitadas:
                  #verificamos que la ciudad actual no ha sido visitada, si ya a sido visitada se omite
                    nuevo_costo = costo_actual + calcular_costo(ruta[-1], ciudad)
                    #Calcula el costo acumulado hasta la ciudad actual, sumando el costo entre la ultima ciudad en la ruta y la ciudad actual
                    if opt_costo is None or nuevo_costo < opt_costo:
                     #comprueba si el costo calculado es el mejor que el mejor costo conocido (opt_costo)
                     #la condicion opt_costo is none maneja el caso cuando aun no se ha encontrado ninguna solucion
                        _av_aux(ruta + (ciudad,), visitadas.union({ciudad}), nuevo_costo)


    # Llamada inicial con la ciudad inicial como punto de partida
    _av_aux((), set(), 0)

    return opt_costo, opt_ruta
