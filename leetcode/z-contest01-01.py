from typing import List
from collections import deque


'''
You are given an integer array nums of length n.

An array is trionic if there exist indices 0 < p < q < n − 1 such that:

nums[0...p] is strictly increasing,
nums[p...q] is strictly decreasing,
nums[q...n − 1] is strictly increasing.
Return true if nums is trionic, otherwise return false.

©leetcode

'''

# @lc code=start
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums) < 4: 
            return False

        n = len(nums)
        part1 = False
        part2 = False
        part3 = False

        i = 0
        j = 1

        while j < n and nums[i] < nums[j]:
            i += 1
            j += 1
            part1 = True

        # i -> p

        while j < n and nums[i] > nums[j]:
            i += 1
            j += 1
            part2 = True

        # i -> q

        while j < n and nums[i] < nums[j]:
            i += 1
            j += 1
            part3 = True
        
        if j != n:
            part3 = False

        # i -> n-1

        return part1 and part2 and part3
# @lc code=end


testCases = [
    {
        "arr": [1,3,5,4,2,6],
        "expected": True
    },
    {
        "arr": [2,1,3],
        "expected": False
    },
    {
        "arr": [-1000, -999, 0, -1, 1,3],
        "expected": True
    },
    {
        "arr": [-1000, -999, 0, -1, 1, 3, 2],
        "expected": False
    },
    {
        "arr": [-1000, -999, 0, 1, 1, 3],
        "expected": False
    }
]

for testCase in testCases:
    print('')

    arr = testCase["arr"]
    expected = testCase["expected"]

    s = Solution()

    result = s.isTrionic(arr)
    print(arr, result)
    assert result == expected, f"result {result} should be expected: {expected}"


'''
0 < p < q < n-1

0, p, q , n-1

'''