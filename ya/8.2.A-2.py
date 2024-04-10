def calc(target: int) -> int:
    if target > 5:
        dp = [0] * target
    else: 
        dp = [0] * 5
    
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 1
    dp[4] = 1

    if target < 5:
        return dp[target]

    for i in range(5, target):
        dp[i] = min(dp[i-1], dp[i-3], dp[i-4])+1

    return dp[-1]

N = int(input())
print(calc(N))

inputs = [
    [18, 5],
    [20, 5],
    [34, 9],

    [1, 1],
    [2, 2],
    [3, 1],
    [4, 1],
]

for _, input in enumerate(inputs):
    print(calc(input[0]) == input[1])

'''
1,3,4


0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
0 1 2 1 1 2 2 2 2 3 3  3  3  4  4  4  .. 5  5


dp[i] = min(dp[i-1], dp[i-3], dp[i-4]) + 1

'''


'''
18
5

20
5

34
9
'''