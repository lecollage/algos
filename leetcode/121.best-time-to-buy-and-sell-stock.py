from typing import Optional, List

#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minPrice = prices[0]

        for i in range(1, len(prices)):
            price = prices[i]
            minPrice = min(price, minPrice)
            profit = max(profit, price - minPrice)

        return profit

        
# @lc code=end


inputs = [
    [
        [7,1,5,3,6,4],
        5
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