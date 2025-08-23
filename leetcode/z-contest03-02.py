from typing import List
from collections import deque

# @lc code=start
class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        print(nums[1] & nums[3])
        print(nums[0] & nums[3])
        print(nums[1] & nums[2])
        print(5 & 3)
        print(1000 & 9999)
        print(2 & 1)

        return -1
# @lc code=end


testCases = [
    {
        "arr": [0,3,2,1],
        "expected": 1
    },
    {
        "arr": [0,1,3,2],
        "expected": 2
    },
    {
        "arr": [3,2,1,0],
        "expected": 0
    },
]

for testCase in testCases:
    print('')

    arr = testCase["arr"]
    expected = testCase["expected"]

    s = Solution()

    result = s.sortPermutation(arr)
    print(arr, result)
    assert result == expected, f"result {result} should be expected: {expected}"

