def calcEditDistance(A: str, B: str) -> int:
    # print('calcEditDistance:', A, '"'+B+'"')
    n = len(A)
    m = len(B)

    dp = [[0] * (m+1) for _ in range(n+1)]

    # print(dp)

    for j in range(1, m+1):
        dp[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            insertion = dp[i][j-1]+1
            deletion = dp[i-1][j]+1
            matching = dp[i-1][j-1]
            mismatching = dp[i-1][j-1]+1

            if A[i-1] == B[j-1]:
                print('match', i, j, A[i-1], B[j-1])
                dp[i][j] = min(insertion, deletion, matching)
            else:
                print('mismatch', i, j, A[i-1], B[j-1])
                dp[i][j] = min(insertion, deletion, mismatching)

    print(dp)

    return dp[-1][-1]

def calcMincalcEditDistance(A: str, B: str) -> int:
    if len(B) == 0:
        return len(A)

    minimum = calcEditDistance(A, B)
    for i in range(1,len(A)+1):
        minimum = min(calcEditDistance(A, ' '*i+B), minimum)

    return minimum
    

# A = input()
# B = input()
# print(calcMincalcEditDistance(A, B))

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
    ]

    for i, input in enumerate(inputs):
        print(input[2] == calcEditDistance(input[0], input[1]))


# TEST2
def test2():
    inputs = [
        # [
        #     'aac',
        #     'caa',
        #     2
        # ],
        # [
        #     'aaac',
        #     'caaa',
        #     2
        # ],
        # [
        #     'abacab',
        #     'bacacaba',
        #     3
        # ],
        # [
        #     'ada',
        #     'aba',
        #     1
        # ],
        # [
        #     '',
        #     'aba',
        #     3
        # ],
        [
            'aba',
            '',
            3
        ],
        [
            'aba',
            'x  ',
            4
        ],
    ]

    for _, input in enumerate(inputs):
        print(input[2] == calcMincalcEditDistance(input[0], input[1]))

test2()

'''
[
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1]
]
'''