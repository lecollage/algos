from typing import List
import sys

def calc(maxWeight: int, weights: List[int]) -> int:
    n = len(weights)
    dp = []

    for i in range(0, n+1):
        dp.append([False]*(maxWeight+1))
        print(bin(n+1) - bin(i))

    return 0

# N = int(input())
# print(calc(N))

inputs = [
    [4, 3, [3, 1, 1]],
    # [10, 3, [1, 4, 9]],
]

for i, input in enumerate(inputs):
    maxWeight = input[0]
    weights = input[2]
    print(calc(maxWeight, weights))