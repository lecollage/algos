from typing import List
from collections import deque

# 

# @lc code=start
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int) -> List[List[int]]:

# @lc code=end


testCases = [
    {
        "grid": [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],
        "x": 1,
        "y": 0,
        "expected": [[1,2,3,4],[13,14,15,8],[9,10,11,12],[5,6,7,16]]
    },
]

for testCase in testCases:
    print('')

    grid = testCase["grid"]
    x = testCase["x"]
    y = testCase["y"]
    expected = testCase["expected"]

    s = Solution()

    result = s.reverseSubmatrix(grid, x, y)
    print(grid, x, y, result)
    assert result == expected, f"result {result} should be expected: {expected}"
