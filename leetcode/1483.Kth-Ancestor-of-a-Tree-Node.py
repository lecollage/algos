from typing import List, Optional
from collections import deque
from math import log2, ceil

#
# @lc app=leetcode id=1483 lang=python3
#
# 1483. Kth Ancestor of a Tree Node
#

# @lc code=start
class TreeAncestor:
    def dfs(self):
        stack = [self.root]

        while(len(stack)):
            node = stack.pop()

            for child in self.tree[node]:
                stack.append(child)

                self.up[child][0] = node

                for i in range(1, self.maxJump+1):
                    if self.up[child][i-1] != -1:
                        self.up[child][i] = self.up[self.up[child][i-1]][i-1]

    def __init__(self, n: int, parent: List[int]):
        self.n = n
        self.maxJump = ceil(log2(self.n))
        self.up: List[List[int]] = [[-1]*(self.maxJump+1) for _ in range(self.n)]

        self.tree = [[] for _ in range(n)]
        self.root = -1

        for i, el in enumerate(parent):
            if el != -1:
                self.tree[el].append(i)
            else:
                self.root = i

        self.dfs()

        print(*self.up, sep=',\n')

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(self.maxJump, -1, -1):
            if 2**i <= k:
                k -= 2**i
                node = self.up[node][i]

                if node == -1:
                    return -1

        return node
# @lc code=end


t = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
print(t.getKthAncestor(3,1))
print(t.getKthAncestor(5, 2))
print(t.getKthAncestor(6, 3))

