#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isGood(self, current: int, target: int):
        return current*current==target

    def isPerfectSquare(self, target: int) -> bool:
        left = 1
        right = target

        while left+1 < right:
            middle = left + int((right-left)/2)

            if middle*middle <= target:
                left = middle
            else:
                right = middle

            # print(left, right)

        return self.isGood(left, target)


        
# @lc code=end

inputs = [
    [1, True],
    [16, True],
    [14, False],
    [100, True],
    [10000, True],
    [2**31-1, False],
    [2147395600, True],
]

for target, expect in inputs:
    s = Solution()
    print(s.isPerfectSquare(target) == expect)

    



