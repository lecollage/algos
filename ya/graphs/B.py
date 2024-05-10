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

'''