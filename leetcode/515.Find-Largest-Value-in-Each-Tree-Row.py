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
# @lc app=leetcode id=515 lang=python3
#
# 515. Find Largest Value in Each Tree Row
#

# @lc code=start
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque()

        q.append(root)
        levelMaxes = []

        while(len(q)):
            curr_len = len(q)
            # print('')

            maxLevelEl = None

            for _ in range(curr_len):
                node = q.popleft()
                # print(node.val)

                maxLevelEl = node.val if maxLevelEl == None else max(maxLevelEl, node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            levelMaxes.append(maxLevelEl)

        return levelMaxes
# @lc code=end

adjLists = [
    [
        [1,3,2,5,3,None,9],
        [1,3,9]
    ],
    [
        [1,2,3],
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
    res = s.largestValues(node)
    print(res == expect, res)
    print('')
    print('')
    print('')
