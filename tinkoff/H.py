paths = []

def calc(N, M, path):
    if N == 1:
        print('*'.join([str(i) for i in path]))
        paths.append(set(path))
        return
    
    for i in range(M, N+1):
        if N % i == 0:
            newPath = [*path, i]
            newSet = set(newPath)
            
            exists = False
            for p in paths:
                if len(p - newSet) == 0:
                    exists = True

            if not exists:
                calc(N//i, M, newPath)


# N, M = map(int, input().split())
# calc(N, M, [])


inputs = [
    # [4,3],
    # [18,3],
    # [20,4],
    [200,4],
]

for input in inputs:
     N = input[0]
     M = input[1]
     calc(N, M, [])