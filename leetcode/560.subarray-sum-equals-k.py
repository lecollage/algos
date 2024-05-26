from typing import List
#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 1 if nums[0] == target else 0

        count = 0

        for i, el in enumerate(nums):        
            currSum = 10**8
            j = i

            while j < len(nums):
                if currSum == 10**8:
                    currSum = nums[j]
                else: 
                    currSum = currSum + nums[j]

                if currSum == target:
                    count = count+1

                j = j + 1

        # print(queue)

        return count
# @lc code=end



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