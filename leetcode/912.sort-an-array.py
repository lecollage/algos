from typing import List

#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start
class Solution:
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        sorted = []

        i=0
        j=0

        while i < len(left) or j < len(right):
            if i >= len(left):
                sorted.append(right[j])
                j = j + 1
                continue

            if j >= len(right):
                sorted.append(left[i])
                i = i + 1
                continue

            if left[i] <= right[j]:
                sorted.append(left[i])
                i = i + 1
            else:
                sorted.append(right[j])
                j = j + 1

        return sorted

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        
        if len(nums) == 1:
            return nums

        middle = int(len(nums)/2)

        return self.merge(self.sortArray(nums[0:middle]), self.sortArray(nums[middle:len(nums)]))
        
# @lc code=end

# inputs = [
#     [
#         [1],
#         [0]
#     ],
# ]

# s = Solution()
# for [arr1, arr2] in inputs:
#     res = s.merge(arr1, arr2)
#     print(res)


inputs = [
    [
        [5,2,3,1]
    ],
    [
        [5,1,1,2,0,0]
    ]
]

s = Solution()
for [arr1] in inputs:
    res = s.sortArray(arr1)
    print(res)
