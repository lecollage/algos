from typing import List
# from collections import deque
from queue import PriorityQueue

#
# @lc app=leetcode id=787 lang=python3
#
# 787. Cheapest Flights Within K Stops
#

# @lc code=start
class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0

        n = len(grid)
        m = len(grid[0])
        # minScores = [[float("inf") for _ in range(m)] for _ in range(n)]
        visited = [[False for _ in range(m)] for _ in range(n)]
        directions = [
            [-1,0],
            [0,-1],
            [1,0],
            [0,1],
        ]
        queue = PriorityQueue()

        queue.put((-grid[0][0],0,0)) # pathScore, i, j 

        def isEnd(i, j) -> bool:
            return i == n-1 and j == m-1

        def isValid(i: int, j: int) -> bool:
            if i < 0 or i >= len(grid):
                return False
            
            if j < 0 or j >= len(grid[i]):
                return False
            
            return True
        
        while not queue.empty():
            negativePathScore, i, j = queue.get()
            pathScore = -negativePathScore

            print(pathScore, i, j, grid[i][j])

            if isEnd(i, j):
                return pathScore
            
            if visited[i][j]:
                continue

            visited[i][j] = True
            
            for dI, dJ in directions:
                nextI = i + dI
                nextJ = j + dJ

                if isValid(nextI, nextJ) :
                    newPathScore = min(pathScore, grid[nextI][nextJ])

                    queue.put((-newPathScore, nextI, nextJ))

        return -1
# @lc code=end


testCases = [
    {
        "grid": [
            [5,4,5],
            [1,2,6],
            [7,4,6]
        ],
        "expected": 4
    },
    {
        "grid": [
            [5,4,5],
        ],
        "expected": 4
    },
    {
        "grid": [
            [5,4,5,3],
        ],
        "expected": 3
    },
    {
        "grid": [
            [2,2,1,2,2,2],
            [1,2,2,2,1,2]
        ],
        "expected": 2
    },
    {
        "grid": [
            [3,4,6,3,4],
            [0,2,1,1,7],
            [8,8,3,2,7],
            [3,2,4,9,8],
            [4,1,2,0,0],
            [4,6,5,4,3]
        ],
        "expected": 3
    },
]

for testCase in testCases:
    print('')

    grid = testCase["grid"]
    expected = testCase["expected"]

    s = Solution()

    result = s.maximumMinimumPath(grid)
    print(grid, result)
    assert result == expected, f"result {result} should be expected: {expected}"



'''
            [5,4,5]
            [1,2,6]
            [7,4,6]

            min(grid[i][j], pathScore) - current cell

            visited?
            4<5 currMin < pathMin update min
            add max

            4
            1

            [5,4,-1]
            [1,-1,-1]
            [-1,-1,-1]
'''

'''

queue.add(min(grid[nextI][nextJ], pathScore)) - current cell

max(mins)

mins
            [5,4,inf]
            [1,inf,inf]
            [inf,inf,inf]

[
node0,
node1,
node2,


]

'''