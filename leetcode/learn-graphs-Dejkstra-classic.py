def dijkstra(start, end, graph):
    n = len(graph)

    # start -> [Infinity, Infinity, Infinity, Infinity, Infinity, Infinity]

    distances = [float("inf")] * n
    distances[start] = 0
    visited = [False] * n

    for _ in range(n):
        # get next min vertice
        minNode = -1

        for i, d in enumerate(distances):
            if not visited[i] and (minNode == -1 or d < distances[minNode]):
                minNode = i

        if distances[minNode] == float("inf"):
            break

        if minNode == end:
            break

        neighbours = graph[minNode]
        
        for neighbour, weight in neighbours:
            if distances[neighbour] > distances[minNode] + weight:
                distances[neighbour] = distances[minNode] + weight

        visited[minNode] = True

    return distances[end]


'''
5 6
1 2 2
2 5 5
2 3 4
1 4 1
4 3 3
3 5 1
'''
# 1 4 3 5

'''
6 6
1 2 2
2 5 5
2 3 4
1 4 1
4 3 3
3 5 1
'''


n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1; v -= 1 
    graph[v].append((u, w))
    graph[u].append((v, w))

end = n-1

print(dijkstra(0, end, graph))
    