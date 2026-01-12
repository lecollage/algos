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

    def check(self, verticeA: int, verticeB: int) -> bool:
        return self.find(verticeA) == self.find(verticeB)

    def countOfComponents(self) -> int:
        count = 0

        for i, el in enumerate(self.parents):
            if i == el:
                count += 1

        return count

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # revercedAccounts = 

        # for account in accounts

        ...
# @lc code=end

'''
'''

testCases = [
    [
        [
            ["John","johnsmith@mail.com","john_newyork@mail.com"],
            ["John","johnsmith@mail.com","john00@mail.com"],
            ["Mary","mary@mail.com"],
            ["John","johnnybravo@mail.com"]
        ],
        [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]],
    ],
    [
        [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]],
        [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
    ],
]

for [a, expected] in testCases:
    print('')

    s = Solution()

    result = s.accountsMerge(a)
    print(a)
    print(result == expected, f"result {result} should be expected: {expected}")


dsu = DSU(10)

# dsu.union(3, 1)
# dsu.union(2, 1)

# dsu.union(0, 5)
# dsu.union(0, 4)
# dsu.union(0, 3)

dsu.union(0, 1)
dsu.union(0, 2)

dsu.union(3, 4)
dsu.union(4, 5)
dsu.union(5, 6)

print(dsu.check(6, 2))

dsu.union(6, 2)



"johnsmith@mail.com"
"john_newyork@mail.com"



print(dsu.parents)
print(dsu.rank)
# print(dsu.find(5))

# dsu.merge(5, 8)
# print(dsu.parents)
print(dsu.find(2))
print(dsu.find(6))

print(dsu.find(0))