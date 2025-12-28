# @lc code=start
from typing import Optional, List

class Solution:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [0 for _ in range(n)]
        self.weight = [1 for _ in range(n)]

    def find(self, vertice: int) -> int:
        if self.parents[vertice] == vertice:
            return vertice

        self.parents[vertice] = self.find(self.parents[vertice])

        return self.parents[vertice]
    

    def merge(self, verticeA: int, verticeB: int):
        rootA = self.find(verticeA)
        rootB = self.find(verticeB)

        if self.ranks[rootA] < self.ranks[rootB]:
            rootA, rootB = rootB, rootA

        #if self.weight[rootA] < self.weight[rootB]:
            #rootA, rootB = rootB, rootA
        self.parents[rootB] = rootA

        #self.weight[rootA] += self.weight[rootB]

        if self.ranks[rootA] == self.ranks[rootB]:
            self.ranks[rootA] += 1

    def check(self, verticeA: int, verticeB: int) -> bool:
        return self.find(verticeA) == self.find(verticeB)
        
# @lc code=end

'''
parents: 0, 1, 2, 3, 4, 5

0, 5, 5, 3, 4, 5
'''

testCases = [

]

for testCase in testCases:
    print('')

    edges = testCase["edges"]
    expected = testCase["expected"]

    s = Solution()

    result = s.findItinerary(edges)
    print(edges)
    assert result == expected, f"result {result} should be expected: {expected}"
