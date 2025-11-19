from typing import List, Optional

from collections import deque
from heapq import *
from math import *
#
# @lc app=leetcode id=973 lang=python3
#
# 973. K Closest Points to Origin
#

# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(sqrt((0 - x)**2 + (0 - y)**2), [x, y]) for (x,y) in points]

        # print(distances)

        heapify(distances)

        result = []

        for _ in range(0, k):
            result.append(heappop(distances)[1])

        return result
# @lc code=end

adjLists = [
    [
        [[1,3],[-2,2]],
        1,
        [[-2,2]],
    ],
    [
        [[3,3],[5,-1],[-2,4]],
        2,
        [[3,3],[-2,4]],
    ],
]

for [points, k, expect] in adjLists:
    s = Solution()
    res = s.kClosest(points, k)
    print(res == expect, res)
    print('')
    print('')
    print('')
