from typing import List
import math

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if m == 0 or n == 0:
            return 0
        
        if len(ops) == 0:
            return m * n
        
        minX = math.inf
        minY = math.inf

        for i, operation in enumerate(ops):
            minX = min(operation[0], minX)
            minY = min(operation[1], minY)

        return minX * minY

inputs = [
    [
        3, 3, [
         [2,2],
         [3,3]
        ]
    ],
    [
        3, 3, [
            [2,2],
            [3,3],
            [3,3],
            [3,3],
            [2,2],
            [3,3],
            [3,3],
            [3,3],
            [2,2],
            [3,3],
            [3,3],
            [3,3],
        ]
    ],
    [
        3, 3, 
        []
    ]
]

s = Solution()
for input in inputs:
    print(s.maxCount(input[0], input[1], input[2]))