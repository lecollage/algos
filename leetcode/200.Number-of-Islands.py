from typing import Optional, List

# @lc code=start
class DSU:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0] * size

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
    
    def countOfComponents(self) -> int:
        count = 0

        for i, el in enumerate(self.root):
            if i == el:
                count += 1
        
        return count
    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dsu = DSU(n * m)
 
        # i*m+j
        # 0 -> -1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "0":
                    dsu.root[i*m+j] = -1
                else:
                    if i > 0 and grid[i-1][j] == "1":
                        dsu.union((i-1)*m + j, i*m + j)

                    if j > 0 and grid[i][j-1] == "1":
                        dsu.union(i*m + (j-1), i*m + j)

        # print(dsu.root)

        return dsu.countOfComponents()
# @lc code=end

'''

'''

testCases = [
    [
        [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ],
        1
    ],
    [
        [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ],
        3
    ],
    
]

for [a, expected] in testCases:
    print('')

    s = Solution()

    result = s.numIslands(a)
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