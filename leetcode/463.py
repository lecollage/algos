from typing import List

class Solution:
    def getKey(self, i: int, j: int) -> str:
        return str(i)+":"+str(j)
    
    def getPerimeter(self, grid: List[List[int]], startI: int, startJ: int) -> int:
        visited = set()
        stack = [
            [startI,startJ]
        ]
        graph = {}
        perimeter = 0

        while len(stack) > 0:
            [i,j] = stack.pop()
            key = self.getKey(i,j)
            visited.add(key)
            neighbours = set()
            perimeter = perimeter + 4

            if i < len(grid)-1 and grid[i+1][j] == 1:
                neighbours.add(self.getKey(i+1,j))
                perimeter = perimeter - 1
                if self.getKey(i+1,j) not in visited:
                    stack.append([i+1,j])
            
            if j < len(grid[i])-1 and grid[i][j+1] == 1:
                neighbours.add(self.getKey(i,j+1))
                perimeter = perimeter - 1
                if self.getKey(i,j+1) not in visited:
                    stack.append([i,j+1])

            if j > 0 and grid[i][j-1] == 1:
                neighbours.add(self.getKey(i,j-1))
                perimeter = perimeter - 1
                if self.getKey(i,j-1) not in visited:
                    stack.append([i,j-1])

            if i > 0 and grid[i-1][j] == 1:
                neighbours.add(self.getKey(i-1,j))
                perimeter = perimeter - 1
                if self.getKey(i-1,j) not in visited:
                    stack.append([i-1,j])


            graph[key] = neighbours
            print(perimeter, [i,j], visited, stack)
            
        print(graph)
        print(perimeter)

        return perimeter

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        for i, row in enumerate(grid):
            for j, el in enumerate(row):
                if el == 1:
                    perimeter = self.getPerimeter(grid, i, j)
                    return perimeter
        
        return 0

inputs = [
    # [
    #     [
    #         [0,1,0,0],
    #         [1,1,1,0],
    #         [0,1,0,0],
    #         [1,1,0,0]
    #     ],
    #     16
    # ],
    # [
    #     [
    #         [1]
    #     ],
    #     4
    # ],
    # [
    #     [
    #         [1,0]
    #     ],
    #     4
    # ],
    # [
    #     [
    #         [0,1,0,0],
    #         [1,1,1,1],
    #         [0,1,0,0],
    #         [1,1,0,0]
    #     ],
    #     18
    # ],
    # [
    #     [
    #         [0,0]
    #     ],
    #     0
    # ],
    [
        [
            [1,1],
            [1,1]
        ],
        8
    ],
    # [
    #     [
    #         [1,1],
    #     ],
    #     6
    # ],
    # [
    #     [
    #         [1,1],
    #         [1,0],
    #     ],
    #     8
    # ]
]
s = Solution()
for [grid, res] in inputs:
    print(s.islandPerimeter(grid)==res)