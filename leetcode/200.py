from typing import List

class Solution:
    visited = set()

    def getKey(self, i: int, j: int) -> str:
        return str(i)+":"+str(j)

    def explore(self, i: int, j: int, grid: List[List[str]]):
        stack = [[i,j]]

        while len(stack) > 0:
            i, j = stack.pop()

            key = self.getKey(i,j)

            if key in self.visited:
                continue

            self.visited.add(key)

            if i > 0 and grid[i-1][j] == '1':
                stack.append([i-1,j])
            
            if i < len(grid)-1 and grid[i+1][j] == '1':
                stack.append([i+1,j])

            if j > 0 and grid[i][j-1] == '1':
                stack.append([i,j-1])

            if j < len(grid[i])-1 and grid[i][j+1] == '1':
                stack.append([i,j+1])

    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited = set()
        islands = 0
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == '1' and not self.getKey(i,j) in self.visited:
                    islands = islands + 1
                    # print('explore starts', i, j)
                    self.explore(i, j, grid)
                    
        return islands

inputs = [
    [
        [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ],
        1
    ],
    [
        [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ],
        3
    ]
]


for _, input in enumerate(inputs):
    s = Solution()
    res = s.numIslands(input[0])

    print(res, res == input[1])

'''
  |
- i -
  |
'''