from typing import List, Optional

from collections import deque
from heapq import *
#
# @lc app=leetcode id=1046 lang=python3
#
# 1046. Last Stone Weight
#

# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        preparedStones = []

        for s in stones:
            preparedStones.append(-s)

        heapify(preparedStones)

        # print(preparedStones)

        while(len(preparedStones)>1):
            stone1 = heappop(preparedStones)
            stone2 = heappop(preparedStones)

            stoneResult = abs(stone1) - abs(stone2)

            # print(stone1, stone2, stoneResult)

            if stoneResult > 0:
                heappush(preparedStones, -stoneResult)

            print(preparedStones)

        return 0 if len(preparedStones) == 0 else abs(heappop(preparedStones))
# @lc code=end

adjLists = [
    [
        [2,7,4,1,8,1],
        1,
    ],
    [
        [1],
        1,
    ],
    [
        [],
        0,
    ],
]

for [arr, expect] in adjLists:
    s = Solution()
    res = s.lastStoneWeight(arr)
    print(res == expect, res)
    print('')
    print('')
    print('')
