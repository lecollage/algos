from typing import List

#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixes = {
            0: -1
        }

        prefixSum = 0

        for i, el in enumerate(nums):
            prefixSum += el
            mod = prefixSum % k

            if mod in prefixes:
                if i - prefixes[mod] >= 2:
                    return True
            else: 
                prefixes[mod] = i
            
        return False
            

# @lc code=end

'''
{
0:1
1:1
2:1
}
'''

inputs = [
    [
        [23,2,4,6,7],
        6,
        True
    ],
    [
        [23,2,6,4,7],
        6,
        True
    ],
    [
        [23,2,6,4,7],
        13,
        False
    ],
    [
        [6,0],
        6,
        True
    ],
    [
        [0,6,],
        6,
        True
    ],
    [
        [0],
        6,
        False
    ]
]

s = Solution()
for [arr1, target, expect] in inputs:
    res = s.checkSubarraySum(arr1, target)
    print(res==expect, res)

