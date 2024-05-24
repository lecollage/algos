from typing import List

#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        overallProfit = 0
        profit = 0
        minPrice = prices[0]

        prices.append(-1)

        for i in range(1, len(prices)):
            price = prices[i]
            minPrice = min(minPrice, price)
            newProfit = price-minPrice

            if newProfit < profit:
                overallProfit = overallProfit + profit
                profit = 0
                minPrice = price
            else:
                profit = newProfit

        return overallProfit

# @lc code=end
inputs = [
    [
        [7,1,5,3,6,4],
        7
    ],
    [
        [1,2,3,4,5],
        4
    ],
    [
        [7,6,4,3,1],
        0
    ],
]
s = Solution()
for [arr, expected] in inputs:
    res = s.maxProfit(arr)
    print(res == expected, res, arr)
