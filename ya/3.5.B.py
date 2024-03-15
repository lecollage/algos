from typing import List

def mergeTwoArrs(arrOne: List[int], arrTwo: List[int]):
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
# print(mergeTwoArrs([],[]))
# print(mergeTwoArrs([-5],[-1]))
# print(mergeTwoArrs([-5,-1],[-10,-1])) # [-10, -5, -2, -1]
# print(mergeTwoArrs([-5,-1],[10,100000,1000000,1000000000])) # [-10, -5, -2, -1]
# print(mergeTwoArrs([10,100000,1000000,1000000001],[-5,-1,100000,1000000000])) # [-10, -5, -2, -1]


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

2
1
1000000
1
1000000000

4
3
1 2 3
6
3 90 91 100 101 203
4
3 5 6 7
5
1 3 7 203 800
'''

