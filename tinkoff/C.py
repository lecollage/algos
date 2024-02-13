def calc(N: int, K: int, s: str = ""):
    if not K:
        print(s + '0' * N)
        return
    
    if N == K:
        print(s + '1' * N)
        return

    # if not N and not K:
    #     print(s)
    #     return 

    # if N < K:
    #     return
    
    # if K < 0:
    #     return

    calc(N-1, K, s+"0")
    calc(N-1, K-1, s+"1")

N, K = map(int, input().split())
calc(N, K, "")










'''
0111
1011
1101
1110

4 3

1111


N-1, K-1, 

N < K


'''


