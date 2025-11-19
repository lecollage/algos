from typing import List, Optional

from collections import deque
from heapq import *
#
# @lc app=leetcode id=215 lang=python3
#
# 215. Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-1 * n for n in nums]

        heapify(nums)

        for _ in range(0, k-1):
            heappop(nums)

        return -1 * heappop(nums)
# @lc code=end


adjLists = [
    [
        [3,2,1,5,6,4],
        2,
        5,
    ],
    [
        [3,2,3,1,2,4,5,5,6],
        4,
        4,
    ],
]

for [nums, k, expect] in adjLists:
    s = Solution()
    res = s.findKthLargest(nums, k)
    print(res == expect, res)
    print('')
    print('')
    print('')
