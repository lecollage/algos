from typing import Optional, List

# @lc code=start
class DSU:
    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.rank = [0] * size

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

    def isConnected(self, verticeA: int, verticeB: int) -> bool:
        return self.find(verticeA) == self.find(verticeB)

    def countOfComponents(self) -> int:
        count = 0

        for i, el in enumerate(self.parents):
            if i == el:
                count += 1

        return count

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        '''
            house 0: edges to all nodes with w wells[i]
        '''

        for i, w in enumerate(wells):
            pipes.append([0, i+1, w])

        pipes.sort(key=lambda p:p[2])

        cost = 0
        dsu = DSU(n+1)
        edgesCount = 0

        for u,v,w in pipes:
            if not dsu.isConnected(u,v):
                dsu.union(u,v)
                cost += w
                edgesCount += 1

            if edgesCount == n:
                return cost

        return cost
# @lc code=end

'''
'''

testCases = [
    [
        3,
        [1,2,2],
        [[1,2,1],[2,3,1]],
        3
    ],
    [
        2,
        [1,1],
        [[1,2,1],[1,2,2]],
        2
    ],
]

for [n, wells, pipes, expected] in testCases:
    print('')

    s = Solution()

    result = s.minCostToSupplyWater(n, wells, pipes)
    print(n, wells, pipes)
    print(result == expected, f"result {result} should be expected: {expected}")

# dsu = DSU(10)

# # dsu.union(3, 1)
# # dsu.union(2, 1)

# # dsu.union(0, 5)
# # dsu.union(0, 4)
# # dsu.union(0, 3)

# dsu.union(0, 1)
# dsu.union(0, 2)

# dsu.union(3, 4)
# dsu.union(4, 5)
# dsu.union(5, 6)

# print(dsu.check(6, 2))

# dsu.union(6, 2)



# "johnsmith@mail.com"
# "john_newyork@mail.com"



# print(dsu.parents)
# print(dsu.rank)
# # print(dsu.find(5))

# # dsu.merge(5, 8)
# # print(dsu.parents)
# print(dsu.find(2))
# print(dsu.find(6))

# print(dsu.find(0))