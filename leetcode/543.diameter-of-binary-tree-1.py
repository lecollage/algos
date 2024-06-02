

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


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        depth = {None: 0}
        res = 0

        while len(stack) > 0:
            print(stack)

            node = stack.pop()

            if node is None:
                continue

            leftDepth = depth.get(node.left, None)
            rightDepth = depth.get(node.right, None)

            if leftDepth is None or rightDepth is None:
                stack.append(node)
                stack.append(node.left)
                stack.append(node.right)
                continue

            depth[node] = max(leftDepth, rightDepth) + 1
            res = max(leftDepth + rightDepth, res)

        return res

# @lc code=end

adjLists = [
    [
        [1,2,3,4,5],
        3
    ],
    [
        [1,2],
        1,
    ],
]

for [adjList, expect] in adjLists:
    node = buildTree(adjList)
    s = Solution()
    res = s.diameterOfBinaryTree(node)
    print(res == expect, res)
    print('')
    print('')
    print('')
