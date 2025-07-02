from typing import List
from collections import deque

#
# @lc app=leetcode id=3286 lang=python3
#
# 3286. Find a Safe Walk Through a Grid
#

# @lc code=start
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        if health <= 0: 
            return False

        queue = deque()

        
        print(grid[0][0])

        if grid[0][0] == 1:            
            queue.append((0, 0, health - 1))
        else:
            queue.append((0, 0, health))

        grid[0][0] = -1

        directions = [
            [-1,0],
            [0,-1],
            [1,0],
            [0,1],
        ]

        def isValid(i: int, j: int, grid: List[List[int]]) -> bool:
            if i < 0 or i >= len(grid):
                return False
            
            if j < 0 or j >= len(grid[i]):
                return False
            
            return True
        
        def isEnd(i: int, j: int, grid: List[List[int]]) -> bool:
            if i != len(grid)-1:
                return False
            
            if j != len(grid[i])-1:
                return False
            
            return True

        while len(queue):
            i, j, currentHealth = queue.popleft()

            print(i, j, currentHealth)

            if isEnd(i, j, grid) and currentHealth > 0:
                return True
            
            if currentHealth <= 0:
                continue

            for dirI, dirJ in directions:
                nextI = i + dirI
                nextJ = j + dirJ

                if isValid(nextI, nextJ, grid) and grid[nextI][nextJ] != -1:
                    healthDiff = 0

                    if grid[nextI][nextJ] == 1:
                        healthDiff = 1
                        
                    queue.append((nextI, nextJ, currentHealth-healthDiff))
                    grid[nextI][nextJ] = -1

        return False
# @lc code=end


testCases = [
    {
        "grid": [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]],
        "health": 1,
        "expected": True
    },
    {
        "grid": [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]],
        "health": 3,
        "expected": False
    },
    {
        "grid": [
            [1,1,1,1],
        ],
        "health": 4,
        "expected": False
    },
    {
        "grid": [[1,1,1],[1,0,1],[1,1,1]],
        "health": 5,
        "expected": True
    },
    {
        "grid": [
            [1],
        ],
        "health": 4,
        "expected": True
    },
    {
        "grid": [
            [1],
        ],
        "health": 0,
        "expected": False
    },
]

for testCase in testCases:
    print('')

    grid = testCase["grid"]
    health = testCase["health"]
    expected = testCase["expected"]

    s = Solution()

    result = s.findSafeWalk(grid, health)
    print(health, grid, result)
    assert result == expected, f"result {result} should be expected: {expected}"
