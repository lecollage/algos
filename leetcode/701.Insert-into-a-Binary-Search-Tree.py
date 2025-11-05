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
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        def dfs(node: TreeNode):
            if node.val > val:
                if node.left:
                    dfs(node.left)
                else:
                    node.left = TreeNode(val)
            elif val > node.val:
                if node.right:
                    dfs(node.right)
                else:
                    node.right = TreeNode(val)

        dfs(root)

        return root
# @lc code=end

adjLists = [
    [
        [4,2,7,1,3],
        5,
        [4,2,7,1,3,5],
    ],
    [
        [40,20,60,10,30,50,70],
        5,
        [4,2,7,1,3,5],
    ],
]

for [tree, val, expect] in adjLists:
    t = buildTree(tree)

    s = Solution()
    res = s.insertIntoBST(t, val)
    print(res == expect, res)
    print('')
    print('')
    print('')
