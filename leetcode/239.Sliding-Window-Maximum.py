from typing import List, Optional

from collections import deque
#
# @lc app=leetcode id=239 lang=python3
#
# 239. Sliding Window Maximum
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        answer = []
        stack = []

        for i in range(k):
            while len(stack) > 0 and stack[-1] < nums[i]:
                stack.pop()
            
            stack.append(nums[i])

            # print(i, stack)

        answer.append(stack[0])

        for i in range(k, n, 1):
            while len(stack) > 0 and (stack[-1] < nums[i] or len(stack) >= k):
                stack.pop()
            
            stack.append(nums[i])
            answer.append(stack[0])

        return answer
# @lc code=end

adjLists = [
    [
        [1,3,-1,-3,5,3,6,7],
        3,
        [3,3,5,5,6,7]
    ],
    [
        [1],
        1,
        [1]
    ],
    [
        [1,-1],
        1,
        [1,-1]
    ],
    [
        [7,2,4],
        2,
        [7,7]
    ],
    
]

for [nums, k, expect] in adjLists:
    s = Solution()
    res = s.maxSlidingWindow(nums, k)
    print(res == expect, res)
    print('')
    print('')
    print('')
