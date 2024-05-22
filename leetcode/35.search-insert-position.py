from typing import List

#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while (right - left) > 1:
            middle = left + int((right - left)/2)

            if target >= nums[middle]: 
                left = middle
            else: 
                right = middle
        
        if target > nums[right]:
            return right+1
        
        if target > nums[left]:
            return left + 1
        
        return left

# @lc code=end



inputs = [
    [
       [1,3,5,6],
       5,
       2
    ],
    [
       [1,3,5,6],
       2,
       1
    ],
    [
       [1,3,5,6],
       7,
       4
    ],
    [
       [1,3,5,6],
       0,
       0
    ],
]
s = Solution()
for [arr, target, expected] in inputs:
    res = s.searchInsert(arr, target)
    print(res == expected, res)