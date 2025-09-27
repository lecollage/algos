
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def serialize_graph(node: Node):
    if not node:
        return {}

    visited = set()
    adj_list = {}
    queue = deque([node])

    while queue:
        current = queue.popleft()
        if current.val in visited:
            continue
        visited.add(current.val)

        # store neighbor values
        adj_list[current.val] = [n.val for n in current.neighbors]

        # add neighbors to queue
        for neighbor in current.neighbors:
            if neighbor.val not in visited:
                queue.append(neighbor)

    return adj_list

# @lc code=start
from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clonnedNode = Node(node.val)

        visited = {}

        visited[clonnedNode.val] = clonnedNode

        def DFS(node: Optional['Node'], clonnedNode: Node):
            if not node:
                return

            print(node.val, clonnedNode.val)

            for neighbor in node.neighbors:
                clonnedNeighbor = visited[neighbor.val] if neighbor.val in visited else Node(neighbor.val)
                print('   ', neighbor.val)

                clonnedNode.neighbors.append(clonnedNeighbor)

                if clonnedNeighbor.val not in visited:
                    visited[clonnedNeighbor.val] = clonnedNeighbor
                    DFS(neighbor, clonnedNeighbor)
        
        DFS(node, clonnedNode)

        return clonnedNode
# @lc code=end

'''
'''


def case1():
    print('')

    graph = Node(10)
    node1 = Node(20)
    node2 = Node(30)
    node3 = Node(40)
    node4 = Node(50)
    node5 = Node(60)
    node2.neighbors = [node4, node5]
    graph.neighbors = [node1, node2, node3] 

    print(serialize_graph(graph))

    s = Solution()

    result = s.cloneGraph(graph)

    print(serialize_graph(result))

    # assert result == expected, f"result {result} should be expected: {expected}"

def case2():
    print('')

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    graph = node1

    print(serialize_graph(graph))

    s = Solution()

    result = s.cloneGraph(graph)


    print(serialize_graph(result))
    print(result.neighbors[1].val)
    print(result.neighbors[1].neighbors)

    # result.val = 999
    # result.neighbors[1].val = 666

    # print(serialize_graph(graph))
    # print(serialize_graph(result))

    # assert result == expected, f"result {result} should be expected: {expected}"


[[2,4],[1,3],[2,4],[1,3]]
case1()
case2()