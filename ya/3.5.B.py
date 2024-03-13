from typing import List

def mergeTwoArrs(arrOne: List[int], arrTwo: List[int]):
    mergedArr = []

    i = 0
    j = 0

    shortArr = arrOne
    longArr = arrTwo

    if len(arrTwo) < len(arrOne):
        shortArr = arrTwo
        longArr = arrOne

    while i < len(shortArr) or j < len(longArr):
        if i < len(shortArr) and (j == len(longArr) or shortArr[i] <= longArr[j]):
            mergedArr.append(shortArr[i])
            i+=1
        else:
            mergedArr.append(longArr[j])
            j+=1
    
    return mergedArr

def merge(arrs: List[List[int]]):
    if not len(arrs):
        return []

    mergedArr = [*arrs[0]]

    for i in range(1, len(arrs)):
        mergedArr = mergeTwoArrs(mergedArr, arrs[i])

    return mergedArr

arrs = []

N = int(input())
for i in range(0, N):
    arrLen = int(input())
    arrs.append(list(map(int, input().strip().split())))

mergedArr = merge(arrs)
print(' '.join([str(i) for i in mergedArr]))


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
# print(mergeTwoArrs([],[],))

'''
3
3
1 2 3
2
1 2
4
3 5 6 7

3
1
20
2
22 30
4
20 20 20 21

3
1
21
2
22
4
20 21 21 22

1
1
21
'''

