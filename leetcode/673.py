
from typing import List

class Solution:

    def findNumberOfLIS(self, nums: List[int], startIndex: int = 0, lenght: int = 0) -> int:
        print(startIndex, lenght)

        if startIndex == len(nums)-1:
            return lenght

        lengths = []
        for i in range(startIndex, len(nums)):
            if nums[i] > nums[startIndex]:
                lengths.append(self.findNumberOfLIS(nums, i+1, lenght+1))

        # print(lengths)

        return lenght

inputs = [
    # [
    #     [1,3,5,4,7], # [1, 3, 4, 7] and [1, 3, 5, 7]
    #     2
    # ],
    # [
    #     [2,2,2,2,2],
    #     5
    # ],
    # [
    #     [2],
    #     1
    # ],
    # [
    #     [-2,2,2],
    #     2
    # ],
    [
        [1,2,4,3,5,4,7,2], # 1,2,3,4,7 | 1,2,4,5,7 | 1,2,3,5,7
        3
    ]
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