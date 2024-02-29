from typing import List

class Solution:
    def largestRectangleArea(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        maxSquare = 0
        memo = {}

        for i in range(0, len(nums)):
            minLength = nums[i]
            skipCalc = False

            if minLength in memo.keys():
                indexes = memo[minLength]

                for index in indexes:
                    if i >= index[0] and i <= index[1]:
                        skipCalc = True

            print(skipCalc)

            if not skipCalc: 
                stackLeft = []
                stackRight = []
                
                # left direction
                for j in range(i-1, -1, -1):
                    if nums[j] >= minLength: 
                        stackLeft.append(j)
                    else:
                        break
                    

                # right direction
                for j in range(i, len(nums), 1):
                    if nums[j] >= minLength:
                        stackRight.append(j)
                    else:
                        break

                square = minLength * (len(stackLeft) + len(stackRight))

                if len(stackLeft) > 0 and len(stackRight) > 0:
                    memo[minLength] = [[stackLeft[-1], stackRight[-1]]]

                if square > maxSquare:
                    maxSquare = square

        print(memo)

        return maxSquare

inputs = [
    # [2,1,5,6,2,3],
    # [2,1,5,6,2,3,1,10],
    # [2,4],
    # [2,0,2],
    # [1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,9,10,10,10,10,10,10,10,10,10,10,11,11,11,11,11,11,11,11,11,11,12,12,12,12,12,12,12,12,12,12,13,13,13,13,13,13,13,13,13,13,14,14,14,14,14,14,14,14,14,14,15,15,15,15,15,15,15,15,15,15,16,16,16,16,16,16,16,16,16,16,17,17,17,17,17,17,17,17,17,17,18,18,18,18,18,18,18,18,18,18,19,19,19,19,19,19,19,19,19,19,20,20,20,20,20,20,20,20,20,20,21,21,21,21,21,21,21,21,21,21,22,22,22,22,22,22,22,22,22,22,23,23,23,23,23,23,23,23,23,23,24,24,24,24,24,24,24,24,24,24,25,25,25,25,25,25,25,25,25,25,26,26,26,26,26,26,26,26,26,26,27,27,27,27,27,27,27,27,27,27,28,28,28,28,28,28,28,28,28,28,29,29,29,29,29,29,29,29,29,29,30,30,30,30,30,30,30,30,30,30,31,31,31,31,31,31,31,31,31,31,32,32,32,32,32,32,32,32,32,32,33,33,33,33,33,33,33,33,33,33,34,34,34,34,34,34,34,34,34,34,35,35,35,35,35,35,35,35,35,35,36,36,36,36,36,36,36,36,36,36,37,37,37,37,37,37,37,37,37,37,38,38,38,38,38,38,38,38,38,38,39,39,39,39,39,39,39,39,39,39,40,40,40,40,40,40,40,40,40,40],
]
s = Solution()
for input in inputs:
    print(s.largestRectangleArea(input))