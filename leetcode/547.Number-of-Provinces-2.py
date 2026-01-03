from typing import Optional, List


# @lc code=start
class DSU:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def check(self, verticeA: int, verticeB: int) -> bool:
        return self.find(verticeA) == self.find(verticeB)
        

class Solution:
    def findCircleNum(self, mtx: List[List[int]]) -> int:
        n = len(mtx)
        dsu = DSU(n)

        # dsu.parents[-1] = -1
        print(dsu.root)

        for i in range(n):
            for j in range(n):
                if mtx[i][j] == 1:
                    if not dsu.check(i, j):
                        dsu.union(i, j)

        print(dsu.root)

        unique = set(dsu.root)

        return len(unique)
# @lc code=end

'''
parents: 0, 1, 2, 3, 4, 5
         0, 5, 5, 3, 4, 5

1,1,0, 1,1,0, 0,0,1

0,1,2, 3,4,5, 6,7,8

[
    [1,0,0,1],
    [0,1,1,0],
    [0,1,1,1],
    [1,0,1,1]
]

i -> j
j -> i

0 - 0
0 - 3
3 - 0
1 - 1
1 - 2
2 - 1
2 - 2
2 - 3


[1,1,0]
[1,1,0]
[0,0,1]

0 - 0 
0 - 1
1 - 0

2-2

0..n
2

'''

testCases = [
    [
        [[1,1,0],[1,1,0],[0,0,1]],
        2
    ],
    [
        [[1,0,0],[0,1,0],[0,0,1]],
        3
    ],
    [
        [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]],
        1
    ],
    [
        [
            [1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
            [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],
            [0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],
            [0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],
            [0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],
            [1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
            [0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],
            [0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],
            [0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],
            [0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],
            [0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]
        ],
        3
    ],
    [
        [
            [1,1,0,0,0,0,0,1,0,1],[1,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,1,0,0,0,1,1,0,0],[1,0,0,0,0,0,1,1,0,0],[0,0,0,0,0,0,0,0,1,1],[1,0,0,0,0,0,0,0,1,1]
        ],
        4
    ],
    
    
    # [
    #     [[0,0,0],[0,0,0],[0,0,0]],
    #     0
    # ]
]

for [a, expected] in testCases:
    print('')

    s = Solution()

    result = s.findCircleNum(a)
    print(a)
    assert result == expected, f"result {result} should be expected: {expected}"


# dsu = DSU(10)

# dsu.merge(0, 5)

# print(dsu.parents)
# print(dsu.find(5))

# dsu.merge(5, 8)
# print(dsu.parents)
# print(dsu.find(5))
# print(dsu.find(8))