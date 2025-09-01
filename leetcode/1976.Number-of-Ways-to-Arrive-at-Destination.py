from typing import List
# from collections import deque
from queue import PriorityQueue

#
# @lc app=leetcode id=1631 lang=python3
#
# 1631. Path With Minimum Effort
#

# @lc code=start
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u,v,time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        distances = [float("inf")]*n
        numbersShortestPaths = [0]*n

        numbersShortestPaths[0] = 1

        # print(graph)
        # print(distances)

        queue = PriorityQueue()

        queue.put((0,0))

        distances[0] = 0

        while not queue.empty():
            distance, node = queue.get()

            if distance > distances[node]:
                continue

            if node == n-1:
                return numbersShortestPaths[node]

            for neighbour, weight in graph[node]:
                nextDistance = distance + weight

                if nextDistance < distances[neighbour]:
                    numbersShortestPaths[neighbour] = numbersShortestPaths[node]
                    distances[neighbour] = nextDistance
                    queue.put((nextDistance, neighbour))
                elif nextDistance == distances[neighbour]:
                    numbersShortestPaths[neighbour] = (numbersShortestPaths[node] + numbersShortestPaths[neighbour]) % (10**9 + 7)

        return 0
# @lc code=end


testCases = [
    {
        "n":  7,
        "roads": [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]],
        "expected": 4
    },
    {
        "n":  2,
        "roads": [[1,0,10]],
        "expected": 1
    }
]

for testCase in testCases:
    print('')

    n = testCase["n"]
    roads = testCase["roads"]
    expected = testCase["expected"]

    s = Solution()

    result = s.countPaths(n, roads)
    print(n, roads, result)
    assert result == expected, f"result {result} should be expected: {expected}"
