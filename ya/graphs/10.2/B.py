from typing import Optional, List

def getFirstGraph(stopsCount: int, routes: List[List[int]]) -> List[List[int]]:
    matrix = [[0] * stopsCount for _ in range(stopsCount)]

    for route in routes:
        for j in range(1, len(route)):
            u = route[j-1]-1
            v = route[j]-1

            matrix[u][v] = 1
            matrix[v][u] = 1

    return matrix

def getSecondGraph(stopsCount: int, routes: List[List[int]]) -> List[List[int]]:
    matrix = [[0] * stopsCount for _ in range(stopsCount)]

    for route in routes:
        for i in range(0, len(route)-1):
            for j in range(i+1, len(route)):
                u = route[i]-1
                v = route[j]-1

                matrix[u][v] = 1
                matrix[v][u] = 1

    return matrix




n, m = map(int, input().split())
routes = [[] for _ in range(m)]
for i in range(0, m):
    _, *routes[i] = map(int, input().split())







'''
3 3

###
...
..#

2 2
6
RMLLMM

[2,2] - [2,3] - [2,2] - [2,1]
3


i,j
nextI, nextJ
count++

set()

(2,3)
(2,4)


1: [2]


'''