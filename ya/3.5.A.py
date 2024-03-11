from typing import List

def selectionSort(arr: List[int]):
    for i in range(0, len(arr) - 1):
        indexOfMin = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[indexOfMin]:
                indexOfMin = j
            
        buf = arr[i]
        arr[i] = arr[indexOfMin]
        arr[indexOfMin] = buf

    return arr


N = int(input())
arr = list(map(int, input().strip().split()))

sortedArr = selectionSort(arr)
print(' '.join([str(i) for i in sortedArr]))

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
