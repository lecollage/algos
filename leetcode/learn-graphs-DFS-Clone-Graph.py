
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# @lc code=start
from typing import Optional
class Solution:
    def cloneGraphInternal(self, node: Optional['Node'], cloneNode: Optional['Node']) -> Optional['Node']:
            
            for neighbor in node.neighbors:
                self.cloneGraphInternal(neighbor)

                clonnedNode.neighbors

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        clonnedNode = Node(node.val)

        self.cloneGraphInternal(node, clonnedNode)

# @lc code=end

'''
'''


testCases = [
    {
        "graph": [[2,4],[1,3],[2,4],[1,3]],
        "expected": [[2,4],[1,3],[2,4],[1,3]]
    },
]

for testCase in testCases:
    print('')

    graph = testCase["graph"]
    expected = testCase["expected"]

    s = Solution()

    result = s.allPathsSourceTarget(graph)
    print(graph)
    assert result == expected, f"result {result} should be expected: {expected}"
