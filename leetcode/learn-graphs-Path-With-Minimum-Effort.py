from typing import List
from collections import deque

#
# @lc app=leetcode id=1631 lang=python3
#
# 1631. Path With Minimum Effort
#

# @lc code=start
class Solution:
    def minimumEffortPath(self, grid: List[List[int]]) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0

        n = len(grid)
        m = len(grid[0])
       
        INF = 10**6+1

        directions = [
            [-1,0],
            [0,-1],
            [1,0],
            [0,1],
        ]

        def isEnd(i, j) -> bool:
            return i == n-1 and j == m-1

        def isValid(i: int, j: int) -> bool:
            if i < 0 or i >= len(grid):
                return False
            
            if j < 0 or j >= len(grid[i]):
                return False
            
            return True
        
        # build array of edges

        edges = []
        queue = deque()
        visited = [[False for _ in range(m)] for _ in range(n)]

        queue.appendleft((0,0)) # i, j

        while queue:
            i, j = queue.popleft()

            # print(i, j)

            for dI, dJ in directions:
                nextI = i + dI
                nextJ = j + dJ

                if isValid(nextI, nextJ) and not visited[nextI][nextJ]:
                    edgeWeight = abs(grid[i][j] - grid[nextI][nextJ])

                    edges.append(((i,j), (nextI, nextJ), edgeWeight))
                    queue.appendleft((nextI, nextJ))
                    visited[nextI][nextJ] = True

        print(edges)

        # perform Bellman Ford to calculate shortest path from 0 to m-1, n-1

        distances = [[INF for _ in range(m)] for _ in range(n)]
        distances[0][0] = 0

        wasAnyRelaxation = True

        while wasAnyRelaxation:
            wasAnyRelaxation = False

            for u, v, w in edges:
                ui, uj = u
                vi, vj = v

                print(ui, uj, vi, vj, w, distances)

                if distances[ui][uj] != INF:
                    nextDistance = w

                    if nextDistance < distances[vi][vj]:
                        distances[vi][vj] = nextDistance
                        wasAnyRelaxation = True

        print(distances)

        return distances[n-1][m-1]

# @lc code=end


testCases = [
    {
        "grid": [
            [1,2,3],
            [3,8,4],
            [5,3,5]
        ],
        "expected": 1
    },
    {
        "grid": [
            [1,10,6,7]
        ],
        "expected": 9
    },
    {
        "grid": [
            [1,10,6,7,9,10,4,9]
        ],
        "expected": 9
    },
    {
        "grid": [
            [1,2,2],
            [3,8,2],
            [5,3,5]
        ],
        "expected": 2
    },
    {
        "grid": [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]],
        "expected": 0
    },
    {
        "grid": [[9]],
        "expected": 0
    },
    {
        "grid": [[9, 9, 9]],
        "expected": 0
    },
    {
        "grid": [
            [9],
            [9],
            [9],
            [9]
        ],
        "expected": 0
    },
]

for testCase in testCases:
    print('')

    grid = testCase["grid"]
    expected = testCase["expected"]

    s = Solution()

    result = s.minimumEffortPath(grid)
    print(grid, result)
    assert result == expected, f"result {result} should be expected: {expected}"
