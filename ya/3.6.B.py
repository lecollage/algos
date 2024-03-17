'''
Quick Sort Algorithm

quickSort(arr, beg, end)
  if (beg < end)
    pivotIndex = partition(arr,beg, end)
    quickSort(arr, beg, pivotIndex)
    quickSort(arr, pivotIndex + 1, end)

partition(arr, beg, end)
  set end as pivotIndex
  pIndex = beg - 1
  for i = beg to end-1
    if arr[i] < pivot
        swap arr[i] and arr[pIndex]
        pIndex++
    swap pivot and arr[pIndex+1]
return pIndex + 1
'''

from typing import List
import random

def partition(arr: List[int], low: int, high: int):
    pivot = arr[high]
    i = low-1

    for j in range(low, high):
        if arr[j] <= pivot:
          i+=1
          arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i+1

def randomizedPartition(arr: List[int], low: int, high: int):
    i = random.randint(low, high)
    arr[i], arr[high] = arr[high], arr[i]
    return partition(arr, low, high)
        

def quickSort(arr: List[int], low: int, high: int):
    if low < high:
        pivotIndex = randomizedPartition(arr, low, high)
        quickSort(arr, low, pivotIndex-1)
        quickSort(arr, pivotIndex+1, high)

    return arr


N = int(input())
arr = list(map(int, input().strip().split()))
sortedArr = quickSort(arr, 0, len(arr)-1)
print(' '.join([str(i) for i in sortedArr]))



'''
7
13 17 37 73 31 19 23

4
18 20 3 17

3
0 11 0
'''

