def calc(N: int, K: int, s: str = ""):
    if N == len(s):
        print(s)
        return 

    for i in range(K):
        calc(N, K, s+str(i))

N, K = map(int, input().split())
calc(N, K, "")
