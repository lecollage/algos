from typing import List

'''
1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.
'''

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dp = [[float("inf") for _ in range(n)] for _ in range(n)]
        p = [[None for _ in range(n)] for _ in range(n)]

        for u,v,w in edges:
            if w <= distanceThreshold:
                dp[u][v] = w
                dp[v][u] = w
                p[u][v] = v
                p[v][u] = u

        for i in range(n):
            dp[i][i] = 0
            p[i][i] = i

        print(dp)

        for k in range(n):
            for u in range(n):
                for v in range(n):
                    if dp[u][v] > dp[u][k] + dp[k][v] and dp[u][k] + dp[k][v] <= distanceThreshold:
                        dp[u][v] = dp[u][k] + dp[k][v]
                        p[u][v] = p[u][k]

        print(dp)
        print(p)

        minCityIndex = -1
        minCityCount = -1

        for u in range(n):
            count = 0

            for v in range(n):
                if u != v and p[u][v] != None:
                    count += 1

            if minCityIndex == -1:
                minCityIndex = u
                minCityCount = count
            elif count <= minCityCount:
                minCityCount = count
                minCityIndex = u

        return minCityIndex

'''
[
    [0, 3, 4, 5],
    [3, 0, 1, 2],
    [4, 1, 0, 1],
    [5, 2, 1, 0]
]

0 -> 1 -> 2

[
    [0, 3, inf, inf],
    [3, 0, 1, 4],
    [inf, 1, 0, 1],
    [inf, 4, 1, 0]
]

[
    [0, 1, None, None],
    [1, 1, 2, 2],
    [None, 2, 2, 3],
    [None, 3, 3, 3]
]


[
    [0, 1, 1, None],
    [0, 1, 2, 2],
    [1, 1, 2, 3],
    [None, 2, 2, 3]
]

----------

[
    [0, 1, None, None, None],
    [0, 1, None, None, 4],
    [None, None, 2, 3, 3],
    [None, None, 2, 3, 4],
    [None, 1, 3, 3, 4]
]
'''

testCases = [
    {
        "edges": [
            [0,1,3],
            [1,2,1],
            [1,3,4],
            [2,3,1]
        ],
        "n": 4,
        "distanceThreshold": 4,
        "expected": 3
    },
    {
        "edges": [
            [0,1,2],
            [0,4,8],
            [1,2,3],
            [1,4,2],
            [2,3,1],
            [3,4,1]
        ],
        "n": 5,
        "distanceThreshold": 2,
        "expected": 0
    },
]


for testCase in testCases:
    print('')

    edges = testCase["edges"]
    n = testCase["n"]
    distanceThreshold = testCase["distanceThreshold"]
    expected = testCase["expected"]

    s = Solution()

    result = s.findTheCity(n, edges, distanceThreshold)
    print(n, distanceThreshold, edges)
    assert result == expected, f"result {result} should be expected: {expected}"
