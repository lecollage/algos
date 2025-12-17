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
        q = deque() # min -> max monotonic

        maxQLen = 0

        for i in range(n):
            while len(q) > 0 and q[0] < i:
                q.popleft()

            while len(q) > 0 and q[-1] < i:
                q.pop()

            if len(q) == 0:
                q.append(i)

            j = i + 1
            stop = False
            additional = 0

            while j < n and nums[q[-1]] - nums[q[0]] <= limit and not stop:
                el = nums[j]

                if el <= nums[q[0]] and j != q[0]:
                    if nums[q[-1]] - el <= limit:
                        q.appendleft(j)
                    else:
                        stop = True
                elif el >= nums[q[-1]] and j != q[-1]:
                    if el - nums[q[0]] <= limit:
                        q.append(j)
                    else:
                        stop = True
                elif j != q[-1] and j != q[0] and el < nums[q[-1]] and el > nums[q[0]]:
                    additional += 1

                print(i, j, el, nums[q[-1]], nums[q[0]], additional, q)

                j += 1

            maxQLen = max(maxQLen, len(q) + additional)

            print(i, q, maxQLen)
            print()

        return maxQLen
# @lc code=end

'''
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

for [nums, k, expect] in adjLists:
    s = Solution()
    res = s.longestSubarray(nums, k)
    print(res == expect, res)
    print('')
    print('')
    print('')
