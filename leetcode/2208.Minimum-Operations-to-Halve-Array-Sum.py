from typing import List, Optional

from collections import deque
from heapq import *
#
# @lc app=leetcode id=2208 lang=python3
#
# 2208. Minimum Operations to Halve Array Sum
#

# @lc code=start
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        arrSum = 0

        for n in nums:
            arrSum += n

        treshold = arrSum / 2

        nums = [-n for n in nums]

        heapify(nums)

        # print(nums, arrSum)

        count = 0

        while arrSum > treshold:
            el = abs(heappop(nums))
            diff = el / 2
            
            heappush(nums, -diff)

            count += 1
            arrSum -= diff
            # print(nums, arrSum, diff)

        return count
# @lc code=end

adjLists = [
    [
        [5,19,8,1],
        3,
    ],
    [
        [3,8,20],
        3,
    ],
    [
        [],
        0,
    ],
]

for [arr, expect] in adjLists:
    s = Solution()
    res = s.halveArray(arr)
    print(res == expect, res)
    print('')
    print('')
    print('')
