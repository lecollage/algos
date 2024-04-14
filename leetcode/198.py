from typing import List
import math

class Solution:
    def rob(self, costs: List[int]) -> int:
        if len(costs) == 1:
            return costs[0]

        if len(costs) == 2:
            return max(costs[0], costs[1])

        dp = [costs[0], costs[1]]

        for i in range(2, len(costs)):
            buf=dp[0]
            dp[0]=max(dp[0], dp[1])
            dp[1]=costs[i]+buf

        return max(dp)