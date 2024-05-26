#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for el in s:
            if el in [')', ']', '}'] and len(stack) > 0:
                last = stack.pop()

                if last == '(' and el == ')':
                    continue
                elif last == '{' and el == '}':
                    continue
                elif last == '[' and el == ']':
                    continue
                else: 
                    return False
            elif el in [')', ']', '}'] and len(stack) == 0: 
                return False
            else: 
                stack.append(el)
                    
        return len(stack) == 0
        
# @lc code=end

inputs = [
    [
        "()",
        True,
    ],
    [
        "()[]{}",
        True,
    ],
    [
        "(]",
        False,
    ],
    [
        "]",
        False,
    ],
]

s = Solution()
for [arr1, expect] in inputs:
    res = s.isValid(arr1)
    print(res==expect)

