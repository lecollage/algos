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
# @lc app=leetcode id=199 lang=python3
#
# 199. Binary Tree Right Side View
#

# @lc code=start
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque()

        q.appendleft((root, 0)) # node, level

        rightView = [None]*100
        rightView[0] = root.val

        while(len(q)):
            node, level = q.popleft()

            # print(node.val, level)
            
            rightView[level] = node.val

            if node.right:
                q.appendleft((node.right, level+1))

            if node.left:
                q.appendleft((node.left, level+1))

        rightViewResult = []

        for el in rightView:
            if el != None:
                rightViewResult.append(el)
            else:
                return rightViewResult

        return rightViewResult
# @lc code=end

adjLists = [
    [
        [1,2,3,None,5,None,4],
        [1,3,4]
    ],
    [
        [1,2,3,4,None,None,None,5],
        [1,3,4,5]
    ],
    [
        [1,None,3],
        [1,3]
    ],
    [
        [],
        []
    ],
]

for [adjList, expect] in adjLists:
    node = buildTree(adjList)
    s = Solution()
    res = s.rightSideView(node)
    print(res == expect, res)
    print('')
    print('')
    print('')
