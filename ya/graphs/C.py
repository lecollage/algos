from typing import List

def isTree(v: int, e: int, edges: List[List[int]]) -> bool:
    if v-1 != e:
        return False

    graph = [[] for _ in range(0, v)]

    for _, [A,B] in enumerate(edges):
        graph[A].append(B)
        graph[B].append(A)
    
    visited = [False for _ in range(0, v)]

    def dfs(vertex: int):
        for el in graph[vertex]:
            if visited[el]:
                continue

            visited[el] = True
            dfs(el)

    dfs(0)
            
    return sum(visited) == len(visited)


edges = []
v, e = map(int, input().split())
for _ in range(0, e):
    n1, n2 = map(int, input().split())
    edges.append([n1-1, n2-1])

print(isTree(v,e, edges))



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

        [
0        [1,2]
1        [2]
2        [1]
3        []
        ]


{
    1: [2,3],
    2: [3],

}

6 3

800 2
1 3
2 3
'''