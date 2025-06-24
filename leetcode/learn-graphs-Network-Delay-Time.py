from typing import List
import math

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, start: int) -> int:
        # print(times, n, start)

        start -= 1

        if start >= n:
            return -1
        
        graph = [[] for _ in range(n)]

        for u, v, w in times:
            u -= 1
            v -= 1
            graph[u].append((v, w))
            # graph[v].append((u, w))

        # print(graph)

        edgeVertices = []

        for i in range(n):
            if len(graph[i]) == 0:
                edgeVertices.append(i)

        # print(edgeVertices)

        distances = [float("inf")] * n
        distances[start] = 0
        visited = [False] * n

        for _ in range(n):
            # get min node
            minNode = -1

            for node, distance in enumerate(distances):
                if not visited[node] and (minNode == -1 or distance < distances[minNode]):
                    minNode = node
            
            neighbours = graph[minNode]

            for neighbour, weight in neighbours:
                newDistance  = distances[minNode] + weight

                if distances[neighbour] > newDistance:
                    distances[neighbour] = newDistance
            
            visited[minNode] = True

        # print(distances)

        maxDistance = -1

        for node in range(n):
            if math.isinf(distances[node]):
                return -1

            if distances[node] > 0 :
                maxDistance = max(distances[node], maxDistance)

        return maxDistance

testCases = [
    {
        "times": [
            [2,1,1],
            [2,3,1],
            [3,4,1]
        ],
        "n": 4,
        "k": 2,
        "expected": 2
    },
    {
        "times": [[1,2,1]],
        "n": 2,
        "k": 1,
        "expected": 1
    },
    {
        "times": [[1,2,1]],
        "n": 2,
        "k": 2,
        "expected": -1
    },
    {
        "times": [
            [1,2,1],
            [2,3,2],
            [1,3,4]
        ],
        "n": 3,
        "k": 1,
        "expected": 3
    },
    {
        "times": [
            [1,2,1],
            [2,1,3]
        ],
        "n": 2,
        "k": 2,
        "expected": 3
    },
    {
        "times": [
            [1,2,1],
            [2,3,2],
            [1,3,1]
        ],
        "n": 3,
        "k": 2,
        "expected": -1
    },
    
]

'''
0-1 1
1-2 2
0-2 1
'''


for testCase in testCases:
    print('')

    times = testCase["times"]
    n = testCase["n"]
    k = testCase["k"]
    expected = testCase["expected"]

    s = Solution()

    result = s.networkDelayTime(times, n, k)
    print(times, n, k, result)
    assert result == expected, f"result {result} should be expected: {expected}"
