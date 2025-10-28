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
# @lc app=leetcode id=1302 lang=python3
#
# 1302. Deepest Leaves Sum
#

# @lc code=start
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([(root, 0)])
        sum = 0
        levelsSum = {}

        while len(q):
            node,level = q.popleft()

            if node.left:
                q.append((node.left, level+1))

            if node.right:
                q.append((node.right, level+1))

            if not node.left and not node.right:
                if level in levelsSum:
                    levelsSum[level] += node.val
                else:
                    levelsSum[level] = node.val

        # print(levelsSum)

        maxLevel = 0

        for level in levelsSum:
            maxLevel = max(maxLevel, level)
        
        return levelsSum[maxLevel]
# @lc code=end

adjLists = [
    [
        [1,2,3,4,5,None,6,7,None,None,None,None,8],
        15
    ],
    [
        [6,7,8,2,7,1,3,9,None,1,4,None,None,None,5],
        19
    ],
    [
        [],
        0
    ],
]

for [adjList, expect] in adjLists:
    node = buildTree(adjList)
    s = Solution()
    res = s.deepestLeavesSum(node)
    print(res == expect, res)
    print('')
    print('')
    print('')
