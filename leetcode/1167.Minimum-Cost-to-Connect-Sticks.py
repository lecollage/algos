from typing import List, Optional

from collections import deque
from math import *
from heapq import *
#
# @lc app=leetcode id=1167 lang=python3
#
# 1167. Minimum Cost to Connect Sticks
#

# @lc code=start
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)

        totalCost = 0

        while len(sticks) > 1:
            x = heappop(sticks)
            y = heappop(sticks)

            totalCost += (x+y)

            heappush(sticks, x+y)

        return totalCost
# @lc code=end

adjLists = [
    [
        [2,4,3],
        14
    ],
    [
        [1,8,3,5],
        30
    ],
    [
        [5],
        0
    ],
]

for [arr, expect] in adjLists:
    s = Solution()
    res = s.connectSticks(arr)

    print(res == expect, res)
    print('')
    print('')
    print('')
