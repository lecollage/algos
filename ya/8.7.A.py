from typing import List

def calc(weights: List[int]) -> bool:
    if len(weights) < 3:
        return False

    sum = 0

    for _, weight in enumerate(weights):
        sum = sum + weight
    
    if sum%3 != 0:
        return False
    maxWeight = int(sum/3)
    weights = [0, *weights]
    L = len(weights)

    dp = [
        [
            [
                False for _ in range(maxWeight)
            ] * (maxWeight) for _ in range(maxWeight)
        ] * (L) for _ in range(L)
    ]

    # print(dp[0])
    # print("")
    # print(dp[0][0])
    # print("")
    print(dp[0][0][0])
    # print("")

    dp[0][0][0] = True

    for i in range(1, L):
        for j in range(0, maxWeight):
            for k in range(0, maxWeight):
                dp[i][j][k] = dp[i-1][j][k]

                if j > weights[i]:
                    dp[i][j][k] = dp[i-1][j-weights[i]][k] or dp[i][j][k]

                if k > weights[i]:
                    dp[i][j][k] = dp[i-1][j][k-weights[i]] or dp[i][j][k]

                print(i, j, dp[i][j])

    print(dp[-1])

    return dp[-1][-1][-1]


#  or dp[i-1][j][k-weights[i-1]]

# N = input()
# arr = list(map(int, input().strip().split()))
# print(calc(N, arr))

inputs = [
    # [
    #     [1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25],
    #     True
    # ],
    # [
    #     [1, 2, 3, 4, 5, 6, 7],
    #     True
    # ],
    # [
    #     [12, 13, 14, 15, 23],
    #     True
    # ],
    # [
    #     [12],
    #     False
    # ],
    # [
    #     [12, 18],
    #     False
    # ],
    # [
    #     [3, 3, 4],
    #     False
    # ],
    [
        [3, 3, 3],
        True
    ]
]

for i, input in enumerate(inputs):
    weights = input[0]
    print(calc(weights) == input[1])


'''
73 5
1 2 3 4 5 5 7 7 8 10 12 19 25

10 + 10 + 14 + 18 + 12 + 44 = 34 + 40 + 44 = 108
108/3 = 36

108/2 = 54

1,2,3


108 - 20

20

20-10
10/10

108-25

        0 1 2 3 4 5 6 7 8 9 10 ... 17 18 19 20 ... 25 26 27 28 29 30 ... 36 ... 54
    0   x x
    1     t                                                                      
    2     t t                                                                    
    3     t   t     x     x                                                       
    4     t     t t       x t                                                    
 15 5     t       t         f                                                    
 20 5   t t t               t                                                   
    7                                                                           
    7                                                                           
    8                                                                           
    10                                      t                                    
    12                                      f                                   
    19                                                                          
    25                                      f                                   


dp[i][j]=dp[i-1][j] || dp[i-1][j-v[i-1]]

dp[i][j][k]=dp[i-1][j][k] || dp[i-1][j-v[i-1]][k] || dp[i-1][j][k-v[i-1]]
'''




'''
Ввод
13
1 2 3 4 5 5 7 7 8 10 12 19 25

Вывод
1




7
1 2 3 4 5 6 7
'''