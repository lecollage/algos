from typing import List, Optional

from collections import deque
#
# @lc app=leetcode id=1438 lang=python3
#
# 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        qMin = deque() # q[0] 1,4,5 -> indexes
        qMax = deque() # q[0] 5,2,1 -> indexes
        l = 0
        maxWindowLen = 1

        for r in range(n):
            # add r to qMax
            while len(qMax) > 0 and qMax[-1] < nums[r]:
                qMax.pop()

            qMax.append(nums[r])

            # add r to qMin
            while len(qMin) > 0 and qMin[-1] > nums[r]:
                qMin.pop()

            qMin.append(nums[r])

            # check while window is not good, move left
            while qMax[0] - qMin[0] > limit:
                if qMax[0] == nums[l]:
                    qMax.popleft()

                if qMin[0] == nums[l]:
                    qMin.popleft()

                l += 1

            # print(l, r)

            maxWindowLen = max(maxWindowLen, r-l+1)

        return maxWindowLen
# @lc code=end

'''
min, max -> 2 deque
len(window) -> 2 pointers: right - left



[8,2,4,7]
8 2 

4,2,2,2,4,5

5,4,4,2,2



max, min
'''

adjLists = [
    [
        [8,2,4,7],
        4,
        2
    ],
    [
        [10,1,2,4,7,2],
        5,
        4
    ],
    [
        [4,2,2,2,4,4,2,2],
        0,
        3
    ],
    [
        [8,7,4,2,8,1,7,7],
        8,
        8
    ],
    
]

for [nums, limit, expect] in adjLists:
    s = Solution()
    res = s.longestSubarray(nums, limit)
    print(res == expect, res)
    print('')
    print('')
    print('')
