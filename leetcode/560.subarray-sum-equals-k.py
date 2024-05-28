from typing import List
#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], target: int) -> int:
        count = 0
        prefixSum = 0
        prefixes = {
            0:1
        }

        for el in nums:
            prefixSum += el
            diff = prefixSum-target

            count += prefixes.get(diff, 0)
            prefixes[prefixSum] = prefixes.get(prefixSum, 0) + 1

        return count

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
        [1,1,1],
        2,
        2
    ],
    [
        [1,2,3],
        3,
        2
    ],
    [
        [1,2,3,1,2,3],
        6,
        4
    ],
    [
        [1,2,3,7,1,2,3],
        6,
        2
    ],
    [
        [1],
        0,
        0
    ],
    [
        [-1,-1,1],
        0,
        1
    ],
    [
        [1,-1,0],
        0,
        3
    ],
]

s = Solution()
for [arr1, target, expect] in inputs:
    res = s.subarraySum(arr1, target)
    print(res==expect, res)



# nums = [7,2,3]
# print(nums.pop(0))