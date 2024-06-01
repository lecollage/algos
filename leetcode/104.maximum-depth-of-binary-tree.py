from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        # Compare the new value with the parent node
      if self.val:
         if val < self.val:
            if self.left is None:
               self.left = TreeNode(val)
            else:
               self.left.insert(val)
         elif val > self.val:
               if self.right is None:
                  self.right = TreeNode(val)
               else:
                  self.right.insert(val)
      else:
         self.val = val

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()

        print(self.val)

        if self.right:
             self.right.PrintTree()

#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        stack = [[root, 1]]

        maxDepth = 1

        while len(stack) > 0:
            node, depth = stack.pop()

            maxDepth = max(depth, maxDepth)

            if node.left is not None:
                stack.append([node.left, depth+1])

            if node.right is not None:
                stack.append([node.right, depth+1])

        return maxDepth
# @lc code=end



adjLists = [
    [
        [3,9,20,None,None,15,7],
        3
    ],
    [
        [1,None,2],
        2,
    ],
]

for [adjList, expect] in adjLists:
    node = TreeNode(adjList[0])

    for el in adjList:
        if el is not None:
            node.insert(el)
    
    node.PrintTree()

    s = Solution()
    print(s.maxDepth(node) == expect)
    print('')
    print('')
    print('')
