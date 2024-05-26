from typing import List

#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#

# @lc code=start
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
        
        res = 0

        while len(stack) > 0:
            res += stack.pop()

        return res

        
# @lc code=end

inputs = [
    [
        ["5","-2","4","C","D","9","+","+"],
        27
    ],
  
]

for [arr, expect] in inputs:
    solution = Solution()
    print(solution.calPoints(arr) == expect)
