from typing import List

#
# @lc app=leetcode id=554 lang=python3
#
# [554] Brick Wall
#

# @lc code=start
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        intersections = [
            # [0 for _ in row] for row in wall
        ]

        maxLen = 1
        
        for row in wall:
            maxLen = max(maxLen, len(row))

            intersectRow = []

            for i in range(0, len(row)):
                el = row[i]

                for _ in range(0, el-1, 1):
                    intersectRow.append(1)
                
                if i == len(row)-1:
                    intersectRow.append(1)
                else:
                    intersectRow.append(0)

            intersections.append(intersectRow)

        if maxLen == 1:
            return len(wall)

        width = len(intersections[0])

        minSum = 10**4

        for i in range(0, width):
            count = 0

            for row in intersections:
                if row[i] == 1:
                    count = count+1

            minSum = min(minSum, count)

        # print(intersections)
        # print(minSum)

        return minSum
# @lc code=end


inputs = [
    [
        [
            [1,2,2,1],
            [3,1,2],
            [1,3,2],
            [2,4],
            [3,1,2],
            [1,3,1,1]
        ],
        2
    ],
    [
        [
            [1],
            [1],
            [1]
        ],
        3
    ],
    [
        [
            [1,1],
            [2],
            [1,1]
        ],
        1
    ]

]

s = Solution()
for [arr1, expect] in inputs:
    res = s.leastBricks(arr1)
    print(res==expect)


'''
[1,2,2,1],
[3,1,2],
[1,3,2],
[2,4],
[3,1,2],
[1,3,1,1]

010101


-++--+
 01010
122334

 010102,2
 11001
 01101
 10111
 11001
 01100

[1,2,2,1] -> 01010
[3,1,2]   -> 11001
[1,3,2],  -> 01101

i == i -> +1

[
    [0, 1, 0, 1, 0, 0],
    [1, 1, 0, 0, 1, 0],
    [0, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 0]
]

'''


'''
[1,2,2,1],
[3,1,2],
[1,3,2],
[2,4],
[3,1,2],
[1,3,1,1]


[1,2,2,1]

i == 1
1,1*el-1

1010101
1110011

            [1,1],
            [2],
            [1,1]

1

'''