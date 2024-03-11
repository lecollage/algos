from typing import List

def mergeTwoArrs(arrOne: List[int], arrTwo: List[int]):
    mergedArr = []

    i = 0
    j = 0

    minLen = min(len(arrOne), len(arrTwo)) - 1

    while i != minLen and j != minLen:
        if arrOne[i] >= arrOne[j]:
            mergedArr.append(arrOne[i])
            i=i+1





def merge(arrs: List[List[int]]):
    if not len(arrs):
        return []

    mergedArr = [*arrs[0]]

    for i in range(0, len(arrs)):
        arr = arrs[0]
        mergedArr

    return mergedArr


arrs = []

N = int(input())
for i in range(0, N):
    arrLen = int(input())
    arrs.append(list(map(int, input().strip().split())))

mergedArr = merge(arrs)
print(' '.join([str(i) for i in mergedArr]))


'''
3
3
1 2 3
2
1 2
4
3 5 6 7
'''
