from typing import List

def maxMultiplication(arr: List[int]):
    max1 = 0 # -Infinity
    max2 = 0

    for i, el in enumerate(arr):
        if el > max1:
            max2 = max1
            max1 = el
        elif el > max2:
            max2 = el

    # print(max1, max2)

    return max1*max2


N = int(input())
arr = list(map(int, input().strip().split()))

result = maxMultiplication(arr)
print(result)


# inputs = [
#     [1, 2, 3],
#     [0, 1],

#     [3, 2, 1],
#     [13, 17, 37, 73, 31, 19, 23],
#     [12, 18, 7, 11, 5, 17],
#     [99, 88, 12, 18, 7, 11, 5, 17, 88],
# ]

# for i, arr in enumerate(inputs):
#     print(maxMultiplication(arr))


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
