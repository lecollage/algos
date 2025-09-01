from typing import List
from collections import deque

# 18 min

# @lc code=start
class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort(key = lambda x: x)

        n = len(nums)

        print(nums)

        i = 0
        j = n-1
        result = 0

        while i < j:
            median = nums[j-1]
            result += median
            i += 1
            j -= 2

        return result

# @lc code=end


testCases = [
    {
        "nums": [2,1,3,2,1,3],
        "expected": 5
    },
    {
        "nums": [1,1,10,10,10,10],
        "expected": 20
    },
    {
        "nums": [6,9,12,14,1,9],
        "expected": 21
    },
    {
        "nums": [6,9,12],
        "expected": 9
    },

    {
        "nums": [],
        "expected": 0
    },
]

for testCase in testCases:
    print('')

    nums = testCase["nums"]
    expected = testCase["expected"]

    s = Solution()

    result = s.maximumMedianSum(nums)
    print(nums, result)
    assert result == expected, f"result {result} should be expected: {expected}"
