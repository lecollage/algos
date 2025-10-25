from typing import List, Optional
from collections import deque

#
# @lc app=leetcode id=1026 lang=python3
#
# 1026. Maximum Difference Between Node and Ancestor
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        q = deque()

        q.append((root, root.val, root.val)) # node, min, max

        maxDiff = 0

        while(len(q)):
            node, minVal, maxVal = q.popleft()
            print(node, minVal, maxVal)

            maxDiff = max(maxDiff, abs(minVal - maxVal))

            if node.left:
                q.appendleft((node.left, min(minVal, node.left.val), max(maxVal, node.left.val)))

            if node.right:
                q.appendleft((node.right, min(minVal, node.right.val), max(maxVal, node.right.val)))
        
        return maxDiff
# @lc code=end

s = Solution()

tree = TreeNode(8)
tree.left = TreeNode(3)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(6)
tree.left.right.left = TreeNode(4)
tree.left.right.right = TreeNode(7)

tree.right = TreeNode(10)
tree.right.right = TreeNode(14)
tree.right.right.right = TreeNode(13)

result = s.maxAncestorDiff(tree)
print(result)





tree2 = TreeNode(1)
tree2.right = TreeNode(2)
tree2.right.right = TreeNode(0)
tree2.right.right.left = TreeNode(3)

result = s.maxAncestorDiff(tree2)
print(result)
