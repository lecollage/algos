from typing import List, Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        stack = [node]
        clonnedGraph = Node(node.val, node.neighbors)
        stackClone = [clonnedGraph]

        while len(stack) > 0:
            currNode = stack.pop()
            clonnedNode = stackClone.pop()

            # print(currNode.val)
            # print(currNode)

            for i, neighbor in enumerate(currNode.neighbors):
                stack.append(neighbor)
                clonnedNode.neighbors.append(Node(neighbor.val))
                stackClone
                

        return clonnedGraph


inputs = [
    [
        [
            [2,4],
            [1,3],
            [2,4],
            [1,3]
        ],
    ],
    
]
s = Solution()
for [grid] in inputs:
    grid

    print(s.cloneGraph(grid))