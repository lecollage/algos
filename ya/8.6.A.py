from typing import List

def calc(maxWeight: int, weights: List[int]) -> int:
    n = len(weights)

    dp = [[True] + [False] * maxWeight for _ in range(0, n+1)]
    weights = [0, *weights]

    max = 0

    for i in range(1, n+1):
        row = dp[i]
        for j in range(1, len(row)):
            dp[i][j] = dp[i-1][j] or (dp[i-1][j-weights[i]] if j-weights[i] >= 0 else False)

            if dp[i][j] and j > max:
                max = j

    # print(dp)

    return max

target, N = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

print(calc(target, arr))

inputs = [
    [
        6, 4,
        [1, 1, 3, 1],
        6
    ],
    [
        7, 4,
        [1, 1, 3, 1],
        6
    ],
    [
        73, 5,
        [19, 23, 31, 17, 18],
        73
    ],
    [
        73, 4,
        [23, 31, 17, 18],
        72
    ],
    [
        73, 4,
        [23, 31, 17, 10**5, 0, 0],
        71
    ],
    [
        10**4 + 73, 4,
        [23, 31, 17, 10**5, 0, 0, 10**4],
        10**4 + 71
    ],
    [
        25, 1,
        [23],
        23
    ],
]

for i, input in enumerate(inputs):
    maxWeight = input[0]
    weights = input[2]
    print(calc(maxWeight, weights) == input[3])


'''
73 5
19 23 31 17 18

        0 1 2 3 4 5 6 7 8 9 10 ... 17 18 19 20 21 22 23 ... 37 ... 41 ... 50 ... 70 71 72 73
0    0  t f f f f f f f f f f      f  f  f  f  f  f  f      f      f      f      f  f  f  f
19   1  t f f f f f f f f f f      f  f  t  f  f  f  f      f      f      f      f  f  f  f
23   2  t                                t           t      f      t      f
31   3  t f f f f f f f f f f      f  f  t  f  f  f  t      f      t      t
17   4  t                                t           t      f      t      t
18   5  t                             t  t           t      t      t      t


dp[Wj, i-1] || dp[Wj-weights[i], i-1]
'''




'''
Ввод
10 3
1 4 9

Вывод
10
'''