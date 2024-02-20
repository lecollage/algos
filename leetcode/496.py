from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) == 0:
            return []
        
        stack = []
        dict = {}

        for i in range(len(nums2)-1, -1, -1):
            while (stack and nums2[stack[-1]] <= nums2[i]):
                stack.pop()
            
            if stack: 
                dict[nums2[i]] = stack[-1]
            else: 
                dict[nums2[i]] = -1

            stack.append(i)
            
        # print(dict)

        output = [0] * len(nums1)
        for i in range(0, len(nums1)):
            output[i] = nums2[dict[nums1[i]]] if dict[nums1[i]] >= 0 else -1

        return output



inputs = [
    # [[], [2,-1,5,0,2,3]],
    [[4,1,2],[1,3,4,2]],
    [[2,4],[1,2,3,4]],
]
s = Solution()
for input in inputs:
    print(s.nextGreaterElement(input[0], input[1]))