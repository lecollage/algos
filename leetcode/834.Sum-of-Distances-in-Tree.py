from typing import List, Optional

from collections import deque
#
# @lc app=leetcode id=834 lang=python3
#
# 834. Sum of Distances in Tree
#

# @lc code=start
class Solution:
    def dfs(self, node: int, parent: int) -> int:
        for (neighbour, w) in self.adjList[node]:
            if neighbour != parent:
                self.dfs(neighbour, node)

                self.dp[node] += self.dp[neighbour] + w * self.size[neighbour]
                self.size[node] += self.size[neighbour]

        self.size[node] += 1

    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        self.adjList = [[] for _ in range(n)]

        for u, v, *w in edges:
            self.adjList[u].append((v, w[0] if w else 1))
            self.adjList[v].append((u, w[0] if w else 1))

        # print(self.adjList)

        weightSums = [0]*n

        for root in range(n):
            self.dp = [0] * n
            self.size = [0] * n
            self.dfs(root, -1)
            weightSums[root] = self.dp[root]

        return weightSums
# @lc code=end

'''
0->* = dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
1->* = dist(1,0) + dist(1,2) + dist(1,3) + dist(1,4) + dist(1,5)
1->* = 1         + 2         + 3         + 3         + 3
2->* = dist(2,0) + dist(2,1) + dist(2,3) + dist(2,4) + dist(2,5)
'''

adjLists = [
    [
        6,
        [[0,1],[0,2],[2,3],[2,4],[2,5]],
        [8,12,6,10,10,10],
    ],
    [
        1,
        [],
        [0]
    ]
]

for [n, edges, expect] in adjLists:
    s = Solution()
    res = s.sumOfDistancesInTree(n, edges)
    print(res == expect, res)
    print('')
    print('')
    print('')
