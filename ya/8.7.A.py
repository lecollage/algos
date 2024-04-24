from typing import List

def calc(maxWeight: int, weights: List[int]) -> int:
    ...

target, N = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

print(calc(target, arr))

inputs = [
    [
        6, 4,
        [1, 1, 3, 1],
        6
    ],
 
]

for i, input in enumerate(inputs):
    maxWeight = input[0]
    weights = input[2]
    print(calc(maxWeight, weights) == input[3])


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


dp[i][j]=dp[i-1][j-v[i-1]] || dp[i-1][j]

dp[i][j][k]=dp[i-1][j-v[i-1]][k] || dp[i-1][j][k] || dp[i-1][j][k-v[i-1]]
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