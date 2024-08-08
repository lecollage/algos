#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#

from typing import List

# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        def swap(nums: List[int], l: int, r: int) -> List[int]:
            buf = nums[l]
            nums[l] = nums[r]
            nums[r] = buf

            return nums

        l = 0
        r = len(nums)-1

        while r-l>=0:
            # print(l, r)
            isLeftEven = nums[l] % 2 == 0
            isRightEven = nums[r] % 2 == 0
            # print(isLeftEven, isRightEven)

            isLeftOdd = not isLeftEven
            isRightOdd = not isRightEven

            if isLeftEven and isRightEven:
                l = l+1
            elif isLeftOdd and isRightOdd:
                r = r-1
            elif isLeftOdd and isRightEven:
                nums = swap(nums, l,r)
                l = l+1
                r = r-1
            else:
                l = l+1
                r = r-1

        return nums

# @lc code=end

inputs = [
    [
        [3,1,2,4], 
    ],
    [
        [3,4,2,4], 
    ],
    [
        [3,4,1,4], 
    ],
    [
        [1,1,0], 
    ],
    [
        [3,4,3,1], 
    ],
]

for [nums] in inputs:
    solution = Solution()
    res = solution.sortArrayByParity(nums)
    print(res)