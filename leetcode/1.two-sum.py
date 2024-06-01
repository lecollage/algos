from typing import List
#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, num in enumerate(nums):
            substitution = target - num

            if substitution in hashMap:
                return [hashMap[substitution], i]

            hashMap[num] = i


# inputs = [
#     [
#         [2,7,11,15],
#         9
#     ],
#     [
#         [3,2,4],
#         6
#     ],
#     [
#         [3,3],
#         6
#     ]
# ]

# s = Solution()
# for [arr, target] in inputs:
#     print(s.twoSum(arr, target))



# @lc code=end

