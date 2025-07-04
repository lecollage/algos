from typing import List
# from collections import deque
from queue import PriorityQueue

#
# @lc app=leetcode id=787 lang=python3
#
# 787. Cheapest Flights Within K Stops
#

# @lc code=start
class Solution:
    def minimumEffortPath(self, grid: List[List[int]]) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0

        n = len(grid)
        m = len(grid[0])
        differences = [[float("inf")] * m for _ in range(n)]
        directions = [
            [-1,0],
            [0,-1],
            [1,0],
            [0,1],
        ]
        queue = PriorityQueue()

        queue.put((0,0,0)) # diff, i, j 
        differences[0][0] = 0

        def isEnd(i, j) -> bool:
            return i == n-1 and j == m-1

        def isValid(i: int, j: int, grid: List[List[int]]) -> bool:
            if i < 0 or i >= len(grid):
                return False
            
            if j < 0 or j >= len(grid[i]):
                return False
            
            return True
        
        while not queue.empty():
            currentDiff, i, j = queue.get()
            
            print(currentDiff, i, j, differences)

            if currentDiff > differences[i][j]:
                continue

            if isEnd(i,j):
                break

            for dirI, dirJ in directions:
                nextI = i + dirI
                nextJ = j + dirJ

                if isValid(nextI, nextJ, grid):
                    nextDiff = currentDiff

                    # go uphill
                    if grid[nextI][nextJ] > grid[i][j]:
                        nextDiff = grid[nextI][nextJ] - grid[i][j]

                    if differences[nextI][nextJ] > nextDiff:
                        differences[nextI][nextJ] = nextDiff
                        queue.put((nextDiff, nextI, nextJ))
        
        return differences[n-1][m-1]
# @lc code=end


testCases = [
    {
        "grid": [
            # [1,10,6,7,9,10,4,9]
            [1,10,6,7]
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
        "grid": [[1,2,3],[3,8,4],[5,3,5]],
        "expected": 1
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
