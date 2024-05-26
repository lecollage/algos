#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start
class Solution:
    def isGood(self, floors: int, maxCoins: int) -> int:
        return (1+floors)*floors/2 <= maxCoins

    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n

        while left < right-1:
            middle = int((left + right)/2)

            if self.isGood(middle, n):
                left = middle
            else:
                right = middle

        return left

        
# @lc code=end

inputs = [
    [
        5,
        2
    ],
    [
        8,
        3
    ],
    [
        1,
        1
    ],
    [
        10,
        4
    ],

]

for [arr, expect] in inputs:
    solution = Solution()
    res = solution.arrangeCoins(arr)
    print(res == expect, res)
