from typing import List

class Solution:
    def largestRectangleArea(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        maxSquare = 0

        for i in range(0, len(nums)):
            minLength = nums[i]
            stackLeft = []
            stackRight = []
            
            # left direction
            for j in range(i-1, -1, -1):
                if nums[j] >= minLength: 
                    stackLeft.append(nums[j])
                else:
                    break
                

            # right direction
            for j in range(i, len(nums), 1):
                if nums[j] >= minLength:
                    stackRight.append(nums[j])
                else:
                    break

            square = minLength * (len(stackLeft) + len(stackRight))

            if square > maxSquare:
                maxSquare = square

        return maxSquare

inputs = [
    [2,1,5,6,2,3],
    [2,4],
    [2,0,2]
]
s = Solution()
for input in inputs:
    print(s.largestRectangleArea(input))