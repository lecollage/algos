from typing import List, Optional

from collections import deque
#
# @lc app=leetcode id=239 lang=python3
#
# 239. Sliding Window Maximum
#

# @lc code=start



'''
[5, 4, 3, 2, 4...]

q: 5 4 3 2
q: 5 4 3
q: 5 4

q: 5 4 4

q: 4 4

-----------------

max-min<=limit

q: 5 4 3 2
q: 4 3 2
q: 4 4 3 2



'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        answer = []
        q = deque()

        for i in range(k): # 0..k-1
            el = nums[i]

            while len(q) > 0 and el > nums[q[-1]]:
                q.pop()

            q.append(i)

        answer.append(nums[q[0]])

        # print(stack)

        i = k

        while i < n: # k..n-1
            el = nums[i]

            while len(q) > 0 and el > nums[q[-1]]:
                q.pop()

            q.append(i)

            while len(q) > 0 and i-k >= q[0]:
                q.popleft()

            answer.append(nums[q[0]])

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
