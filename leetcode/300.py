from typing import List

class Solution:
    cache = {}

    def calc(self, nums: List[int], startFrom: int) -> int:
        if startFrom in self.cache:
            return self.cache[startFrom]

        maxLength = 1

        for i in range(startFrom, len(nums)):
            if nums[i] > nums[startFrom]:
                length = self.calc(nums, i)+1

                if length > maxLength:
                    maxLength = length

        self.cache[startFrom] = maxLength

        return maxLength

    def lengthOfLIS(self, nums: List[int]) -> int:
        self.cache = {}

        maxLength = 1

        for i in range(0, len(nums)):
            length = self.calc(nums, i)

            if length > maxLength:
                maxLength = length

        # print(self.cache)

        return maxLength

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
        [5,3,7,101,18], # 5,7,101 
        3,
    ],
    [
        [0,1,0,3,2,3],
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