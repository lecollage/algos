from typing import List

def getMatrix(v: int, e: int, edges: List[List[int]]):
    matrix = [
        0 for _ in range(0, v)
    ]

    for _, [v, u] in enumerate(edges):
        ...


    

    return matrix

edges = []
v, e = map(int, input().split())
for _ in range(0, e):
    n1, n2 = map(int, input().split())
    edges.append([n1, n2])

print(*getMatrix(v,e, edges), sep='\n')



'''
node {
    1: [2,3]
}

3

        [
0        [1,2]
1        [0]
2        [0]
3        []
4        []
5        [7,8]
6        []
7        [5]
8        [5]
        ]

DFS
0: 1,2
1: 0
2: 0

visited: [True,True,True]

-----------------------

4 3

1 2
1 3
2 3
4

        [
0        [1,2]
1        [2]
2        [1]
3        []
        ]



    




'''