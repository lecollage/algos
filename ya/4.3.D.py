from typing import List
import sys

def maxMultiplication(arr: List[int]) -> int:
    max1 = -sys.maxsize - 4
    max2 = -sys.maxsize - 3
    max3 = -sys.maxsize - 2
    max4 = -sys.maxsize - 1

    min1 = sys.maxsize + 4
    min2 = sys.maxsize + 3
    min3 = sys.maxsize + 2
    min4 = sys.maxsize + 1

    for i, el in enumerate(arr):
        # max
        if el > max1:
            max4 = max3
            max3 = max2
            max2 = max1
            max1 = el
        elif el > max2:
            max4 = max3
            max3 = max2
            max2 = el
        elif el > max3:
            max4 = max3
            max3 = el
        elif el > max4:
            max4 = el

        # min
        if el < min1:
            min4 = min3
            min3 = min2
            min2 = min1
            min1 = el
        elif el < min2:
            min4 = min3
            min3 = min2
            min2 = el
        elif el < min3:
            min4 = min3
            min3 = el
        elif el < min4:
            min4 = el
        
    # print("max: ", max1, max2, max3, "min: ", min1, min2)
            
    return max(max1*max2*max3*max4, max1*max2*min1*min2, min1*min2*min3*min4)


# N = int(input())
# arr = list(map(int, input().strip().split()))

# result = maxMultiplication(arr)
# print(result)


inputs = [
    [1, 2, 3, 4],
    [4, 3, 2, 1],
    [-3, 2, 1, -4],
    [13, 17, 37, 73, 31, 19, 23],
    # [12, 18, 7, 11, 5, 17],
    # [99, 88, 12, 18, 7, 11, 5, 17, 88],
    [-2*(10**4), -2*(10**4), -2*(10**4), -2*(10**4)],
    [2*(10**4), 2*(10**4), 2*(10**4), 2*(10**4)],
    [2*(10**4), 2*(10**4), 2*(10**4), 0],
    [2*(10**4)-1]*(2*(10**5)),
    [-1, 0, -3, -2, 0], # 0
    [-1, -3, -2, -4], # 24
    [1, 2, 3, 4], #24
    [-1, -2, 3, 4], #24
    [-1, -3, -2, -4, -5], #120
    [0, -1, 0, -3, -2, 100], #0
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
