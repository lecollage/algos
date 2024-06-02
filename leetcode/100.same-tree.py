from typing import List, Optional, Tuple

from collections import deque

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


#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [[p, q]]

        while len(stack) > 0:
            nodeQ, nodeP = stack.pop()

            #checks

            if nodeQ is None and nodeP is None:
                continue

            if nodeQ is None and nodeP is not None:
                return False
            
            if nodeQ is not None and nodeP is None:
                return False
            
            if nodeQ.val != nodeP.val:
                return False

            stack.append([nodeQ.left, nodeP.left])
            stack.append([nodeQ.right, nodeP.right])

        return True
        

# @lc code=end



adjLists = [
    [
        [1,2,3],
        [1,2,3],
        True
    ],
    [
        [1,2],
        [1,None, 2],
        False
    ],
    [
        [1,2,1],
        [1,1,2],
        False
    ],
]

for [pList, qList, expect] in adjLists:
    p = buildTree(pList)
    q = buildTree(qList)
    s = Solution()
    res = s.isSameTree(p, q)
    print(res == expect)
    print('')
    print('')
    print('')
