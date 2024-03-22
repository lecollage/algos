from typing import List

def calc(N: int, M: int) -> bool:
    dp = [[1] * (M+3) for _ in range(N+3)]

    for i in range(2, N+3):
        for j in range(2, M+3):
            dp[i][j] = int(not all([
                dp[i-1][j],
                dp[i][j-1],
                dp[i-2][j],
                dp[i][j-2],
                dp[i-1][j-2],
                dp[i-2][j-1],
            ]))

    # print(dp)
    # print(dp[N+1])

    return dp[N+2][M+2]

N, M = map(int, input().split())
print('Win' if calc(N, M) else 'Loose')

inputs = [
    [4, 4],   # Loose
    [17, 72], # Win
    [7, 5],   # Win
]

for input in inputs:
   print('Win' if calc(input[0], input[1]) else 'Loose')

'''
            dp[i-1][j-1] -> dp[i][j]
            dp[i-1][j] -> dp[i][j]
            dp[i][j-1] -> dp[i][j]


            0 1 1
            1 1 1
            1 1 1

            dp[i-1][j] -> dp[i][j]
            dp[i][j-1] -> dp[i][j]
            dp[i-2][j] -> dp[i][j]
            dp[i][j-2] -> dp[i][j]
            dp[i-1][j-2] -> dp[i][j]
            dp[i-2][j-1] -> dp[i][j]

            [
             i/j  0 1 2 3 4
               0 [0,1,0,0,0],
               1 [1,1,0,0,0],
               2 [0,0,0,0,0],
               3 [0,0,0,1,0],
               4 [0,0,0,0,0],
            ]


            [ + padding
             i/j  0 1 2 3 4 5
               0 [1,1,1,1,1,1],
               1 [1,0,1,0,0,0],
               2 [1,1,1,0,0,0],
               3 [1,0,0,0,0,0],
               4 [1,0,0,0,1,0],
               5 [1,0,0,0,0,0],
            ]
'''

