from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    arr = []

    def execInorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return
        
        self.execInorderTraversal(root.left)
        self.arr.append(root.val)
        self.execInorderTraversal(root.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.arr = []
        self.execInorderTraversal(root)
        return self.arr
        
        
# @lc code=end

