from typing import List

#
# @lc app=leetcode id=2215 lang=python3
#
# [2215] Find the Difference of Two Arrays
#

# @lc code=start
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        # print(set1.difference(set2))
        # print(set2.difference(set1))

        return [set1.difference(set2), set2.difference(set1)]

# @lc code=end

inputs = [
    [
        [1,2,3],
        [2,4,6]
    ],
]

s = Solution()
for [arr1, arr2] in inputs:
    res = s.findDifference(arr1, arr2)
    print(res)
