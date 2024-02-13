def calc(N: int, s: str, used):
    if N == len(s):
        print(s)
        return

    for i in range(1, N+1):
        if not used[i]:
            used[i] = True
            calc(N, s+str(i), used)
            used[i] = False


N = int(input())
used = [False] * (N + 1)
calc(N, "", used)










'''
3
123
132
213
231
312
321

for i in range(N):
    calc(N, i+1, s)

'''