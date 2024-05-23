#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

pick = 2

def guess(num: int) -> int:
    if num > pick:
        return -1
    
    if num < pick:
        return 1
    
    if num == pick:
        return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while right - left > 0:
            middle = int((left + right) / 2)
            res = guess(middle)

            if res == 0:
                return middle

            if res == 1 or res == 0:
                left = middle+1
            else:
                right = middle-1

        return left



# @lc code=end



inputs = [
    [
       2,
       2,
       2
    ],
]

s = Solution()
for [n, target, expected] in inputs:
    res = s.guessNumber(n)
    print(res == expected, res)