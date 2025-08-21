from typing import List
from collections import deque


# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        print(graph)

        n = len(graph)
        source = 0
        destination = n-1
        stack = []
        visited = [False for _ in range(n)]
        paths = []

        stack.append((source, [source]))

        while len(stack) > 0:
            node, path = stack.pop()

            print(node, path)

            if node == destination:
                paths.append(path)
                continue
            
            # if visited[node]:
            #     continue

            visited[node] = True

            for neighbour in graph[node]:
                newPath = path.copy()

                newPath.append(neighbour)

                stack.append((neighbour, newPath))

        return paths
# @lc code=end

'''
'''


testCases = [
    # {
    #     "graph": [[1,2],[3],[3],[]],
    #     "expected": [[0,1,3],[0,2,3]]
    # },
    {
        "graph": [[4,3,1],[3,2,4],[3],[4],[]],
        "expected": [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
    },
]

for testCase in testCases:
    print('')

    graph = testCase["graph"]
    expected = testCase["expected"]

    s = Solution()

    result = s.allPathsSourceTarget(graph)
    print(graph)
    assert result == expected, f"result {result} should be expected: {expected}"
