from typing import List, Optional

from collections import deque
from math import *
from heapq import *
#
# @lc app=leetcode id=338 lang=python3
#
# 338. Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)

        if n == 0:
            return dp

        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i >> 1] + i & 1# 0/1

        # i//2 -> число

        return dp
# @lc code=end


'''
       0
       1
      10
      11
     100
     101
     110
     111
    1000
    1001
    1010
'''

adjLists = [
    [
        2,
        [0,1,1],
    ],
    [
        5,
        [0,1,1,2,1,2],
    ],
]

for [k, expect] in adjLists:
    s = Solution()
    res = s.countBits(k)

    print(res == expect, res)
    print('')
    print('')
    print('')
