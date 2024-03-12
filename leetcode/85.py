from typing import List

class Solution:
    def getMaxAreaInHistogram(self, heights: List[int]) -> int:
        stack = [-1]
        heights.append(-1)
        maxArea = 0

        for i, height in enumerate(heights): 
            while heights[stack[-1]] > height:
                maxArea = max(maxArea, heights[stack.pop()] * (i - stack[-1] - 1))

            stack.append(i)

        return maxArea

    def maximalRectangle(self, matrix: List[List[int]]) -> int:
        dp = [0] * len(matrix[0])
        maxArea = 0

        for i in range(0, len(matrix)):
            # currLine: List[int] = [eval(k) for k in matrix[i]]

            for j, el in enumerate(matrix[i]):
                el = eval(el)

                if el != 0:
                    dp[j] += el
                else:
                    dp[j] = 0

            # print(i, dp)
            maxArea = max(self.getMaxAreaInHistogram([*dp]), maxArea)

        return maxArea

inputs = [
    [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","1","1","0"],
        ["1","0","1","1","0"],
        ["1","0","0","1","0"],
        ["0","1","1","1","0"],
    ],
    # [
    #     ["0"]
    # ],
    [
        ["1"]
    ],
]
s = Solution()
for input in inputs:
    print(s.maximalRectangle(input))