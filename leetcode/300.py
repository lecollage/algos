from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        minEl = min(nums)
        maxEl = max(nums)

        dp = [0 for _ in range(0, maxEl+1)]

        for i, el in enumerate(nums):
            maxLength = dp[el]
            found = False

            for j in range(el-1, -1, -1):
                # print(j, el, dp[j], dp[el], maxLength)
                if dp[j] >= maxLength:
                    maxLength = dp[j]
                    found = True

            if found:
                dp[el] = maxLength + 1
            else:
                dp[el] = 1
            # print(dp)

        return max(dp)

inputs = [
    [
        [1,3,6,7,9,4,10,5,6], # 1,3,6,7,9,10
        6,
    ],
    [
        [10,9,2,5,3,7,101,18], # 2,5,7,101 | 2,3,5,6
        4,
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
        [1,8,9,2,6,3,4],
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

'''