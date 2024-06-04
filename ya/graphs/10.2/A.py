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

# print(*getFirstGraph(n, routes), sep='\n')  
# print(*getSecondGraph(n, routes), sep='\n') 

for row in getFirstGraph(n, routes):
    print(*row)

for row in getSecondGraph(n, routes):
    print(*row)






'''
Ввод
5 3
3      1 2 3
2      1 2
5      5 2 4 3 1

Вывод
     1 2 3 4 5   
1    0 1 1 0 0
2    1 0 1 1 1
3    1 1 0 1 0
4    0 1 1 0 0
5    0 1 0 0 0


1-5

1,2 | 2,1
1,3 | 3,1
2,3 | 3,2


5,2
5,4
5,3
5,1
2,4
2,3
2,1


     1 2 3 4 5  
1    0 1 1 1 1
2    1 0 1 1 1
3    1 1 0 1 1
4    1 1 1 0 1
5    1 1 1 1 0


1: [2,3]
2: [1,3,4]
3: [1,2,4]
4: [2,3]
5: [2]

i,j
j,i
i: 1-1, j: 2-1


0 1 1 1 1
1 0 1 1 1
1 1 0 1 1
1 1 1 0 1
1 1 1 1 0


'''