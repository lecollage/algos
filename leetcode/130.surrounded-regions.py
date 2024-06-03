from typing import List

#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()

        def getKey(i: int, j: int) -> str:
            return str(i) + ":" + str(j)

        def exploreAndFlip(startI: int, startJ: int, board: List[List[str]]): 
            queue = [[startI,startJ]]

            flipQueue = [[startI,startJ]]
            flip = True

            while len(queue) > 0:
                i,j = queue.pop(0)
                key = getKey(i,j)

                if key in visited:
                    continue

                visited.add(key)

                if board[i][j] == "O":
                    flipQueue.append([i,j])

                if board[i][j] == "O" and (i==0 or i==len(board)-1 or j==0 or j==len(board[i])-1):
                    flip = False
                    # print("flip = False", i, j)

                if i>0 and board[i-1][j] == "O":
                    queue.append([i-1, j])

                if i<len(board)-1 and board[i+1][j] == "O":
                    queue.append([i+1, j])

                if j>0 and board[i][j-1] == "O":
                    queue.append([i, j-1])

                if j<len(board[i])-1 and board[i][j+1] == "O":
                    queue.append([i, j+1])

            # print("flip: ", startI, startJ, flipQueue)

            if flip:
                while len(flipQueue) > 0:
                    i,j = flipQueue.pop(0)

                    board[i][j] = "X"

        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                key = getKey(i,j)

                if board[i][j] == 'O' and key not in visited:
                    exploreAndFlip(i, j, board)

# @lc code=end

inputs = [
    [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]
    ],
    [
        ["X"]
    ],
    [
        ["O"]
    ],
    [
        ["X", "X", "X"],
        ["X", "O", "X"],
        ["X", "X", "X"],
    ],
    [
        ["X", "O", "X"],
        ["X", "O", "X"],
        ["X", "X", "X"],
    ],
    [
        ["X", "X", "X"],
        ["O", "O", "X"],
        ["X", "X", "X"],
    ],
    [
        ["X", "X", "X"],
        ["X", "O", "O"],
        ["X", "X", "X"],
    ],
    [
        ["X", "X", "X"],
        ["X", "O", "X"],
        ["X", "X", "O"],
    ],
    [
        ["O", "X", "X"],
        ["X", "O", "X"],
        ["X", "X", "O"],
    ],
    [
        ["O", "O", "X"],
        ["X", "O", "O"],
        ["X", "X", "O"],
    ]
]


for input in inputs:
    board = input
    s = Solution()
    s.solve(board)

    print(board)



