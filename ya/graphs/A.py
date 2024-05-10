from typing import List

def getMatrix(v: int, e: int, edges: List[List[int]]):
    matrix = [
        [0 for _ in range(0, v)] for _ in range(0, v)
    ]

    for _, [v, u] in enumerate(edges):
        matrix[v-1][u-1] = 1 # Oriented
        # matrix[u-1][v-1] = 1 # Non-oriented

    return matrix

edges = []
v, e = map(int, input().split())    
for _ in range(0, e):
    n1, n2 = map(int, input().split())
    edges.append([n1, n2])

# print(v,e, vertixes)

print(*getMatrix(v,e, edges), sep='\n')


# arr = list(map(int, input().strip().split()))
# print(calc(N, arr))

# inputs = [
#     # [
#     #     [1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25],
#     #     True
#     # ],
#     # [
#     #     [1, 2, 3, 4, 5, 6, 7],
#     #     True
#     # ],
#     # [
#     #     [12, 13, 14, 15, 23],
#     #     True
#     # ],
#     # [
#     #     [12],
#     #     False
#     # ],
#     # [
#     #     [12, 18],
#     #     False
#     # ],
#     # [
#     #     [3, 3, 4],
#     #     False
#     # ],
#     [
#         [3, 3, 3],
#         True
#     ]
# ]

# for i, input in enumerate(inputs):
#     weights = input[0]
#     print(calc(weights) == input[1])


'''

'''