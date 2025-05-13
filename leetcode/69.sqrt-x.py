#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def isGood(self, n: int, x: int) -> bool:
        return n<=x

    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        l = 0
        r = x

        while l+1 < r:
            m = int((l+r)/2)

            if self.isGood(m*m, x):
                l = m
            else:
                r = m

        return l
                

# @lc code=end



inputs = [
    [
        9, 3
    ],
    [
        10, 3
    ],
    [
        4, 2
    ],
    [
        1, 1
    ],
    [
        0, 0
    ],
    [
        2, 1
    ],
    [
        65, 8
    ],
    [
        80, 8
    ],
    [
        81, 9
    ],
]
s = Solution()
for [target, expected] in inputs:
    res = s.mySqrt(target)
    print(res == expected, res, target)