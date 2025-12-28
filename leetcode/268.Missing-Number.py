#
# @lc app=leetcode id=1832 lang=python3
#
# 1832. Check if the Sentence Is Pangram
#

from typing import List

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)

        for i in range(len(nums)+1):
            if i not in nums_set:
                return i
            
        return -1
# @lc code=end

inputs = [
    [
        [3,0,1], 
        2
    ],
    [
        [0,1], 
        2
    ],
    [
        [9,6,4,2,3,5,7,0,1], 
        8
    ],
]

for [words, expected] in inputs:
    solution = Solution()
    res = solution.missingNumber(words)
    print(res == expected, res, words)