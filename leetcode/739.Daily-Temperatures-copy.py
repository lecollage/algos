from typing import List, Optional

from collections import deque
#
# @lc app=leetcode id=739 lang=python3
#
# 739. Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        if n == 0: 
            return []
        
        days = [0] * n
        stack = []
        
        for d in range(n-1, -1, -1):
            curr_temp = temperatures[d]
            prev_day = -1

            while len(stack) > 0 and stack[-1][0] <= curr_temp:
                stack.pop()

            if len(stack) > 0 and prev_day == -1:
                prev_day = stack[-1][1]

            days[d] = 0 if prev_day < 0 or len(stack) == 0 else prev_day - d
            stack.append((curr_temp, d))

            # print(d, prev_day, stack)

        return days
# @lc code=end

adjLists = [
    [
        [73,74,75,71,69,72,76,73],
        [1,1,4,2,1,1,0,0],
    ],
    [
        [30,40,50,60],
        [1,1,1,0],
    ],
    [
        [30,60,90],
        [1,1,0],
    ],
    [
        [89,62,70,58,47,47,46,76,100,70],
        [8,1,5,4,3,2,1,1,0,0]
    ]
]

for [days, expect] in adjLists:
    s = Solution()
    res = s.dailyTemperatures(days)
    print(res == expect, res)
    print('')
    print('')
    print('')
