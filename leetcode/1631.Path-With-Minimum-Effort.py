from typing import List
# from collections import deque
from queue import PriorityQueue

#
# @lc app=leetcode id=1631 lang=python3
#
# 1631. Path With Minimum Effort
#

# @lc code=start
class Solution:
    def minimumEffortPath(self, grid: List[List[int]]) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0

        n = len(grid)
        m = len(grid[0])
        distances = [[float('inf') for _ in range(m)] for _ in range(n)]
        directions = [
            [-1,0],
            [0,-1],
            [1,0],
            [0,1],
        ]
        queue = PriorityQueue()

        queue.put((0,0,0)) # diff, i, j 

        def isEnd(i, j) -> bool:
            return i == n-1 and j == m-1

        def isValid(i: int, j: int) -> bool:
            if i < 0 or i >= len(grid):
                return False
            
            if j < 0 or j >= len(grid[i]):
                return False
            
            return True
        
        while not queue.empty():
            pathWeight, i, j = queue.get()

            # print(pathWeight, i, j, distances)

            if isEnd(i, j):
                return pathWeight
            
            if distances[i][j] <= pathWeight:
                continue

            distances[i][j]=pathWeight
            
            for dI, dJ in directions:
                nextI = i + dI
                nextJ = j + dJ

                if isValid(nextI, nextJ) :
                    edgeWeight = abs(grid[i][j] - grid[nextI][nextJ])
                    newPathWeight = max(edgeWeight, pathWeight)

                    queue.put((newPathWeight, nextI, nextJ))

        return -1

# @lc code=end


'''
from queue import PriorityQueue

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # начало - обычная Дейкстра, так что привожу фактический код
        n, m = len(heights), len(heights[0])
        visited = [[False] * m for _ in range(n)]
        q = PriorityQueue()
        q.put((0, 0, 0))
        while not q.empty():
            d, i, j = q.get()
            if i == n - 1 and j == m - 1:
                return d
            if visited[i][j]:
                continue
            visited[i][j] = True
            # дальше псевдокод
            for neighbour in neighbours: # граф имплицитный, так что соседей ищем по координатам
               if not visited[neighbour]: # опять же по координатам обращаемся в visited
                    edge_weight = ... # находим вес ребра в соседа в соответствии с условием задачи
                    new_path_weight = ... # определяем, как меняется вес пути от добавления нового ребра в соответствии с функцией агрегации весов ребер в пути
                    q.put((new_path_weight, neighbour))
'''


testCases = [
    {
        "grid": [
            [1,10,6,7]
        ],
        "expected": 9
    },
    {
        "grid": [
            [1,10,6,7,9,10,4,9]
        ],
        "expected": 9
    },
    {
        "grid": [
            [1,2,2],
            [3,8,2],
            [5,3,5]
        ],
        "expected": 2
    },
    {
        "grid": [[1,2,3],[3,8,4],[5,3,5]],
        "expected": 1
    },
    {
        "grid": [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]],
        "expected": 0
    },
    {
        "grid": [[9]],
        "expected": 0
    },
    {
        "grid": [[9, 9, 9]],
        "expected": 0
    },
    {
        "grid": [
            [9],
            [9],
            [9],
            [9]
        ],
        "expected": 0
    },
]

for testCase in testCases:
    print('')

    grid = testCase["grid"]
    expected = testCase["expected"]

    s = Solution()

    result = s.minimumEffortPath(grid)
    print(grid, result)
    assert result == expected, f"result {result} should be expected: {expected}"
