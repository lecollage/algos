# @lc code=start
from typing import Optional, List
class Solution:
    def findItinerary(self, edges: List[List[str]]) -> List[str]:
        graph = {}

        for u,v in edges:
            graph[u] = set()
            graph[v] = set()

        for u,v in edges:
            graph[u].add(v)

        for u in graph:
            s = graph[u]
            a = list(s)
            
            a.sort()
            a.reverse()

            graph[u] = a
            
        # print(graph)
        
        visited = set()
        stack = ['JFK']
        path = []

        while len(stack):
            node = stack.pop()

            path.append(node)
            # print(node)

            for neighbour in graph[node]:
                edge = (node, neighbour)

                if edge not in visited:
                    stack.append(neighbour)
                    visited.add(edge)

        return path
# @lc code=end

'''
'''


testCases = [
    # {
    #     "edges": [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]],
    #     "expected": ["JFK","ATL","JFK","SFO","ATL","SFO"]
    # },
    # {
    #     "edges": [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]],
    #     "expected": ["JFK","MUC","LHR","SFO","SJC"]
    # },
    {
        "edges": [["JFK","SFO"],["JFK","ATL"],["SFO","JFK"],["ATL","AAA"],["AAA","ATL"],["ATL","BBB"],["BBB","ATL"],["ATL","CCC"],["CCC","ATL"],["ATL","DDD"],["DDD","ATL"],["ATL","EEE"],["EEE","ATL"],["ATL","FFF"],["FFF","ATL"],["ATL","GGG"],["GGG","ATL"],["ATL","HHH"],["HHH","ATL"],["ATL","III"],["III","ATL"],["ATL","JJJ"],["JJJ","ATL"],["ATL","KKK"],["KKK","ATL"],["ATL","LLL"],["LLL","ATL"],["ATL","MMM"],["MMM","ATL"],["ATL","NNN"],["NNN","ATL"]],
        "expected": ["JFK","SFO","JFK","ATL","AAA","ATL","BBB","ATL","CCC","ATL","DDD","ATL","EEE","ATL","FFF","ATL","GGG","ATL","HHH","ATL","III","ATL","JJJ","ATL","KKK","ATL","LLL","ATL","MMM","ATL","NNN","ATL"]
    }
]

for testCase in testCases:
    print('')

    edges = testCase["edges"]
    expected = testCase["expected"]

    s = Solution()

    result = s.findItinerary(edges)
    print(edges)
    assert result == expected, f"result {result} should be expected: {expected}"
