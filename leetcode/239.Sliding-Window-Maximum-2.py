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

        for i in range(k): # 0..k-1
            el = nums[i]

            while len(stack) > 0 and el > stack[-1][0]:
                stack.pop()

            stack.append((nums[i], i))

        answer.append(stack[0][0])

        print(stack)

        i = k

        while i < n: # k..n-1
            el = nums[i]
            # print(i, 'BEFORE', stack,  el, i-k)

            while len(stack) > 0 and el > stack[-1][0]:
                x = stack.pop()
                # print(i, 'POPPED-1', x)

            while len(stack) > 0 and i-k >= stack[0][1]:
                x = stack.pop(0)
                # print(i, 'POPPED-2', x)

            stack.append((nums[i], i))
            answer.append(stack[0][0])
            # print(i, 'AFTER', stack)
            # print()

            i+=1

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
        [1,3,1,2,0,5],
        3,
        [3,3,2,5]
    ]
]

for [nums, k, expect] in adjLists:
    s = Solution()
    res = s.maxSlidingWindow(nums, k)
    print(res == expect, res)
    print('')
    print('')
    print('')
