def bellmanFord(n, m, edges, src):
    INF = 30000
    distances = [INF] * n
    distances[src] = 0

    wasAnyRelaxation = True

    while wasAnyRelaxation:
        wasAnyRelaxation = False

        for u,v,w in edges:
            if distances[u] != INF:
                nextDistance = distances[u] + w

                if nextDistance < distances[v]:
                    distances[v] = nextDistance
                    wasAnyRelaxation = True
        
    return distances

'''
4 5
1 2 10
2 3 10
1 3 100
3 1 -10
2 3 1
'''
# 1 4 3 5


n, m = map(int, input().split())
edges = []

for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1; v -= 1 
    edges.append((u, v, w))

end = n-1

result = bellmanFord(n, m, edges, 0)

if result:
    print(*result)
else:
    print(-1)
    