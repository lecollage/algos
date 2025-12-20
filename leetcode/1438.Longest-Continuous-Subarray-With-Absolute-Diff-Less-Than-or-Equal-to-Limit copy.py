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

        maxQLen = 0
        left = 0
        right = 0
        minIndex = 0
        maxIndex = 0

        for i in range(n):
            while right < i:
                right += 1

            j = i + 1
            stop = False

            while j < n and nums[maxIndex] - nums[minIndex] <= limit and not stop:
                if nums[j] <= nums[minIndex]:
                    if nums[j] - nums[minIndex] <= limit:
                        minIndex = j
                        right = j
                    else:
                        stop = True
                elif nums[j] >= nums[maxIndex]:
                    if nums[maxIndex] - nums[j] <= limit:
                        maxIndex = j
                        right = j
                    else:
                        stop = True
                elif nums[j] > nums[minIndex] and nums[j] < nums[maxIndex]:
                    right = j

                print(i, j, left, right, minIndex, maxIndex, maxQLen)

                j += 1

            maxQLen = max(maxQLen, right - i)

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
