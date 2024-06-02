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
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack = [root]
        heights = {None: 0}

        while len(stack) > 0:
            node = stack.pop()

            if node is None:
                continue

            leftHeight = heights.get(node.left, None)
            rightHeight = heights.get(node.right, None)

            if leftHeight is None or rightHeight is None:
                stack.append(node)
                stack.append(node.left)
                stack.append(node.right)
                continue

            heights[node] = max(leftHeight, rightHeight) + 1

            diff = leftHeight - rightHeight

            if diff < 0:
                diff *= -1

            if diff > 1: 
                return False

        return True



# @lc code=end


adjLists = [
    [
        [3,9,20,None,None,15,7],
        True
    ],
    [
        [1,2,2,3,3,None,None,4,4],
        False
    ],
    [
        [1,2],
        True
    ],
    [
        [1],
        True
    ],
    [
        [],
        True
    ],
    [
        [1,2,2,3,None,None,3,4,None,None,4],
        False
    ]
]

for [adjList, expect] in adjLists:
    node = buildTree(adjList)
    s = Solution()
    res = s.isBalanced(node)
    print(res == expect)
    print('')
    print('')
    print('')
