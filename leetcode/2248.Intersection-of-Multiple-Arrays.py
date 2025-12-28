#
# @lc app=leetcode id=1832 lang=python3
#
# 1832. Check if the Sentence Is Pangram
#

from typing import List

# @lc code=start
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans = []
        dict = {}
        n = len(nums)

        for arr in nums:
            for el in arr:
                if el in dict:
                    dict[el] = dict[el] + 1
                else:
                    dict[el] = 1

                if dict[el] == n:
                    ans.append(el)

        ans.sort()

        return ans
# @lc code=end

inputs = [
    [
        [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], 
        [3,4]
    ],
    [
        [[1,2,3],[4,5,6]], 
        []
    ],
]

for [words, expected] in inputs:
    solution = Solution()
    res = solution.intersection(words)
    print(res == expected, res, words)