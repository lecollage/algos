from typing import List
from collections import deque


# @lc code=start
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        print(graph)

        stack = []
        visited = [False for _ in range(n)]

        stack.append(source)

        while len(stack) > 0:
            node = stack.pop()

            if node == destination:
                return True
            
            if visited[node]:
                continue

            visited[node] = True

            for neighbour in graph[node]:
                stack.append(neighbour)

        return False
# @lc code=end

'''
'''


testCases = [
    {
        "n": 3,
        "edges": [[0,1],[1,2],[2,0]],
        "source": 0,
        "destination": 2,
        "expected": True
    },
    {
        "n": 6,
        "edges": [[0,1],[0,2],[3,5],[5,4],[4,3]],
        "source": 0,
        "destination": 5,
        "expected": False
    },
]

for testCase in testCases:
    print('')

    n = testCase["n"]
    edges = testCase["edges"]
    source = testCase["source"]
    destination = testCase["destination"]
    expected = testCase["expected"]

    s = Solution()

    result = s.validPath(n, edges, source, destination)
    print(n, edges, source, destination)
    assert result == expected, f"result {result} should be expected: {expected}"
