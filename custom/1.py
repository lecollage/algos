from typing import Tuple, List

def calc(query: Tuple[int, int, int], arr: List[int]):
    x, y, s = query

    arr[x] = s 
    if y+1 < len(arr):
        arr[y+1] -= s
    
    return arr


queries = [
    [2,3,5],
    [0,0,1]
]

n = int(input())
a = [0] * n

for q in queries:
    a = calc(q, a)

print(a)

for i in range(1, n):
    a[i] += a[i-1]

print(a)