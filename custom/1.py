from typing import Tuple

def calc(querie: Tuple[int, int, int]):
    global a
    
    x, y, s = querie
    
    for i in range(x, y+1):
        a[i] += s

    print()


queries = [
    [2,4,5],
    [1,3,2],  
    [0,1,1]
]

n = int(input())
a = [0] * n

for q in queries:
    calc(q)

for i in range(n):
    ...

print(a)