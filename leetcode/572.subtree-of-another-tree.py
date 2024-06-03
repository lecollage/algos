

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
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def compareSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [
            [root, subRoot]
        ]

        while len(stack) > 0:
            node, nodeSub = stack.pop()

            if node is None and nodeSub is None:
                continue

            if node is not None and nodeSub is None:
                return False

            if node is None and nodeSub is not None:
                return False
            
            if node.val != nodeSub.val:
                return False
            
            stack.append([node.left, nodeSub.left])
            stack.append([node.right, nodeSub.right])

        return True


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]

        while len(stack) > 0:
            node = stack.pop()

            if node is None:
                continue

            if node.val == subRoot.val and self.compareSubtree(node, subRoot):
                return True

            stack.append(node.left)
            stack.append(node.right)

        return False

# @lc code=end



adjLists = [
    [
        [3,4,5,1,2,None,None,None,None,0],
        [4,1,2],
        False
    ],
]

for [adjListRoot, adjListSubRoot, expect] in adjLists:
    root = buildTree(adjListRoot)
    subRoot = buildTree(adjListSubRoot)

    s = Solution()
    res = s.isSubtree(root, subRoot)
    print(res == expect, res)
    print('')
    print('')
    print('')
