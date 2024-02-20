def calc(N: int, K: int, path):
    if K == 0:
        print(' '.join([str(i) for i in path]))
        return []

    for i in range(K, N): 
        newPath = [*path, calc(i, K-1) ]
    

N, K = map(int, input().split())

for i in range(K, N+1):
        calc(i, K-1)




'''
5 3


3 2 1

4 2 1
4 3 1
4 3 2

5 4 3
5 4 2
5 4 1
5 3 2
5 3 1
5 2 1
'''