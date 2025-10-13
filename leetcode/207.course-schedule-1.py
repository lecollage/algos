from typing import List

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # graph
        # visited
        # DFS

        graph = [[] for _ in range(numCourses)]

        for v,u in prerequisites:
            graph[u].append(v)

        print(graph)

        def DFS(node: int) -> bool:
            print(node, visited)

            if visited[node] == 1:
                return False
            
            if visited[node] == 2:
                return True

            visited[node] = 1
            
            

            for neighbour in graph[node]:
                if not DFS(neighbour):
                    return False

            visited[node] = 2

            return True

        visited = [0] * numCourses

        for node in range(numCourses):
            if visited[node] == 0 and not DFS(node):
                return False
    
        return True


        

# @lc code=end

inputs = [
    [
        2,
        [
            [1,0]
        ],
        True
    ],
    [
        4,
        [
            [1,0],
            [2,1],
            [2,3],
        ],
        True
    ],
    [
        4,
        [
            [1,0],
            [2,1],
            [2,3],
            [3,0],
        ],
        True
    ],
    [
        4,
        [
            [1,0],
            [2,1],
            [2,3],
            [0,3],
            [3,0],
        ],
        False
    ],
    [
        3,
        [
            [1,0],
            [0,2],
            [2,1]
        ],
        False
    ],
    [
        4,
        [
            [3,2],
            [3,1],
            [2,0],
            [1,0],
            [0,1],
        ],
        False
    ],
    [
        9,
        [
            [3,2],
            [3,1],
            [2,0],
            [1,0],

            [4,3],

            [5,6],
            [5,7],
            [7,8],
            [6,8],
            [8,0],

            [0,5],
        ],
        False
    ]
]

for n, cources, expect in inputs:
    print()
    s = Solution()
    res = s.canFinish(n, cources)
    print(res == expect)
    assert res == expect, f"result {res} should be expected: {expect}"

