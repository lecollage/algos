def calc(N: int, max: int, path):
    if N == 0:
        print(*path)
        return path

    for i in range(1, max+1):
        if N-i >= 0:
            calc(N-i, i, [*path, i])


N = int(input())

for i in range(1, N):
    calc(N-i, i, [i])

print(N)
'''
'''
