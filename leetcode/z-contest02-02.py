from typing import List
from collections import deque

# @lc code=start
class Solution:
    def isGood(self, minItem: int, maxItem: int, k: int) -> bool:
        return minItem*k >= maxItem # max <= min * k

    def binSearch(self, nums: List[int], start: int, minItem: int, k: int) -> int:
        # all bad
        if not self.isGood(minItem, nums[start], k):
            return -1

        # find good
        n = len(nums)
        left = start
        right = n

        while left+1 < right:
            middle = (left + right)//2

            if self.isGood(minItem, nums[middle], k):
                left = middle
            else:
                right = middle

        # print(left, right, start, minItem, k)

        if right == n and not self.isGood(minItem, nums[-1], k):
            return -1

        return left

    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if n == 1:
            return 0

        nums.sort(key=lambda x: x)

        print(nums)

        minCommon = float("inf")

        for i in range(n):
            if i == n-1:
                minCommon = min(minCommon, n-1)
            else:
                j = self.binSearch(nums, i+1, nums[i], k)

                if j != -1:
                    minCommon = min(minCommon, n - (j - i + 1))

            print(i, j, minCommon)
      
        return minCommon
# @lc code=end



'''
[1,6,2,9]
[1,2] -> 2
[2,6] -> 2

'''

testCases = [
    {
        "nums": [1,2,5],
        "i": 0,
        "k": 1,
        "expected": -1
    },
    {
        "nums": [1,2,5],
        "i": 1,
        "k": 1,
        "expected": -1
    },
    {
        "nums": [1,2,5],
        "i": 0,
        "k": 2,
        "expected": 1
    },
    {
        "nums": [1,2,6,9],
        "i": 0,
        "k": 2,
        "expected": 1
    },
    {
        "nums": [1,2,6,9],
        "i": 1,
        "k": 2,
        "expected": -1
    },
    {
        "nums": [1,2,6,9],
        "i": 2,
        "k": 2,
        "expected": 3
    },
    {
        "nums": [1,2,6,10000000],
        "i": 2,
        "k": 2,
        "expected": -1
    },
]

for testCase in testCases:
    print('')

    nums = testCase["nums"]
    i = testCase["i"]
    k = testCase["k"]
    expected = testCase["expected"]

    s = Solution()
    start = i+1
    minItem = nums[i]
    result = s.binSearch(nums, start, minItem, k)
    print(nums, k, result)
    assert result == expected, f"result {result} should be expected: {expected}"

# ##################

testCases = [
    {
        "nums": [2,1,5],
        "k": 2,
        "expected": 1
    },
    {
        "nums": [1,6,2,9],
        "k": 3,
        "expected": 2
    },
    {
        "nums": [4,6],
        "k": 2,
        "expected": 0
    },
]

for testCase in testCases:
    print('')

    nums = testCase["nums"]
    k = testCase["k"]
    expected = testCase["expected"]

    s = Solution()

    result = s.minRemoval(nums, k)
    print(nums, k, result)
    assert result == expected, f"result {result} should be expected: {expected}"

