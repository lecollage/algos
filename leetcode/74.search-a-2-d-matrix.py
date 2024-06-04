from typing import List, Optional

#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchI(self, matrix: List[List[int]], target: int) -> int:
        top = 0
        bottom = len(matrix)-1

        while bottom-top>1:
            middle=top+int((bottom-top)/2)

            # print(middle)

            row = matrix[middle]

            if row[0] <= target and row[-1] >= target:
                return middle


            if row[0] < target:
                top = middle

            if row[-1] > target:
                bottom = middle

        # print(top, bottom)

        if matrix[top][0] <= target and matrix[top][-1] >= target:
            return top
        
        if matrix[bottom][0] <= target and matrix[bottom][-1] >= target:
            return bottom
        
        return -1

    def searchJ(self, arr: List[int], target: int) -> bool:
        left = 0
        right = len(arr)-1

        while right-left>1:
            middle=left+int((right-left)/2)

            # print(middle)

            if arr[middle] == target:
                return middle

            if arr[middle] < target:
                left = middle+1

            if arr[middle] > target:
                right = middle-1

        # print(top, bottom)

        if arr[left] == target or arr[right] == target:
            return True
        
        return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = self.searchI(matrix, target)

        if i < 0:
            return False

        return self.searchJ(matrix[i], target)
        
# @lc code=end

inputsSearchI = [
    [
        [
            [1,3,5,7],
            [10,11,16,20],
            [23,30,34,60]
        ],
        23,
        2
    ],
    [
        [
            [1,3,5,7],
            [10,11,16,20],
            [23,30,34,60]
        ],
        1,
        0
    ],
    [
        [
            [1,3,5,7],
            [10,11,16,20],
            [23,30,34,60]
        ],
        0,
        -1
    ],
    [
        [
            [1,3,5,7],
            [10,11,16,20],
            [23,30,34,60]
        ],
        8,
        -1
    ],
    [
        [
            [1,3,5,7],
            [10,11,16,20],
            [23,30,34,60]
        ],
        21,
        -1
    ],
    [
        [
            [1,3,5,7],
            [10,11,16,20],
            [23,30,34,60]
        ],
        61,
        -1
    ],
]

# s = Solution()
# for [matrix, target, expect] in inputsSearchI:
#     res = s.searchI(matrix, target)
#     print(res==expect)


inputsSearchJ = [
    [
        [
            [1,3,5,7],
            [10,11,16,20],
            [23,30,34,60]
        ],
        23,
        True
    ],
    [
        [
            [1,3,5,7],
            [10,11,16,20],
            [23,30,34,60]
        ],
        1,
        True
    ],
    [
        [
            [1,3,5,7],
            [10,11,16,20],
            [23,30,34,60]
        ],
        0,
        False
    ],
    [
        [
            [1,3,5,7],
            [10,11,16,20],
            [23,30,34,60]
        ],
        8,
        False
    ],
    [
        [
            [1,3,5,7],
            [10,11,16,20],
            [23,30,34,60]
        ],
        21,
        False
    ],
    [
        [
            [1,3,5,7],
            [10,11,16,20],
            [23,30,34,60]
        ],
        61,
        False
    ],
]


s = Solution()
for [matrix, target, expect] in inputsSearchJ:
    res = s.searchMatrix(matrix, target)
    print(res==expect)

