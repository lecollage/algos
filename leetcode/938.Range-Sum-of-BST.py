from typing import List, Optional

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
# @lc app=leetcode id=938 lang=python3
#
# 938. Range Sum of BST
#

# @lc code=start
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        q = deque([root])

        sumValue = 0

        while(len(q)):
            node = q.popleft()

            if node.val >= low and node.val <= high:
                sumValue += node.val

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return sumValue
# @lc code=end

adjLists = [
    [
        [10,5,15,3,7,None,18],
        7,
        15,
        32
    ],
    [
        [10,5,15,3,7,13,18,1,None,6],
        6,
        10,
        23
    ],
    [
        [],
        0,
        0,
        0
    ]
]

for [adjList, low, high, expect] in adjLists:
    node = buildTree(adjList)
    s = Solution()
    res = s.rangeSumBST(node, low, high)
    print(res == expect, res)
    print('')
    print('')
    print('')
