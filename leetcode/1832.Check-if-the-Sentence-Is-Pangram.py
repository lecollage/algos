#
# @lc app=leetcode id=1832 lang=python3
#
# 1832. Check if the Sentence Is Pangram
#

from typing import List

# @lc code=start
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
        
# @lc code=end

inputs = [
    [
        "thequickbrownfoxjumpsoverthelazydog", 
        True
    ],
    [
        "leetcode", 
        False
    ],
]

for [words, expected] in inputs:
    solution = Solution()
    res = solution.checkIfPangram(words)
    print(res == expected, res, words)