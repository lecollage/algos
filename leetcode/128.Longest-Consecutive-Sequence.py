from typing import Optional, List

# @lc code=start
class DSU:
    def __init__(self):
        self.parents = {}
        self.sizes = {}

    def addNode(self, value: int):
        self.parents[value] = value
        self.sizes[value] = 1

    def find(self, x):
        if x == self.parents[x]:
            return x

        self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if self.sizes[rootX] < self.sizes[rootY]:
            rootX, rootY = rootY, rootX
        
        self.sizes[rootX] += self.sizes[rootY]
        self.parents[rootY] = rootX

    def check(self, verticeA: int, verticeB: int) -> bool:
        return self.find(verticeA) == self.find(verticeB)
    
    def largestSize(self) -> int:
        maxSize = 0

        for node, parent in self.parents.items():
            if node == parent:
               maxSize = max(self.sizes[node], maxSize)

        return maxSize

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dsu = DSU(len(nums))

        for num in nums:
            if num in dsu.parents:
                continue

            dsu.addNode(num)

            if num-1 in dsu.parents:
                dsu.union(num-1, num)

            if num+1 in dsu.parents:
                dsu.union(num+1, num)

        return dsu.largestSize()
# @lc code=end

'''
'''

testCases = [
    [
        [100,4,200,1,3,2],
        4
    ],
    [
        [0,3,7,2,5,8,4,6,0,1],
        9
    ],
    [
        [1,0,1,2],
        3
    ],
    [
        [],
        0
    ],
    
]

for [a, expected] in testCases:
    print('')

    s = Solution()

    result = s.longestConsecutive(a)
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