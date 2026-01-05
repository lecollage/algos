from typing import Optional, List


# @lc code=start
class DSU:
    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.parents[x]:
            return x

        self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parents[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parents[rootX] = rootY
            else:
                self.parents[rootY] = rootX
                self.rank[rootX] += 1

    def check(self, verticeA: int, verticeB: int) -> bool:
        return self.find(verticeA) == self.find(verticeB)
    
    def countOfComponents(self) -> int:
        count = 0

        for i, node in enumerate(self.parents):
            if node == i:
                count += 1

        return count
        
class Solution:
    def findCircleNum(self, mtx: List[List[int]]) -> int:
        n = len(mtx)
        dsu = DSU(n)

        print(dsu.parents)

        for i in range(n):
            for j in range(n):
                if mtx[i][j] == 1:
                    dsu.union(i, j)
                    dsu.union(j, i)


        print(dsu.parents)

        return dsu.countOfComponents()
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