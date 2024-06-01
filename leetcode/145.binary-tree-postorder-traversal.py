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
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        res = []
        stack = [root]
        visited = [False]

        while len(stack) > 0:
            node, v = stack.pop(), visited.pop()

            if node:
                if v:
                    res.append(node.val)
                else:
                    stack.append(node)
                    visited.append(True)
                    
                    stack.append(node.right)
                    visited.append(False)

                    stack.append(node.left)
                    visited.append(False)
        return res

# @lc code=end

adjLists = [
    [1,None,2,3],
    [3,1,2]
]

for adjList in adjLists:
    node = TreeNode(adjList[0])

    for el in adjList:
        if el is not None:
            node.insert(el)
    
    # node.PrintTree()

    s = Solution()
    print(s.postorderTraversal(node))
    print('')
    print('')
    print('')
