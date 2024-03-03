from typing import List
import copy

def calc(sum, dict, path):
    if sum == 0:
        print("Yes")
        print(len(path))
        print(' '.join([str(i) for i in path]))
        return True
    
    if sum < 0:
        return False
    
    for coin in dict:
        dictNew = copy.deepcopy(dict)
        if dictNew[coin] > 0:
            dictNew[coin] -= 1
            good = calc(sum - coin, dictNew, [*path, coin])

            if good:
                return True
    
    return False


N, sum = map(int, input().split())
coins = list(map(int, input().strip().split()))[:N]
dict = {}

for coin in coins:
    dict[coin] = 2

good = calc(sum, dict, [])

if not good:
    print("No")