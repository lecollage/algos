
from typing import List

class Solution:
   def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        dp = [0 for _ in range(0, len(nums))]
        dp[0]=1

        absoluteMax = 1
        for i in range(1, len(nums)):
            currMax = -10**4-1

            for j in range(i-1, -1, -1):
                if nums[i] > nums[j] and dp[j] > currMax:
                    currMax = dp[j]

            if currMax != -10**4-1:
                dp[i] = currMax+1
                absoluteMax = max([dp[i], absoluteMax])
            else:
                dp[i] = 1


            # print(dp)

        return absoluteMax

        



inputs = [
    [
        [0,1,0,3,2,3],
        4
    ],
    [
        [1,3,6,7,9,4,10,5,6], # 1,3,6,7,9,10
        6,
    ],
    [
        [10,9,2,5,3,7,101,18], # 2,5,7,101 | 2,3,5,6
        4,
    ],
    [
        [5, 2,101,18,19],
        3,
    ],
    [
        [5,3,7,9,8], # 5,7,9
        3,
    ],
    [
        [1,3,2,3],
        3,
    ],
    [
        [1,8,9,2,6,3,4], # 1,2,3,4
        4,
    ],
    [
        [7,7,7,7,7,7,7],
        1,
    ],
    [
        [3,4,2,6],
        3,
    ],
    [
        [6,4,2],
        1,
    ],
    [
        [6],
        1,
    ],
    [
        [1, 2, 0],
        2,
    ],
    [
        [0,1,2],
        3,
    ],
    [
        [-1, 0,1,2],
        4,
    ],
    [
        [-1,-2],
        1,
    ],
    [
        [-2, -1],
        2,
    ],
    [
        [-10**4, -1],
        2,
    ],
    [
        [-10**4, -1, 0, 1, 10**4],
        5,
    ]
]


for _, input in enumerate(inputs):
    solution = Solution()
    print(solution.lengthOfLIS(input[0]) == input[1])

'''
[10,9,2,5,3,7,101,18]

10 9 2 5 3 7 101 18 1
0  1 2 3 4 5 6   7
1  1 1 2 2 3 
10 9 2 5 

10 9 2 2 2 2 2   2
       5 3 3 3   3
           7 7   7
             101 18

0 1 2 3 4 5 6 7 8 9 10

0 1 2 3 4 5 6 7 4 5 6

10^8

10**4
1 + 10**4

[-10**4..-1]..[0..10**4]

0..10**4*2

lengths


0 10
1 9
2 2
3 5
4 3
5 7
6 101
7 18

[0,1,0,3,2,3]


   0 1 2 3 4 5
0  1 
1  
2
3
'''