from typing import List
from collections import deque
# from queue import Queue

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
        
        def good(left, right): 
            queue = deque()
            visited = [[False for _ in range(m)] for _ in range(n)]

            queue.appendleft((0, 0, 0))

            while len(queue) > 0:
                i, j, diff = queue.pop()

                if isEnd(i,j):
                    return True

                if visited[i][j]:
                    continue

                visited[i][j] = True

                print(i,j,diff, (left, right))

                for di, dj in directions:
                    nextI = i + di
                    nextJ = j + dj

                    if isValid(nextI, nextJ):
                        nextDiff = abs(grid[nextI][nextJ]-grid[i][j])
                        nextDiff = max(nextDiff,diff)

                        # if nextDiff == left:
                            # queue.appendleft((nextI, nextJ, nextDiff))

                        if nextDiff >= left and nextDiff < right:
                            queue.append((nextI, nextJ, nextDiff))
            
            return False
        
        # print(good(0, 1000000))

        # return -1

        left = 0
        right = 10**6 + 1
        middle = 1

        while right-left>1:
            middle = round((left+right)/2)

            if good(left, middle):
                right = middle
            else:
                left = middle

        return left

# @lc code=end


testCases = [
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
    {
        "grid": [[4,3,4,10,5,5,9,2],[10,8,2,10,9,7,5,6],[5,8,10,10,10,7,4,2],[5,1,3,1,1,3,1,9],[6,4,10,6,10,9,4,6]],
        "expected": 5
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
