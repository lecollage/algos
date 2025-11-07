from typing import List, Optional

from collections import deque
#
# @lc app=leetcode id=530 lang=python3
#
# 530. Minimum Absolute Difference in BST
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def buildTree(nodes: list) -> Optional[TreeNode]:
    n = len(nodes)

    if n == 0:
        return None
    
    parentStack = deque()
    root = TreeNode(nodes[0])
    curParent = root

    for i in range(1, n):
        if i % 2 == 1:
            if nodes[i] is not None:
                curParent.left = TreeNode(nodes[i])
                parentStack.append(curParent.left)
        else:
            if nodes[i] is not None:
                curParent.right = TreeNode(nodes[i])
                parentStack.append(curParent.right)
            
            curParent = parentStack.popleft()

    return root

# @lc code=start
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        diff = float("inf")
        minNode = root

        def dfs(node: Optional[TreeNode]):
            nonlocal diff, minNode

            if not node:
                return

            if abs(node.val - target) < diff or (abs(node.val - target) == diff and node.val < minNode.val):
                minNode = node
                diff = abs(node.val - target)

            if node.val >= target:
                dfs(node.left)
            elif target > node.val:
                dfs(node.right)

        dfs(root)

        return minNode.val
# @lc code=end

adjLists = [
    [
        [4,2,5,1,3],
        3.714286,
        4,
    ],
    [
        [1],
        4.428571,
        1,
    ],
    [
        [4,2,5,1,3],
        3.5,
        3,
    ],
    [
        [4,2,5,1,3],
        4.5,
        4,
    ],
    
]

for [tree, val, expect] in adjLists:
    t = buildTree(tree)

    s = Solution()
    res = s.closestValue(t, val)
    print(res == expect, res)
    print('')
    print('')
    print('')
