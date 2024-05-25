from typing import List

#
# @lc app=leetcode id=554 lang=python3
#
# [554] Brick Wall
#

# @lc code=start
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # joints = []
        jointCounts = {}
        maxCount = 0

        for row in wall:
            jointRow = []

            for i in range(0, len(row)-1):
                el = row[i]

                if i == 0:
                    jointRow.append(el)
                else:
                    jointRow.append(el + jointRow[-1])

                if jointRow[-1] in jointCounts:
                    jointCounts[jointRow[-1]] = jointCounts[jointRow[-1]] + 1
                else:
                    jointCounts[jointRow[-1]] = 1

                maxCount = max(jointCounts[jointRow[-1]], maxCount)

            # joints.append(jointRow)

        # print(joints)
        # print(jointCounts)
        # print(maxCount)

        return len(wall) - maxCount
# @lc code=end


inputs = [
    # [
    #     [
    #         [1,2,2,1],
    #         [3,1,2],
    #         [1,3,2],
    #         [2,4],
    #         [3,1,2],
    #         [1,3,1,1]
    #     ],
    #     2
    # ],
    # [
    #     [
    #         [1],
    #         [1],
    #         [1]
    #     ],
    #     3
    # ],
    # [
    #     [
    #         [1,1],
    #         [2],
    #         [1,1]
    #     ],
    #     1
    # ],
    [
        [
            [100000000],
            [100000000],
            [100000000]
        ],
        3
    ]

    

]

s = Solution()
for [arr1, expect] in inputs:
    res = s.leastBricks(arr1)
    print(res==expect, res)


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