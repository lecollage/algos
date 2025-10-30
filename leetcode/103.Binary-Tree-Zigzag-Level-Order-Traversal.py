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
# @lc app=leetcode id=103 lang=python3
#
# 103. Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([root])
        ans = []

        leftFirst = True

        while(len(q)):
            currLen = len(q)
            level = deque()

            for _ in range(currLen):
                node = q.popleft()

                if leftFirst:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)

                # print(node.val,leftFirst,level)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            leftFirst = not leftFirst
            ans.append(list(level))

        return ans
# @lc code=end

adjLists = [
    [
        [3,9,20,1,None,15,7],
        [[3],[20,9],[1,15,7]]
    ],
    [
        [1],
        [[1]]
    ],
    [
        [1,2,3,4,None,None,5],
        [[1],[3,2],[4,5]]
    ],
    [
        [],
        []
    ],
]

for [adjList, expect] in adjLists:
    node = buildTree(adjList)
    s = Solution()
    res = s.zigzagLevelOrder(node)
    print(res == expect, res)
    print('')
    print('')
    print('')
