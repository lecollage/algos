from typing import List
from collections import deque
from math import log2, ceil

#
# @lc app=leetcode id=236 lang=python3
#
# 236. Lowest Common Ancestor of a Binary Tree
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# @lc code=start
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        tin = {}
        tout = {}
        seq = 0
        valNodeMap = {}


        def dfsValNodeMap(node: 'TreeNode'):
            nonlocal seq

            tin[node.val] = seq
            seq += 1
            valNodeMap[node.val] = node

            if node.left:
                dfsValNodeMap(node.left)

            if node.right:
                dfsValNodeMap(node.right)

            tout[node.val] = seq
            seq += 1



        def dfs(node: 'TreeNode'):
            nonlocal maxJump

            if node.left:
                up[node.left.val][0] = node.val

                for i in range(1, maxJump+1):
                    if up[node.left.val][i-1] != None:
                       up[node.left.val][i] = up[up[node.left.val][i-1]][i-1]

                dfs(node.left)

            if node.right:
                up[node.right.val][0] = node.val

                for i in range(1, maxJump+1):
                    if up[node.right.val][i-1] != None:
                       up[node.right.val][i] = up[up[node.right.val][i-1]][i-1]

                dfs(node.right)

        dfsValNodeMap(root)

        n = len(tin)
        maxJump = ceil(log2(n))
        up: dict[List[int]] = {key: [None]*(maxJump+1) for key in valNodeMap}

        dfs(root)

        def isAncestor(val: int, potentialAncestor: int) -> bool:
            return tin[potentialAncestor] <= tin[val] and tout[val] <= tout[potentialAncestor]

        pVal = p.val
        qVal = q.val

        if isAncestor(qVal, pVal):
            return p
        
        if isAncestor(pVal, qVal):
            return q

        for i in range(maxJump, -1, -1):
            if up[pVal][i] != None and not isAncestor(qVal, up[pVal][i]):
                pVal = up[pVal][i]
              
        return valNodeMap[up[pVal][0]]
# @lc code=end
