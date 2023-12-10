# Math_Travel
Proyecto de python en la LiMA donde se resuleve el problema del agente viajero.

##
## ¿Qué hace nuestro proyecto?
Responde a la siguiente pregunta: dada una lista de ciudades y los costos entre cada par de ellas, ¿cuál es la ruta más corta posible que visita cada ciudad exactamente una vez y al finalizar regresa a la ciudad origen?. El problema fue formulado por primera vez en *1930* y es uno de los problemas de optimización más estudiados. Es usado como prueba para muchos métodos de optimización. Consiste en encontrar el camino único más corto que, dada una lista de ciudades y los costos entre ellas, visita todas las ciudades una sola vez y regresa a la ciudad de origen
##
## El Problema del Agente Viajero (TSP)
Plantaemos el problema del TSP enfocado en la teoria de grafos:
Sea $G = (V, A)$ un grafo completo, donde $V = {1, 2, 3, ..., n}$ es el conjunto de vértices y $A$ es el conjunto de aristas. Los vértices $i = {2, 3, 4, ..., n}$ se corresponden con los nodos a visitar y el vértice 1 es el nodo de origen y destino.
Por conveniencia nosotros definimos
$cost(x,y) = \left\{ \begin{array}{lcc} cost({x,y}) & si & x \neq y \\ \\ \infty & si &  x = y  \end{array} \right$

##
## Integrantes 
- Claudia Gisell Salas Cervantes 
- Tamara Popoca Alvarado
- Iván Delgado Carmona
- Ana Karem García Hernández

## Funciones importadas
1. `calcular_costo`, la cual calcula el costo entre dos ciudades
2. `generar_matriz`, genera una matriz aleatoria de $nxn$ que consta de los precios entre ciudades
