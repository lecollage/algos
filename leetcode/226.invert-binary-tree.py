from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return []

        queue = [root]

        while len(queue) > 0:
            node = queue.pop(0)

            tmp = node.left
            node.left = node.right
            node.right = tmp

            if node.right is not None:
                queue.append(node.right)

            if node.left is not None:
                queue.append(node.left)

        return root

# @lc code=end


