# Math_Travel
Python project in the LiMA where the problem of the traveling agent is solved.
![](https://github.com/Ana-Karem-Garcia/Math_Travel/blob/main/Doc/Agente.jpeg)

##
# What does our project do?
It answers the following question: given a list of cities and the costs between each pair of them, what is the shortest possible route that visits each city exactly once and at the end returns to the home city? The problem was first formulated in *1930* and is one of the most studied optimization problems. It is used as a test for many optimization methods. It consists of finding the shortest single path that, given a list of cities and the costs between them, visits all the cities only once and returns to the city of origin.
##
# The Travel Agent Problem(TSP)
Let's plant the problem of TSP focused on graph theory:
Let $G = (V, A)$ be a complete graph, where $V = {1, 2, 3, ..., n}$ is the set of vertices and $A$ is the set of edges. The vertices $i = {2, 3, 4, ..., n}$ correspond to the nodes to be visited, and vertex 1 is the source and destination node.
For convenience we define
$cost(x,y)=cost({x,y})$ if $x neq y$ e $infty$ if $x=y$.
Each $(i, j)$ arc is associated with a non-negative value $c_ij$ , which represents the cost of traveling from vertex $i$ to $j$.
The goal of the Travel Agent Problem is to find a route that, starting and ending in a given city, in this case denoted by the city $i$, passes only once through each of the cities and minimizes the cost of the tour.  If the dichotomous decision variables $x_ij$ are defined for all $(i, j) ∈ A$, so that they take the value 1 if the arc $(i, j)$ is part of the solution and $0$ otherwise.

##
# Members 
- Salas Cervantes Claudia Gisell
- Popoca Alvarado Tamara 
- Delgado Carmona Iván
- García Hernández Ana Karem 

# Imported Functions
1. `generar_matriz`, generates a random $nxn$ matrix with zeros on the diagonal consisting of cross-city prices.
2. `agente_viajero_poda`, main function of the agent journey and the cost it accumulates.

##
# Github profiles
| [<img src="https://avatars.githubusercontent.com/u/141759953?v=4" width=100><br><sub>Claudia Gisell </sub>](https://github.com/Claudia-Salas) |  [<img src="https://avatars.githubusercontent.com/u/142260985?v=4" width=100><br><sub>Ana Karem </sub>](https://github.com/Ana-Karem-Garcia) |  [<img src="https://avatars.githubusercontent.com/u/141845372?v=4" width=100><br><sub>Tamara</sub>](https://github.com/Tamara0409)  |[<img src="https://avatars.githubusercontent.com/u/142260687?v=4" width=100><br><sub>Iván</sub>](https://github.com/ivan-math) |
| :---: | :---: | :---: |  :---: | 


