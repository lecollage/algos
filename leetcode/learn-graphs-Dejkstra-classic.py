def dijkstra(start, end, graph):
    n = len(graph)

    # start -> [Infinity, Infinity, Infinity, Infinity, Infinity, Infinity]

    distances = [float("inf")] * n
    distances[start] = 0
    visited = [False] * n
    prev = [-1] * n

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
            newDistance  = distances[minNode] + weight

            if distances[neighbour] > newDistance:
                distances[neighbour] = newDistance
                prev[neighbour] = minNode

        visited[minNode] = True

    if distances[end] == float("inf"):
        return []

    node = end
    path = [end+1]

    while node != start:
        node = prev[node]
        path.append(node+1)

    return path[::-1] # reverced


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

result = dijkstra(0, end, graph)

if result:
    print(*result)
else:
    print(-1)
    