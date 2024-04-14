import math
from typing import List

class Solution:
    def coinChange(self, coins: List[int], targetAmount: int) -> int:
        if targetAmount==0:
            return 0

        dp = [math.inf]*(targetAmount+1)
        dp[0]=0

        for i in range(1, targetAmount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        # print(dp)

        return dp[-1] if dp[-1]!=math.inf else -1
