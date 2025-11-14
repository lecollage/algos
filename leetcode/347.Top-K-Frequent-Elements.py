from typing import List, Optional

from collections import deque
from math import *
from heapq import *
#
# @lc app=leetcode id=347 lang=python3
#
# 347. Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}

        for n in nums:
            if n in m:
                m[n] = m[n] + 1
            else:
                m[n] = 1

        print(m)

        top = []

        for key in m:
            print(key)

# @lc code=end

adjLists = [
    [
        [1,1,1,2,2,3],
        12,
        [1,2]
    ],
    [
        [1],
        1,
        [1]
    ],
    [
        [1,2,1,2,1,2,3,1,3,2],
        2,
        [1,2]
    ],
    [
        [1,1,1,2,2,5,5,5,6,6,6,6],
        3,
        [6,1,5]
    ],
]

for [arr, k, expect] in adjLists:
    s = Solution()
    res = s.topKFrequent(arr, k)

    print(res == expect, res)
    print('')
    print('')
    print('')
