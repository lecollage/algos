from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#     def buildTree(nodes: list) -> TreeNode:
#         n = len(nodes)

#         if n == 0:
#             return None
        
#         parentStack = collections.deque()
#         root = TreeNode(nodes[0])
#         curParent = root

#         for i in range(1, n):
#             if i % 2 == 1:
#                 if nodes[i] is not None:
#                     curParent.left = TreeNode(nodes[i])
#                     parentStack.append(curParent.left)
#             else:
#                 if nodes[i] is not None:
#                     curParent.right = TreeNode(nodes[i])
#                     parentStack.append(curParent.right)
                
#                 curParent = parentStack.popleft()

#         return root

#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(root: Optional[TreeNode]):
            if root is None:
                return -1
            
            left = dfs(root.left)
            right = dfs(root.right)

            res[0] = max(res[0], left + right + 2)

            return max(left, right) + 1
        
        dfs(root)

        return res[0]

# @lc code=end

