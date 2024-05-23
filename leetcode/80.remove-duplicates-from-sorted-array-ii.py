from typing import Optional, List

#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        countOfRemovedElements = 0
        i = 0

        while i < len(nums)-countOfRemovedElements-2:
            if nums[i] == nums[i+1] and nums[i+1] == nums[i+2]:
                j = i + 1

                while j < len(nums)-max(1, countOfRemovedElements) and nums[j] == nums[j+1]:
                    j = j + 1
                    countOfRemovedElements = countOfRemovedElements + 1

                j = j + 1
                k = i + 2

                while k < len(nums) and j < len(nums):
                    nums[k] = nums[j]
                    k = k + 1
                    j = j + 1
                    
                
                print(i, countOfRemovedElements)

            i = i + 1

        return len(nums) - countOfRemovedElements


# @lc code=end



inputs = [
    [
        [0,0,0, 1,1,1,1,1,1,1,1, 2,3,3, 5], # [0,0, 1,1, 2,3,3, 5],
        8
    ],
    # [
    #     [1,1,1,2,2,3],
    #     5
    # ],
    # [
    #     [0,0,1,1,1,1,2,3,3],
    #     7
    # ],
    # [
    #     [0,0],
    #     2
    # ],
    # [
    #     [0],
    #     1
    # ],
    # [
    #     [0,0,0],
    #     2
    # ],
    [
        [0,1,2,2,2,2,2,3,4,4,4], #[0,1,2,2,3,4,4]
        7
    ],
    [
        [0,0,0,0,0], #[0,0]
        2
    ],
    
    
]
s = Solution()
for [arr, expected] in inputs:
    res = s.removeDuplicates(arr)
    print(res == expected, res, arr)