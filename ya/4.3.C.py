from typing import List
import sys

def maxMultiplication(arr: List[int]) -> int:
    max1 = -sys.maxsize - 3
    max2 = -sys.maxsize - 2
    max3 = -sys.maxsize - 1

    for i, el in enumerate(arr):
        if el > max1:
            max3 = max2
            max2 = max1
            max1 = el
        elif el > max2:
            max3 = max2
            max2 = el
        elif el > max3:
            max3 = el

    # print(max1, max2, max3)

    return max1*max2*max3


N = int(input())
arr = list(map(int, input().strip().split()))

result = maxMultiplication(arr)
print(result)


inputs = [
#     [1, 2, 3],
#     [0, 1],

#     [3, 2, 1],
#     [13, 17, 37, 73, 31, 19, 23],
#     [12, 18, 7, 11, 5, 17],
#     [99, 88, 12, 18, 7, 11, 5, 17, 88],
    
    # [-2*(10**5), -2*(10**5), -2*(10**5)],
    # [2*(10**5), 2*(10**5), 2*(10**5)],
    # [2*(10**5), 2*(10**5), 0],
    [2*(10**5)-1]*(2*(10**5)),
]

for i, arr in enumerate(inputs):
    print(maxMultiplication(arr))


'''
3
3 2 1

7
13 17 37 73 31 19 23

6
12 18 7 11 5 17

3
1 2 3
'''
