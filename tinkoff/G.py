def calc(N: int, path): 
    # print(N, path)
    if N == 0:
        print(path)
        return

    last = path[len(path)-1]

    for i in range(N, last-1, -1):
        if N-i >= i or N-i==0:
            calc(N-i, [*path, i])
        


N = int(input())

for i in range(N, 0, -1):
    if N-i >= i:
        calc(N-i, [i])


'''
5

5
2 3
1 4
1 2 2
1 1 3
1 1 1 2
1 1 1 1 1

9//2 = 4

9
4 5
3 6
3 3 3
2 2 2 3
2 2 5
2 3 4
1 2 2 2 2
1 1 1 2 2 2

90//2 = 45

'''
