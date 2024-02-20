from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) == 0:
            return []
        
        stack = []
        output = [0] * len(nums2)

        for i in range(len(nums2)-1, -1, -1):
            while (stack and nums2[stack[-1]] <= nums2[i]):
                stack.pop()
            
            output[i] = stack[-1] if stack else len(nums2)
            stack.append(i)
            
        return output



inputs = [
    [2,-1,5,0,2,3]
]
s = Solution()
for input in inputs:
    print(s.nextGreaterElement([1], input))