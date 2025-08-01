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
        
        def isGood(threshold):
            queue = deque()
            visited = [[False for _ in range(m)] for _ in range(n)]

            queue.appendleft((0,0)) # i, j

            while queue:
                i, j = queue.popleft()

                # print(i, j)

                if isEnd(i,j):
                    return True

                for dI, dJ in directions:
                    nextI = i + dI
                    nextJ = j + dJ

                    if isValid(nextI, nextJ) and not visited[nextI][nextJ]:
                        edgeWeight = abs(grid[i][j] - grid[nextI][nextJ])

                        if edgeWeight <= threshold:
                            queue.appendleft((nextI, nextJ))
                            visited[nextI][nextJ] = True

            return False

        # print(isGood(9))

        left = 0
        right = 10**6

        while right>left:
            middle = (right+left)//2

            x = isGood(middle)

            # print(left, middle, right, x)

            if x:
                right = middle
            else:
                left = middle+1

        return right

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
            [1,2,3],
            [3,8,4],
            [5,3,5]
        ],
        "expected": 1
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
