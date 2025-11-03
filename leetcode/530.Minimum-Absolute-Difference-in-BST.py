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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = []

        def dfs(node: Optional[TreeNode]):
            if not node:
                return

            dfs(node.left)

            arr.append(node.val)

            dfs(node.right)

        dfs(root)

        # print(arr)

        minDiff = 10**9

        for i in range(0,len(arr)-1):
            minDiff = min(minDiff, arr[i+1]-arr[i])

        return minDiff
# @lc code=end

adjLists = [
    [
        [4,2,6,1,3],
        1,
    ],
    [
        [1,0,48,None,None,12,49],
        1,
    ],
]

for [tree, expect] in adjLists:
    t = buildTree(tree)

    s = Solution()
    res = s.getMinimumDifference(t)
    print(res == expect, res)
    print('')
    print('')
    print('')
