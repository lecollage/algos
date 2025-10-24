from typing import List, Optional
from collections import deque

#
# @lc app=leetcode id=111 lang=python3
#
# 111. Minimum Depth of Binary Tree
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# @lc code=start
class Solution:
    def dfs(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return (-1, -1) # diameter, longest path
        
        leftDiameter, leftLongestPath = self.dfs(root.left)
        rightDiameter, rightLongestPath = self.dfs(root.right)

        return (max(leftDiameter, rightDiameter, leftLongestPath + rightLongestPath + 1), max(leftLongestPath, rightLongestPath) + 1) 


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter, _ = self.dfs(root)

        return diameter

# @lc code=end

'''
           2
          /  \
         3    5
        /    / \
       4    3   6
      /
     9

      2
     /  \
    3    5
'''

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)

s = Solution()
print(s.diameterOfBinaryTree(tree))