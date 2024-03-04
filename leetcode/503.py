from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = [-1]
        output = [-1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            el = nums[i]

            while len(stack) > 1 and nums[stack[-1]] <= el:
                stack.pop()

            if stack[-1] > -1:
                output[i] = nums[stack[-1]]

            stack.append(i)
        
        return output




inputs = [
    # [1,2,1],
    [1,2,3,4,3], # [2,3,4,-1,-1]
]
s = Solution()
for input in inputs:
    print(s.nextGreaterElements(input))