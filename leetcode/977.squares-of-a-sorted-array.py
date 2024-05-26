from typing import List

#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i=0

        left = 0
        right = len(nums)

        while left < right:
            middle = int((left+right)/2) 

            if nums[middle] <= 0:
                left = middle + 1
            else:
                right = middle

        # print(right)

        i = right

        j=i-1

        arr = []

        while j >= 0 and i < len(nums):
            if nums[i] < (-1*nums[j]):
                arr.append(nums[i]**2)
                i+=1
            else:
                arr.append((-1*nums[j])**2)
                j-=1

            # print(arr)

        while i < len(nums):
            arr.append(nums[i]**2)
            i+=1

        while j >= 0:
            arr.append((-1*nums[j])**2)
            j-=1

        # print(arr)

        return arr
       
        
# @lc code=end

s = Solution()
print(s.sortedSquares([-7,-3,2,3,11]))
print(s.sortedSquares([0,2,3,11]))
print(s.sortedSquares([-4,-1,0,3,10]))
print(s.sortedSquares([-4,-1]))
print(s.sortedSquares([-1]))



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