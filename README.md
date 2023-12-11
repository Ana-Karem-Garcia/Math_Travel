# Math_Travel
Python project in the LiMA where the problem of the traveling agent is solved.

##
## What does our project do?
It answers the following question: given a list of cities and the costs between each pair of them, what is the shortest possible route that visits each city exactly once and at the end returns to the home city? The problem was first formulated in *1930* and is one of the most studied optimization problems. It is used as a test for many optimization methods. It consists of finding the shortest single path that, given a list of cities and the costs between them, visits all the cities only once and returns to the city of origin.
##
## El Problema del Agente Viajero (TSP)
Plantaemos el problema del TSP enfocado en la teoria de grafos:
Sea $G = (V, A)$ un grafo completo, donde $V = {1, 2, 3, ..., n}$ es el conjunto de vértices y $A$ es el conjunto de aristas. Los vértices $i = {2, 3, 4, ..., n}$ se corresponden con los nodos a visitar y el vértice 1 es el nodo de origen y destino.
Por conveniencia nosotros definimos 
$cost(x,y)=cost({x,y})$ si $x \neq y$ e $\infty$ si $x=y$.
A cada arco $(i, j)$ se le asocia un valor no negativo $c_ij$ , que representa el coste de viajar del vértice $i$ al $j$.
El objetivo del Problema del Agente Viajero es encontrar una ruta que, comenzando y terminando en una ciudad determinada, en este caso denotada por la ciudad $i$, pase una sola vez por cada una de las ciudades y minimice el costo del recorrido. Si se definen las variables dicotómicas de decisión $x_ij$ para todo $(i, j) ∈ A$, de forma que tomen el valor 1 si el arco $(i, j)$ forma parte de la solución y $0$ en otro caso.

##
## Integrantes 
- Claudia Gisell Salas Cervantes 
- Tamara Popoca Alvarado
- Iván Delgado Carmona
- Ana Karem García Hernández

## Funciones importadas
1. `calcular_costo`, la cual calcula el costo entre dos ciudades
2. `generar_matriz`, genera una matriz aleatoria de $nxn$ que consta de los precios entre ciudades
