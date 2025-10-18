from typing import List
from collections import deque

#
# @lc app=leetcode id=3286 lang=python3
#
# 3286. Find a Safe Walk Through a Grid
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
        parents = {}
        valNodeMap = {}

        def dfs(node: 'TreeNode'):
            nonlocal seq
            tin[node.val] = seq
            seq += 1
            valNodeMap[node.val] = node

            if node.left:
                parents[node.left.val] = node.val
                dfs(node.left)

            if node.right:
                parents[node.right.val] = node.val
                dfs(node.right)

            tout[node.val] = seq
            seq += 1

        dfs(root)

        def isAncestor(val: int, potentialAncestor: int) -> bool:
            return tin[potentialAncestor] <= tin[val] and tout[val] <= tout[potentialAncestor]

        pVal = p.val
        qVal = q.val

        while(True):
            if isAncestor(qVal, pVal):
                return valNodeMap[pVal]
            
            if isAncestor(pVal, qVal):
                return valNodeMap[qVal]
            
            pVal = parents[pVal]
            qVal = parents[qVal]            
# @lc code=end
