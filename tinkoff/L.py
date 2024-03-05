import math

paths = []

def calc(N, attemps, path):
    print(N, attemps, path)

    if N < 0:
        return
    
    if attemps == 0 and N != 0:
        return

    if N == 0:
        revercedPath = path[::-1]
        print(revercedPath)
        paths.append(set(revercedPath))
        return
    
    max = int(math.sqrt(N))

    for i in range(max+1, 0 -1):
        newPath = [*path, i]
        newSet = set(newPath)
        exists = False

        for existingPath in paths:
            if len(existingPath - newSet) == 0:
                exists = True
            
        if not exists:
            calc(int(N-math.pow(i, 2)), attemps-1, newPath)
    

# N = map(int, input())


inputs = [
    # 7,
    10000
]

for N in inputs:
    calc(N, 4, [])

