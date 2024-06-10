from typing import List

#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []

        left = 0
        right = len(nums)

        while left+1 < right:
            middle = left + (right-left)//2

            if nums[middle] < 0:
                left = middle
            
            if nums[middle] >= 0:
                right = middle

        i = left
        j = left+1
        res = []

        while i > -1 or j < len(nums):
            one = nums[i]**2 if i>-1 else -1
            two = nums[j]**2 if j<len(nums) else -1

            if one == -1:
                res.append(two)
                j+=1
                continue
                
            if two == -1:
                res.append(one)
                i-=1
                continue

            if one < two:
                res.append(one)
                i-=1
            else: 
                res.append(two)
                j+=1

        return res

# @lc code=end

s = Solution()
print(s.sortedSquares([-7,-3,2,3,11]))
print(s.sortedSquares([0,2,3,11]))
print(s.sortedSquares([-4,-1,-1,0,3,10]))
print(s.sortedSquares([-8,-4,-1]))
print(s.sortedSquares([-1]))
print(s.sortedSquares([]))



'''
     j i
[-7,-3,2,3,11]



while j!=0 or i < len(nums):
    if i < len(nums) and nums[i] > (-1*nums[j]):
        arr.append(nums[i])
        i+=1
    elif j>-1:
        arr.append(nums[j])
        j-=1

'''