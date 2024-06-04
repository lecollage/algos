from typing import List, Optional

from collections import deque

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

#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        stack = [[root, root.val]]

        while len(stack) > 0:
            node, nodeSum = stack.pop()

            if node.left is None and node.right is None and nodeSum == targetSum:
                return True

            if node.left is not None:
                stack.append([node.left, nodeSum + node.left.val])

            if node.right is not None:
                stack.append([node.right, nodeSum + node.right.val])

        return False

            
# @lc code=end




adjLists = [
    [
        [5,4,8,11,None,13,4,7,2,None,None,None,1],
        22,
        True
    ],
    [
        [1,2,3],
        5,
        False
    ],
    [
        [],
        0,
        False
    ],
]

for [l,target,expect] in adjLists:
    p = buildTree(l)
    s = Solution()
    res = s.hasPathSum(p, target)
    print(res == expect)
    print('')
    print('')
    print('')


