from typing import List
from queue import PriorityQueue

# @lc code=start
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u,v,time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        # calc shortest path

        distances = [float("inf")]*n
        q = PriorityQueue()

        q.put((0, 0))
        distances[0] = 0

        while not q.empty():
            distance, node = q.get()

            if distances[node] < distance:
                continue

            for neighbour, weight in graph[node]:
                if distance+weight < distances[neighbour]:
                    q.put((distance+weight, neighbour))
                    distances[neighbour] = distance+weight

        # print(distances)

        # build new graph with only shortest paths (DAG), no weights needed

        DAG = [[] for _ in range(n)]

        for u,v,time in roads:
            if time + distances[u] == distances[v]:
                DAG[u].append(v)

            if time + distances[v] == distances[u]:
                DAG[v].append(u)

        visited = [False] * n
        topSorted = []

        # print(DAG)

        def DFS(node: int):
            if visited[node]:
                return
            
            visited[node] = True

            for neighbour in DAG[node]:
                DFS(neighbour)

            topSorted.append(node)

        DFS(0)
        topSorted.reverse()

        dp = [0] * n

        # print(topSorted)

        dp[0] = 1

        for node in topSorted:
            for neighbour in DAG[node]:
                dp[neighbour] += dp[node]

        # print(dp)

        return dp[n-1]  % (10**9 + 7)
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
