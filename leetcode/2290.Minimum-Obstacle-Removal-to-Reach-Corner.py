from typing import List
from collections import deque

#
# @lc app=leetcode id=3286 lang=python3
#
# 3286. Find a Safe Walk Through a Grid
#

# @lc code=start
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        directions = [
            [-1,0],
            [0,-1],
            [1,0],
            [0,1],
        ]

        def isValid(x: int,y: int) -> bool:
            if x < 0 or x > n-1:
                return False
            
            if y < 0 or y > m-1:
                return False

            return True

        q = deque()

        q.appendleft((0,0,0)) # x,y,obstacles

        while(len(q)):
            x,y,obstacles = q.popleft()

            # print(x,y,obstacles, grid, q)

            if x == n-1 and y == m-1:
                return obstacles

            for dX, dY in directions:
                newX = x+dX
                newY = y+dY

                if isValid(newX, newY) and grid[newX][newY] != -1:
                    if grid[newX][newY] == 1:
                        q.append((newX, newY, obstacles + 1))
                    else:
                        q.appendleft((newX, newY, obstacles))

                    grid[newX][newY] = -1

        # print(grid)

        return -1
# @lc code=end

"""
[-1, -1, 1],
[-1, -1, 0],
[1, 1, 0]
"""

testCases = [
    {
        "grid": [[0,1,1],[1,1,0],[1,1,0]],
        "expected": 2
    },
    {
        "grid": [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]],
        "expected": 0
    },
]

for testCase in testCases:
    print('')

    grid = testCase["grid"]
    expected = testCase["expected"]

    s = Solution()

    result = s.minimumObstacles(grid)
    print(grid, result)
    assert result == expected, f"result {result} should be expected: {expected}"
