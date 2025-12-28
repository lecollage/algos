#
# @lc app=leetcode id=2351 lang=python3
#
# 2351. First Letter to Appear Twice
#

from typing import List

# @lc code=start
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dict = set()

        for el in s:
            if el in dict:
                return el
            
            dict.add(el)
        
        return ''
        
# @lc code=end

inputs = [
    [
        "abccbaacz", 
        "c"
    ],
    [
        "abcdd", 
        "d"
    ],
]

for [words, expected] in inputs:
    solution = Solution()
    res = solution.repeatedCharacter(words)
    print(res == expected, res, words)