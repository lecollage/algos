from typing import List

#
# @lc app=leetcode id=525 lang=python3
#
# 525. Contiguous Array
#

# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        balances = {0: 0}
        prefixBalance = 0
        arrLen = 0

        for i, n in enumerate(nums):
            if n == 0:
                prefixBalance += 1
            elif n == 1:
                prefixBalance -= 1

            if prefixBalance in balances:
                arrLen = max(arrLen, i - balances[prefixBalance])

            if prefixBalance == 0:
                arrLen = max(arrLen, i+1)

            if prefixBalance not in balances or prefixBalance == 0:
                balances[prefixBalance] = i

        print(balances)

        return arrLen
# @lc code=end

'''
balance: count(0)-count(1)
b: 0  1  0 -1 -2 -3 -4  3  2  1
   0, 0, 1, 1, 1, 1, 1, 0, 0, 0
   


b:  0  1  2  1  0 -1 -2 -3 -2 -1  0 
   -1  0, 0, 1, 1, 1, 1, 1, 0, 0, 0

0:  0  1  2  2  2  2  2  2  3  4  5
1:  0  0  0  1  2  3  4  5  5  5  5

0  1  2  3  4  5  6  7  8
1  0  -1 -2 -4 -5 -4 -3 -2
0, 1, 1, 1, 1, 1, 0, 0, 0

{
  0: 1,
  1: 0,
  -1: 2,
  -2: 3,
  -3: 4,
  -4: 5
}
'''

inputs = [
    [
        [0,1],
        2
    ],
    [
        [0,1,0],
        2
    ],
    [
        [0,1,1,1,1,1,0,0,0],
        6
    ],
]

s = Solution()
for [arr1, expect] in inputs:
    res = s.findMaxLength(arr1)
    print(res==expect, res)

