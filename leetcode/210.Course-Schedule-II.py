from typing import List

# @lc code=start
class Solution:
    time = 0

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # graph
        # visited
        # DFS

        graph = [[] for _ in range(numCourses)]

        for v,u in prerequisites:
            graph[u].append(v)

        print(graph)

        tin = [-1] * n
        tout = [-1] * n

        def DFS(node: int):
            if visited[node]:
                return

            visited[node] = True
            tin[node] = self.time
            self.time += 1

            for neighbour in graph[node]:
                DFS(neighbour)

            tout[node] = self.time
            self.time += 1
                
        visited = [0] * numCourses

        DFS(0)

        print(tin)
        print(tout)

        

# @lc code=end

inputs = [
    [
        2,
        [
            [1,0]
        ],
        [0,1]
    ],
    [
        4,
        [
            [1,0],[2,0],[3,1],[3,2]
        ],
        [0,1,2,3]
    ],
    [
        1,
        [
            []
        ],
        [0]
    ],
]

for n, cources, expect in inputs:
    print()
    s = Solution()
    res = s.findOrder(n, cources)
    print(res == expect)
    assert res == expect, f"result {res} should be expected: {expect}"

