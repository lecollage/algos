import heapq # import priorQueue from queue

def dijkstra(start, end, graph):
    n = len(graph)

    distances = [float("inf")] * n
    distances[start] = 0
    prev = [-1] * n
    heap = [(0, start)]  

    while heap:
        # get next min vertice
        current_distance, current_node = heapq.heappop(heap)

        if current_distance > distances[current_node]:
            continue

        if distances[current_node] == float("inf"):
            break

        if current_node == end:
            break

        neighbours = graph[current_node]
        
        for neighbour, weight in neighbours:
            newDistance = distances[current_node] + weight

            if distances[neighbour] > newDistance:
                distances[neighbour] = newDistance
                prev[neighbour] = current_node
                heapq.heappush(heap, (newDistance, neighbour))

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
    