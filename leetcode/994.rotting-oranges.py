from typing import List, Optional

#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
1
# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        hasRotting = False
        hasFresh = False

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 2:
                    queue.append([i, j, 0])
                    hasRotting = True
                
                if grid[i][j] == 1:
                    hasFresh = True

        if not hasRotting and hasFresh:
            return -1
        
        if not hasRotting and not hasFresh:
            return 0

        maxMinutes = 0

        while len(queue) > 0:
            el = queue.pop(0)

            print(el)

            i = el[0]
            j = el[1]
            minute = el[2]

            maxMinutes = max(maxMinutes, minute)

            if i-1>-1 and grid[i-1][j] == 1:
                grid[i-1][j] = 2
                queue.append([i-1,j,minute+1])
            
            if i+1<len(grid) and grid[i+1][j] == 1:
                grid[i+1][j] = 2
                queue.append([i+1,j,minute+1])

            if j-1>-1 and grid[i][j-1] == 1:
                grid[i][j-1] = 2
                queue.append([i,j-1,minute+1])

            if j+1<len(grid[0]) and grid[i][j+1] == 1:
                grid[i][j+1] = 2
                queue.append([i,j+1,minute+1])

        print(grid)

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 1:
                    return -1
            
        return maxMinutes

 

# @lc code=end


inputs = [
    [
        [
            [2,1,1],
            [1,1,0],
            [0,1,1]
        ],
        4,
    ],
    [
        [
            [2,1,1],
            [0,1,1],
            [1,0,1]
        ],
        -1
    ],
    [
        [
            [0,2]
        ],
        0,
    ],
    [
        [
            [2,1,1],
            [1,1,1],
            [0,1,2]
        ],
        2,
    ],
    
]

s = Solution()
for [arr1, expect] in inputs:
    res = s.orangesRotting(arr1)
    print(res==expect, res)

