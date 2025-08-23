from typing import List
from collections import deque

# 25 min

# @lc code=start
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        submaxtrixStartI = x
        submaxtrixStartJ = y
        submaxtrixEndI = submaxtrixStartI + k
        submaxtrixEndJ = submaxtrixStartJ + k

        iter = 0

        while submaxtrixStartI + iter < submaxtrixEndI - iter:
            row1 = submaxtrixStartI + iter
            row2 = submaxtrixEndI - iter - 1

            # print(row1, row2)

            for j in range(y, submaxtrixEndJ):
                buff = grid[row1][j]
                grid[row1][j] = grid[row2][j]
                grid[row2][j] = buff

            iter += 1

        return grid

# @lc code=end


testCases = [
    {
        "grid": [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],
        "x": 1,
        "y": 0,
        "k": 3,
        "expected": [[1,2,3,4],[13,14,15,8],[9,10,11,12],[5,6,7,16]]
    },
    {
        "grid": [[3,4,2,3],[2,3,4,2]],
        "x": 0,
        "y": 2,
        "k": 2,
        "expected": [[3,4,4,2],[2,3,2,3]]
    },
]

for testCase in testCases:
    print('')

    grid = testCase["grid"]
    x = testCase["x"]
    y = testCase["y"]
    k = testCase["k"]
    expected = testCase["expected"]

    s = Solution()

    result = s.reverseSubmatrix(grid, x, y, k)
    print(grid, x, y, k, result)
    assert result == expected, f"result {result} should be expected: {expected}"
