from typing import List
import sys

def calc(N: int) -> int:
    arr = [sys.maxsize]*(N+1)

    arr[0] = 0

    for i in range(1, N+1):
        for j, coin in enumerate([1,3,4]):
            if coin <= i:
                arr[i] = min(arr[i], arr[i-coin] + 1)

    # print(arr)

    return arr[N]

N = int(input())
print(calc(N))

inputs = [
    1,
    2,
    3,
    4,
    5,
    6,
    10,
    18,
    20,
    34,
    1000,
]

for i, N in enumerate(inputs):
    print(calc(N))