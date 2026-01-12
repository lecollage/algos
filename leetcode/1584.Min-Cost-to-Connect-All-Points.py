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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # points[i] = [xi, yi]
        # |xi - xj| + |yi - yj|

        # [xi, yi]
        edges = []

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                edges.append((i, j))

        def calcWeight(x) -> int:
            i = x[0]
            j = x[1]

            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        edges.sort(key=calcWeight)

        dsu = DSU(len(points))
        weight = 0
        edgesAdded = 0

        for i, j in edges:
            if not dsu.check(i, j):
                dsu.union(i, j)
                weight += calcWeight((i, j))
                edgesAdded += 1

                if edgesAdded == len(points)-1:
                    return weight

        return 0
# @lc code=end

'''
'''

testCases = [
    [
        [[0,0],[2,2],[3,10],[5,2],[7,0]],
        20
    ],
    [
        [[3,12],[-2,5],[-4,1]],
        18
    ],
    [
        [[0,0]],
        0
    ]
]

for [a, expected] in testCases:
    print('')

    s = Solution()

    result = s.minCostConnectPoints(a)
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