from typing import List

# dp[5] = 6 . . . . 6
# dp[6] = 4 . . . . 2 4




class Solution:
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     offset = 10**4
    #     dp = [0 for _ in range(0, offset*2+1)]

    #     for i, el in enumerate(nums):
    #         maxLength = dp[el]
    #         found = False

    #         currIndx = el + offset

    #         # print(start)

    #         for j in range(currIndx-1, -1, -1):
    #             if dp[j] > 0:
    #                 maxLength = dp[j]
    #                 # print("maxLength", maxLength)
    #                 found = True
    #                 break

    #         if found:
    #             dp[currIndx] = maxLength + 1
    #         else:
    #             dp[currIndx] = 1
    #         print(el, [dp[9998], dp[9999], dp[10000], dp[10001], dp[10002], dp[10003], dp[10004], dp[10005], dp[10006], dp[10007], dp[10018], dp[10101]], max(dp))

    #     return max(dp)

# from typing import List

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         maxEl = max(nums)

#         dp = [0 for _ in range(0, maxEl+1)]

#         for i, el in enumerate(nums):
#             maxLength = dp[el]
#             found = False

#             for j in range(el-1, -1, -1):
#                 # print(j, el, dp[j], dp[el], maxLength)
#                 if dp[j] >= maxLength:
#                     maxLength = dp[j]
#                     found = True

#             if found:
#                 dp[el] = maxLength + 1
#             else:
#                 dp[el] = 1
#             # print(dp)

#         return max(dp)

    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        dp = [0 for _ in range(0, len(nums))]
        dp[len(nums)-1] = 1

        absoluteMax = 0

        for i in range(len(nums)-2, -1, -1):
            maxLength = 0

            for j in range(i, len(nums), 1):
                # print(i, j, nums[i], nums[j], dp)

                if dp[j] > maxLength and nums[i] < nums[j]:
                    maxLength = dp[j]
                    
            dp[i] = maxLength+1

            if dp[i] > absoluteMax:
                absoluteMax = dp[i]
            # print("AFTER ", i, nums[i],  dp)

        # print(dp)

        return absoluteMax


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