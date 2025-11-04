from typing import List, Optional

from collections import deque
#
# @lc app=leetcode id=530 lang=python3
#
# 530. Minimum Absolute Difference in BST
#

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

# @lc code=start
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = deque([(root, -float("inf"), float("inf"))])

        while(len(stack)):
            node, minVal, maxVal = stack.pop()

            if not node:
                continue
                
            if node.val <= minVal or node.val >= maxVal:
                return False
            
            stack.append((node.left, minVal, node.val))
            stack.append((node.right, node.val, maxVal))

        return True
# @lc code=end

adjLists = [
    [
        [2,1,3],
        True,
    ],
    [
        [5,1,4,None,None,3,6],
        False,
    ],
    [
        [2,2,2],
        False,
    ],
]

for [tree, expect] in adjLists:
    t = buildTree(tree)

    s = Solution()
    res = s.isValidBST(t)
    print(res == expect, res)
    print('')
    print('')
    print('')
