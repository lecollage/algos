from typing import List

class Solution:
    def explore(self, grid: List[List[int]], i: int, j: int) -> int:
        stack = [[i, j]]
        count = 0

        while len(stack) > 0:
            i, j = stack.pop()

            if grid[i][j] == 1:
                count = count + 1

            grid[i][j] = 0
            

            if i > 0 and grid[i-1][j] == 1:
                stack.append([i-1,j])

            if i < len(grid)-1 and grid[i+1][j] == 1:
                stack.append([i+1,j])

            if j > 0 and grid[i][j-1] == 1:
                stack.append([i,j-1])

            if j < len(grid[i])-1 and grid[i][j+1] == 1:
                stack.append([i,j+1])

            '''
                |
               -i-
                |
            '''

        return count

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxIsland = 0

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 1:
                    res = self.explore(grid, i, j)

                    if res > maxIsland:
                        maxIsland = res
                
        return maxIsland

inputs = [
    [
       [
           [0,0,1,0,0,0,0,1,0,0,0,0,0],
           [0,0,0,0,0,0,0,1,1,1,0,0,0],
           [0,1,1,0,1,0,0,0,0,0,0,0,0],
           [0,1,0,0,1,1,0,0,1,0,1,0,0],
           [0,1,0,0,1,1,0,0,1,1,1,0,0],
           [0,0,0,0,0,0,0,0,0,0,1,0,0],
           [0,0,0,0,0,0,0,1,1,1,0,0,0],
           [0,0,0,0,0,0,0,1,1,0,0,0,0]
        ],
       6
    ],
    [
        [
            [0,0,0,0,0,0,0,0]
        ],
        0
    ],
    [
        [
            [1,1,0,0,0],
            [1,1,0,0,0],
            [0,0,0,1,1],
            [0,0,0,1,1]
        ],
        4
    ]
]


for _, input in enumerate(inputs):
    s = Solution()
    res = s.maxAreaOfIsland(input[0])

    print(res, res == input[1])

'''
  |
- i -
  |
'''