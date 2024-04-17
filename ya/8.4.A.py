def calcEditDistance(A: str, B: str) -> int:
    n = len(A)
    m = len(B)

    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        dp[i][0] = i

    for j in range(1, m+1):
        dp[0][j] = j

    # print(dp)

    for i in range(1, n+1):
        for j in range(1, m+1):
            insertion = dp[i][j-1]+1
            deletion = dp[i-1][j]+1
            matching = dp[i-1][j-1]
            mismatching = dp[i-1][j-1]+1

            if A[i-1] == B[j-1]:
                dp[i][j] = min(insertion, deletion, matching)
            else:
                dp[i][j] = min(insertion, deletion, mismatching)

    # print(dp)

    return dp[-1][-1]

A = input()
B = input()
print(calcEditDistance(A, B))

# TEST1
def test1():
    inputs = [
        [
            'aac',
            'caa',
            2
        ],
        [
            'aaac',
            'caaa',
            2
        ],
        [
            'aba',
            '',
            3
        ],

        [
            '',
            'aba',
            3
        ],
        [
            'abacab',
            'bacacaba',
            3
        ],
        [
            'ada',
            'aba',
            1
        ],
        [
            'ada',
            'x',
            3
        ],
    ]

    for _, input in enumerate(inputs):
        print(input[2] == calcEditDistance(input[0], input[1]))


test1()

'''
[
    [0, 1, 2, 3],
    [1, 1, 0, 0],
    [2, 1, 1, 0],
    [3, 0, 1, 1]
]
'''