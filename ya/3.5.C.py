from typing import List
import math

def merge(arrOne: List[int], arrTwo: List[int]):
    mergedArr = []
    i = 0
    j = 0

    while i < len(arrOne) or j < len(arrTwo):
        if j>=len(arrTwo) or (i<len(arrOne) and arrOne[i]<=arrTwo[j]):
            mergedArr.append(arrOne[i])
            i+=1
        else:
            mergedArr.append(arrTwo[j])
            j+=1

    return mergedArr

def mergeSort(arr: List[int]):
    if len(arr) == 1:
        return arr
    
    halfLen = math.floor(len(arr)/2)

    firstHalf = arr[0:halfLen]
    secondHalf = arr[halfLen:len(arr)]

    sortedFirstHalf = mergeSort(firstHalf)
    sortedSecondHalf = mergeSort(secondHalf)

    mergedArr = merge(sortedFirstHalf, sortedSecondHalf)

    return mergedArr


N = int(input())
arr = list(map(int, input().strip().split()))
sortedArr = mergeSort(arr)
print(' '.join([str(i) for i in sortedArr]))


# print(mergeTwoArrs([1,2,3], [4,5,6],))
# print(mergeTwoArrs([4,5,6], [1,2,3],))
# print(mergeTwoArrs([4,5,6,7], [1,2,3],))
# print(mergeTwoArrs([1,2,3],[4,5,6,7],))
# print(mergeTwoArrs([1,2,3,7],[4,5,6,7],))
# print(mergeTwoArrs([7],[4,5,6,7],))
# print(mergeTwoArrs([4,5,6,7],[7],))
# print(mergeTwoArrs([4,5,6,7],[],))
# print(mergeTwoArrs([-2],[4,5,6,7],))
# print(mergeTwoArrs([-2],[],))
# print(mergeTwoArrs([],[-2],))
# print(mergeTwoArrs([],[]))
# print(mergeTwoArrs([-5],[-1]))
# print(mergeTwoArrs([-5,-1],[-10,-1])) # [-10, -5, -2, -1]
# print(mergeTwoArrs([-5,-1],[10,100000,1000000,1000000000])) # [-10, -5, -2, -1]
# print(mergeTwoArrs([10,100000,1000000,1000000001],[-5,-1,100000,1000000000])) # [-10, -5, -2, -1]


'''
7
13 17 37 73 31 19 23

4
18 20 3 17

3
0 11 0
'''

