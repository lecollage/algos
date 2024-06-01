from typing import List, Optional

#
# @lc app=leetcode id=1905 lang=python3
#
# [1905] Count Sub Islands
#

# @lc code=start
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def explore(startI: int, startJ: int, grid1: List[List[int]], grid2: List[List[int]]) -> bool:
            stack = [[startI,startJ]]

            res = True

            while len(stack) > 0:
                i, j = stack.pop()

                if grid1[i][j] != 1:
                    res = False

                if i > 0 and grid2[i-1][j] == 1:
                    stack.append([i-1,j])

                if i < len(grid2)-1 and grid2[i+1][j] == 1:
                    stack.append([i+1,j])

                if j > 0 and grid2[i][j-1] == 1:
                    stack.append([i,j-1])

                if j < len(grid2[i])-1 and grid2[i][j+1] == 1:
                    stack.append([i,j+1])

                grid2[i][j] = 0

            return res

        count = 0

        for i in range(0, len(grid2)):
            for j in range(0, len(grid2[i])):
                if grid2[i][j] == 1:
                    if explore(i,j,grid1, grid2):
                        count += 1

        return count


# @lc code=end

inputs = [
    [
        [
            [1,1,1,0,0],
            [0,1,1,1,1],
            [0,0,0,0,0],
            [1,0,0,0,0],
            [1,1,0,1,1]
        ],
        [
            [1,1,1,0,0],
            [0,0,1,1,1],
            [0,1,0,0,0],
            [1,0,1,1,0],
            [0,1,0,1,0]
        ],
        3,
    ],
    [
        [
            [1,0,1,0,1],
            [1,1,1,1,1],
            [0,0,0,0,0],
            [1,1,1,1,1],
            [1,0,1,0,1]
        ],
        [
            [0,0,0,0,0],
            [1,1,1,1,1],
            [0,1,0,1,0],
            [0,1,0,1,0],
            [1,0,0,0,1]
        ],
        2
    ],
    [
        [
            [1],
        ],
        [
            [1],
        ],
        1
    ],
    [
        [
            [0],
        ],
        [
            [1],
        ],
        0
    ],
    [
        [
            [1],
        ],
        [
            [0],
        ],
        0
    ]
]

s = Solution()
for [grid1,grid2,expect] in inputs:
    res = s.countSubIslands(grid1,grid2)
    print(res==expect, res)


