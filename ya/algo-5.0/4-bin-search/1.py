from typing import List

def getLeftIndex(arr: List[int], target: int) -> int:
    if target <= arr[0]:
        return 0
    
    if target > arr[-1]:
        return len(arr)-1

    left = 0
    right = len(arr)-1

    while(left + 1 < right):
        middle = int(left + (right - left) / 2)

        if arr[middle] <= target :
            left = middle

        if arr[middle] > target:
            right = middle

    if arr[left] == target:
        return left
    
    if arr[right] == target:
        return right
    
    return right

def getRightIndex(arr: List[int], target: int) -> int:
    if target < arr[0]:
        return 0

    if target >= arr[-1]:
        return len(arr)

    left = 0
    right = len(arr)-1

    while(left + 1 < right):
        middle = int(left + (right - left) / 2)

        if arr[middle] <= target :
            left = middle

        if arr[middle] > target:
            right = middle

    return right

def process(arr: List[int], leftTarget: int, rightTarget: int) -> int:
    arr.sort()

    if leftTarget > arr[-1]:
        return 0
    
    if rightTarget < arr[0]:
        return 0

    leftIndex = getLeftIndex(arr, leftTarget)
    rightIndex = getRightIndex(arr, rightTarget)

    return rightIndex - leftIndex

N = int(input())
arr = list(map(int, input().strip().split()))
M = int(input())

allBorders = []

for i in range(0, M):
    allBorders.append(list(map(int, input().strip().split())))

counts = []

for i, borders in enumerate(allBorders):
    counts.append(process(arr, borders[0], borders[1]))

print(' '.join([str(i) for i in counts]))



# # TEST
inputs = [
    [
       [2, 2, 2, 3, 4, 10, 10, 10],
       1, 1,
       0
    ],
    [
       [2, 2, 2, 3, 4, 10, 10, 10],
       1, 2,
       3
    ],
    [
       [2, 2, 2, 3, 4, 10, 10, 10],
       1, 3,
       4
    ],

    [
       [10, 1, 10, 3, 4],
       1, 10,
       5,
    ],
    [
       [10, 1, 10, 3, 4],
       2, 9,
       2,
    ],
    [
       [10, 1, 10, 3, 4],
       3, 4,
       2,
    ],
    [
       [10, 1, 10, 3, 4],
       2, 2,
       0,
    ],

    [
       [1],
       2, 2,
       0,
    ],
    [
       [6],
       2, 5,
       0,
    ],
    [
       [5],
       2, 5,
       1,
    ],
    [
       [2],
       2, 5,
       1,
    ],
    [
       [3],
       2, 5,
       1,
    ],
    [
       [1,3,5,7],
       2, 6,
       2,
    ],
    [
       [1,3,5,7],
       1, 7,
       4,
    ],
    [
       [1,3,5,7],
       1, 6,
       3,
    ],
    [
       [10**9, -10**9, 1,3,5,7],
       1, 6,
       3,
    ],
    [
       [10**9, -10**9, 1,3,5,7],
       1, 10**9,
       5,
    ],
    [
       [10**9, -10**9, 1,3,5,7],
       -10**9, 10**9,
       6,
    ],
    [
       [10**9,10**9,10**9, -10**9, 1,3,5,7],
       -10**9, 10**9-1,
       5,
    ],

    [
       [0,0,0],
       -10**9, 10**9-1,
       3,
    ],
    [
       [-1,0,1],
       -1, 0,
       2,
    ],

    [
       [-1,0,1],
       -2, -1,
       1,
    ],
    [
       [-1,0,1],
       1, 2,
       1,
    ],
    
    [
       [-1,0,1],
       1, 2,
       1,
    ],
]

for i, input in enumerate(inputs):
    arr = input[0]
    arr.sort()
    # print('lower left', getLeftIndex(input[0], input[1]))
    # print('lower right', getRightIndex(input[0], input[2]))
    print('result', process(input[0], input[1], input[2]) == input[3])


'''
5
10 1 10 3 4
4
1 10
2 9
3 4
2 2

5 2 2 0 
'''

