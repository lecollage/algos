# @lc code=start

from collections import deque
from typing import Optional, List

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]

        for u,v in edges:
            graph[u].append(v)

        stack = []
        visited = set()

        stack.append(source)
        visited.add(source)

        while len(stack):
            node = stack.pop()

            if node == destination:
                return True

            for neighbour in graph[node]:
                if neighbour not in visited:
                     stack.append(neighbour)
                     visited.add(neighbour)

        return False
# @lc code=end



testCases = [
    {
        "n": 3,
        "edges": [[0,1],[0,2]],
        "source": 0,
        "destination": 2,
        "expected": False
    },
    {
        "n": 4,
        "edges": [[0,1],[0,3],[1,2],[2,1]],
        "source": 0,
        "destination": 3,
        "expected": False
    },
    {
        "n": 4,
        "edges": [[0,1],[0,2],[1,3],[2,3]],
        "source": 0,
        "destination": 3,
        "expected": True
    },
    {
        "n": 2,
        "edges":  [[0,1],[1,1]],
        "source": 0,
        "destination": 1,
        "expected": False
    },
]

for testCase in testCases:
    print('')

    expected = testCase["expected"]

    s = Solution()

    result = s.leadsToDestination(n=testCase["n"], edges=testCase["edges"], source=testCase["source"], destination=testCase["destination"])
    print(testCase, result)
    assert result == expected, f"result {result} should be expected: {expected}"

