from typing import Optional, List

#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False for i in range(0, len(nums))]

        dp[-1] = True

        for i in range(len(nums)-2, -1, -1):
            value = False

            j = i

            while not value and j < i + nums[i] + 1:
                value = value or dp[j]
                j = j + 1

            dp[i] = value

        return dp[0]

# @lc code=end


inputs = [
    [
        [2,3,1,1,4],
        True
    ],
    [
        [3,2,1,0,4],
        False
    ],
    [
        [0,0],
        False
    ],
    [
        [1,0],
        False
    ],
]
s = Solution()
for [arr, expected] in inputs:
    res = s.canJump(arr)
    print(res == expected)