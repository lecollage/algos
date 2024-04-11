def calc(target: int) -> int:
    if target == 1:
        return [0, '1']

    dp = [0]*(target+1)
    dp[1] = 0

    # calc answer
    for i in range(2, len(dp)):
        cases = [dp[i-1]]

        if i % 2 == 0:
            cases.append(dp[int(i/2)])

        if i % 3 == 0:
            cases.append(dp[int(i/3)])

        dp[i] = min(cases) + 1

    # calc path
    i = len(dp)-1
    path = [i]

    while not i == 1:
        minimum = dp[i-1]

        if i%2==0 and dp[int(i/2)] < minimum:
            minimum = dp[int(i/2)]
            i = int(i/2)
        elif i%3==0 and dp[int(i/3)] < minimum:
            minimum = dp[int(i/3)]
            i = int(i/3)
        else:
            i = i-1

        path.append(i)
        
    path.reverse()

    return [dp[-1], ' '.join([str(i) for i in path])]

target = int(input())
answer, path = calc(target)

print(answer)
print(path)

inputs = [
    [1, 0, '1'],
    [2, 1, '1 2'],
    [3, 1, '1 3'],
    [4, 2, '1 3 4'],
    
    [5, 3, '1 3 4 5'],
    [10, 3, '1 3 9 10'],
    [17, 5, '1 3 4 8 16 17'],
    [10**6, 5, ''],
]

for _, input in enumerate(inputs):
    answer, path = calc(input[0])
    print(answer == input[1], path, path == input[2])



'''
1 2 3 4 5
0 1 1 2 3

5-1
5/2
5/3

4-1
4/2
4/3

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
0 1 1 2 3 2 3 3 2 3  4  3  4  4  4  4  5


'''

'''
5

3
1 3 4 5

10

3
1 3 9 10

17

5
1 3 4 8 16 17

x+1
x*2
x*3
'''