from typing import List, Optional

from collections import deque
from math import *
from heapq import *
#
# @lc app=leetcode id=410 lang=python3
#
# 410. Split Array Largest Sum
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[float("inf")] * (k+1) for _ in range(n+1)]
        prefix = [0] * (n+1)

        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + nums[i-1]

        # base case
        dp[0][0] = float("-inf")

        for i in range(1, n+1):
            for j in range(1, k+1):
                for t in range(j-1, i):
                    # dp[i][j] = min(max(dp[t][j-1], sum(nums[t:i])), dp[i][j])
                    dp[i][j] = min(max(dp[t][j-1], prefix[i]-prefix[t]), dp[i][j])

                    if dp[t][j-1] >= dp[i][j]: # optimisation in case of non-negative numbers
                        break

        return dp[n][k]
# @lc code=end
'''
[7,2,5,10,8]
0..k
'''

adjLists = [
    [
        [7,2,5,10,8],
        2,
        18
    ],
    [
        [1,2,3,4,5],
        2,
        9
    ]
]

for [arr, k, expect] in adjLists:
    s = Solution()
    res = s.splitArray(arr, k)

    print(res == expect, res)
    print('')
    print('')
    print('')
