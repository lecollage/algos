from typing import Optional, List

visited = []
sorted = []


def dfs(v: int):
    stack = [v]

    
    while len(stack) > 0:
        el = stack.pop()

        if visited[el]:
            continue

        sorted.append(el)

        for u in graph[el]:
            stack.append(u)

    print(sorted)


'''
       0
    /     \ 
   1       2
  /  \ 
 3    4


0,2,1
2,1,0
'''




n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [False for _ in range(n)]
for i in range(0, m):
    u,v,t = map(int, input().split())

    if t == 1:
        graph[u-1].append(v-1)
    else:
        graph[v-1].append(u-1)

print(n,m,graph, sep='\n')

dfs(0)









'''
Ввод

5 6
1 4 1
1 2 1
3 1 2
4 2 1
2 3 1
5 3 2

1: [4,2,3]
4: [2]
2: [3]
3: [5]
5: []

1: [2,3,4]
5: [2,3,4]


[


]


YES




Ввод
5 2
2 4 2
3 2 1

1: []
4: [2]
3: [2]
2: []
5: []
'''