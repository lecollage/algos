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
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return None
        
        stack = [root]
        arr = []

        while len(stack) > 0:
            node = stack.pop()

            arr.append(node.val)

            if node.right is not None:
                stack.append(node.right)

            if node.left is not None:
                stack.append(node.left)


        return arr


# @lc code=end



adjLists = [
    # [1,None,2,3],
    [3,1,2]
]

for adjList in adjLists:
    node = TreeNode(adjList[0])

    for el in adjList:
        if el is not None:
            node.insert(el)
    
    # node.PrintTree()

    s = Solution()
    print(s.preorderTraversal(node))
    print('')
    print('')
    print('')
