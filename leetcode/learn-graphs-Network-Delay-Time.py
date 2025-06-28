from typing import List
import math
import heapq

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

        heap = []
        heapq.heappush(heap, (0, start))

        distances = [float("inf")] * n
        distances[start] = 0

        while heap:
            current_distance, current_node = heapq.heappop(heap)

            if current_distance > distances[current_node]:
                continue
            
            neighbours = graph[current_node]

            for neighbour, weight in neighbours:
                newDistance  = distances[current_node] + weight

                if distances[neighbour] > newDistance:
                    distances[neighbour] = newDistance
                    heapq.heappush(heap, (newDistance, neighbour))

        # print(distances)

        maxDistance = -1

        for node in range(n):
            if math.isinf(distances[node]):
                return -1

            if distances[node] > 0 :
                maxDistance = max(distances[node], maxDistance)

        return maxDistance

'''
You are given a network of n nodes, labeled from 1 to n.
You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k.
Return the minimum time it takes for all the n nodes to receive the signal.
If it is impossible for all the n nodes to receive the signal, return -1.

'''

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
