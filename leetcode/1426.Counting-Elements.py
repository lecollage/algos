#
# @lc app=leetcode id=1832 lang=python3
#
# 1832. Check if the Sentence Is Pangram
#

from typing import List

# @lc code=start
class Solution:
    def countElements(self, arr: List[int]) -> int:
        distinctElements = set(arr)
        count = 0

        for el in arr:
            if el+1 in distinctElements:
                count += 1

        return count
# @lc code=end

inputs = [
    [
        [1,2,3], 
        2
    ],
    [
        [1,1,3,3,5,5,7,7], 
        0
    ],
]

for [words, expected] in inputs:
    solution = Solution()
    res = solution.countElements(words)
    print(res == expected, res, words)