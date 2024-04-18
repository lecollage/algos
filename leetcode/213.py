from typing import List

class Solution:
    def rob(self, costs: List[int]) -> int:
        if len(costs) == 1:
            return costs[0]
        
        if len(costs) == 2:
            return max(costs[0], costs[1])

        return max(self.process(costs[:-1]), self.process(costs[1:]))

    def process(self, costs: List[int]) -> int:
        dp = [costs[0], costs[1]]

        for i in range(2, len(costs)):
            buf = dp[0]
            dp[0] = max(dp[0], dp[1])
            dp[1] = buf+costs[i]

        return max(dp)

inputs = [
    [
        [2,3,2],
        3
    ],
    [
        [2],
        2
    ],
    [
        [2,3],
        3
    ]
]

for _, input in enumerate(inputs):
    s = Solution()
    print(s.rob(input[0]) == input[1])