from typing import List, Optional

#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, head: Optional['Node']) -> Optional['Node']:
        if head is None:
            return None
        
        stack=[head]
        graph = []
        visited = set()

        while len(stack) > 0:
            node = stack.pop(0)
            
            if node in visited:
                continue
            
            visited.add(node)

            # print(node.val, [x.val for x in node.neighbors])

            graph.append([x.val for x in node.neighbors])

            for neighbour in node.neighbors:
                stack.append(neighbour)

        # print(graph)

        hashMap = {
            i+1: Node(i+1) for i in range(len(graph))
        }

        # print(hashMap)

        for i, neighbours in enumerate(graph):
            value = i + 1
            hashMap[value].neighbors.extend(
                [hashMap[x] for x in neighbours]
            )

        return hashMap[1]
        

# @lc code=end

adjLists = [
    # [
    #     [2,4],
    #     [1,3],
    #     [2,4],
    #     [1,3]
    # ],
    [
        [2,3],
        [1,3],
        [1,2]
    ],
    # [
    #     [2,3],
    #     [1,3],
    #     [1,2],
    # ],
    # [
    #     [2,3],
    #     [1,3],
    #     [1,2,4],
    #     [3]
    # ],
    # [
    #     [2,3],
    #     [1,3],
    #     [1,2,4,5],
    #     [3,5],
    #     [3,4]
    # ],
    # [
    #     [2,3,4,5],
    #     [1,3,4,5],
    #     [1,2,4,5],
    #     [1,2,3,5],
    #     [1,2,3,4],
    # ],
]

for adjList in adjLists:
    hashMap = {i+1: Node(i+1) for i in range(len(adjList))}

    for i, neigbours in enumerate(adjList):
        value = i + 1

        hashMap[value].neighbors.extend(
            [hashMap[x] for x in neigbours]
        )

    for key, node in hashMap.items():
        print(key, [x.val for x in node.neighbors])

    print('')

    s=Solution()
    s.cloneGraph(hashMap[1])

    print('')
    print('')
    print('')
    print('')
    print('')


'''
{
    1: [2,4],
    2: [1,3],
    3: [2,4],
    4: [1,3]
}


original key
{
    1: ClonnedNode
    2: ClonnedNode
}


'''