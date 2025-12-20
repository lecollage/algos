from typing import List, Optional

from collections import deque
#
# @lc app=leetcode id=496 lang=python3
#
# 496. Next Greater Element I
#
#
# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2Map = {}
        stack = []

        for i in range(len(nums2)-1, -1, -1):
            while len(stack) > 0 and stack[-1] < nums2[i]:
                stack.pop()

            nums2Map[nums2[i]] = -1 if len(stack) == 0 else stack[-1]
            stack.append(nums2[i])
        
        # print(nums2Map)
        
        answer = []

        for el in nums1:
            answer.append(nums2Map[el])

        return answer
# @lc code=end

'''
'''

adjLists = [
    [
        [4,1,2],
        [1,3,4,2],
        [-1,3,-1]
    ],
    [
        [2,4],
        [1,2,3,4],
        [3,-1]
    ],
]

for [nums1, nums2, expect] in adjLists:
    s = Solution()
    res = s.nextGreaterElement(nums1, nums2)
    print(res == expect, res)
    print('')
    print('')
    print('')
