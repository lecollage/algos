
from typing import List

class Solution:

    def findNumberOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        lenghts = [0 for _ in range(0, len(nums))]
        counts = [1 for _ in range(0, len(nums))]

        lenghts[-1]=1

        for i in range(len(nums)-2, -1, -1):
            currMaxLenIndx = 0
            # currMaxLenIndxes = []
            currCount = 1

            for j in range(i+1, len(nums), 1): 
                if nums[j] >= nums[i]:
                    if nums[j] > nums[i] and lenghts[j] > lenghts[currMaxLenIndx]:
                        currMaxLenIndx = j
                        # currMaxLenIndxes = [j]
                        currCount = counts[j]
                    elif lenghts[j] == lenghts[currMaxLenIndx] or nums[j] == nums[i]:
                        # currMaxLenIndxes.append(j)
                        currCount = currCount + 1

            lenghts[i] = lenghts[currMaxLenIndx] + 1
            counts[i] = currCount
            # print('currMaxLenIndxes', currMaxLenIndxes, currCount)


        # print(lenghts)
        # print(counts)

        return counts[0]

inputs = [
    [
        [1,3,5,4,7], # [1, 3, 4, 7] and [1, 3, 5, 7]
        2
    ],
    [
        [2,2,2,2,2],
        5
    ],
    [
        [2],
        1
    ],
    [
        [2,2],
        1
    ],
    # [
    #     [2],
    #     1
    # ],
    # [
    #     [-2,2,2],
    #     2
    # ],
    # [
    #     [1,2,4,3,5,4,7,2], # 1,2,3,4,7 | 1,2,4,5,7 | 1,2,3,5,7
    #     3
    # ]
]


for _, input in enumerate(inputs):
    solution = Solution()
    res = solution.findNumberOfLIS(input[0])
    print(res, res == input[1])

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