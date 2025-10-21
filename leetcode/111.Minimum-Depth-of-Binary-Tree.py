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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque()

        q.append((root, 1))

        while len(q):
            node, depth = q.popleft()

            print(node.val)

            if not node.left and not node.right:
                return depth

            if node.left:
                q.append((node.left, depth+1))

            if node.right:
                q.append((node.right, depth+1))

        return -1
# @lc code=end

'''
           2
          /
         3
        /
       4
       5
       6

'''

tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

s = Solution()
print(s.minDepth(tree))