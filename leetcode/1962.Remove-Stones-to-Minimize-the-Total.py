from typing import List, Optional

from collections import deque
from math import *
from heapq import *
#
# @lc app=leetcode id=1962 lang=python3
#
# 1962. Remove Stones to Minimize the Total
#

# @lc code=start
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        pilesSum = 0

        for pile in piles:
            pilesSum += pile

        piles = [-1 * pile for pile in piles]

        # print(piles)

        heapify(piles)

        for _ in range(0, k):
            pile = -1 * heappop(piles)
            pilesSum -= pile
            # print(pile, ceil(pile / 2))
            pile = ceil(pile / 2)
            pilesSum += pile
            
            heappush(piles, -1 * pile)

        # print(piles)

        return pilesSum
# @lc code=end

adjLists = [
    [
        [5,4,9],
        2,
        12
    ],
    [
        [4,3,6,7],
        3,
        12
    ],
    [
        [4],
        1,
        2
    ],
    [
        [4],
        2,
        1
    ],
    [
        [4],
        3,
        1
    ],
]

for [arr, k, expect] in adjLists:
    s = Solution()
    res = s.minStoneSum(arr, k)

    print(res == expect, res)
    print('')
    print('')
    print('')
