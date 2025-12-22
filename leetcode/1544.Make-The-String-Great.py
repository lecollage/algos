from typing import List, Optional

from collections import deque
from heapq import *
#
# @lc app=leetcode id=1544 lang=python3
#
# 1544. Make The String Great
#

# @lc code=start
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for el in s:
            if len(stack) == 0:
                stack.append(el)
            elif stack[-1] != el and el.capitalize() == stack[-1].capitalize():
                stack.pop()
            else:
                stack.append(el)

        return "".join(stack)
# @lc code=end

adjLists = [
    [
        "leEeetcode",
        "leetcode",
    ],
    [
        "abBAcC",
        "",
    ],
    [
        "s",
        "s",
    ],
]

for [path, expect] in adjLists:
    s = Solution()
    res = s.makeGood(path)
        
    print(res == expect, res)
    print('')
    print('')
    print('')
