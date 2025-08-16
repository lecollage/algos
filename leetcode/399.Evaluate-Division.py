from typing import List
from collections import deque
from queue import Queue

'''
399. Evaluate Division

You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
Return the answers to all queries. If a single answer cannot be determined, return -1.0.
Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.
 
Constraints:
    1 <= equations.length <= 20
    equations[i].length == 2
    1 <= Ai.length, Bi.length <= 5
    values.length == equations.length
    0.0 < values[i] <= 20.0
    1 <= queries.length <= 20
    queries[i].length == 2
    1 <= Cj.length, Dj.length <= 5
    Ai, Bi, Cj, Dj consist of lower case English letters and digits.
'''

class Solution:
    def BFS(self, graph, src, dst) -> float:
        queue = Queue()
        visited = set()

        queue.put((src, 1))

        while not queue.empty():
            node, pathCost = queue.get()

            if node == dst:
                return pathCost

            if node in visited:
                continue

            visited.add(node)

            for neighbour, w in graph.get(node, []):
                if neighbour not in visited:
                    queue.put((neighbour, pathCost * w))
        
        return -1


    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}

        for i,(u,v) in enumerate(equations):
            if u not in graph:
                graph[u] = [(v, values[i])]
            else:
                graph[u].append((v, values[i]))

            if v not in graph:
                graph[v] = [(u, 1/values[i])]
            else:
                graph[v].append((u, 1/values[i]))


        print(graph)

        costs = []

        for src, dst in queries:
            print("query: ", src, dst)

            if src not in graph or dst not in graph:
                costs.append(-1)
            else:
                pathCost = self.BFS(graph, src, dst)
                costs.append(pathCost)

        return costs

'''
'''
testCases = [
    {
        "equations": [["a","b"],["b","c"]],
        "values": [2.0,3.0],
        "queries": [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]],
        "expected": [6.00000,0.50000,-1.00000,1.00000,-1.00000]
    },
    {
        "equations": [["a","b"],["b","c"],["bc","cd"]],
        "values": [1.5,2.5,5.0],
        "queries": [["a","c"],["c","b"],["bc","cd"],["cd","bc"]],
        "expected": [3.75000,0.40000,5.00000,0.20000]
    },
    {
        "equations": [["a","b"]],
        "values": [0.5],
        "queries": [["a","b"],["b","a"],["a","c"],["x","y"]],
        "expected": [0.50000,2.00000,-1.00000,-1.00000]
    },
]


for testCase in testCases:
    print()

    equations = testCase["equations"]
    values = testCase["values"]
    queries = testCase["queries"]
    expected = testCase["expected"]

    s = Solution()
    result = s.calcEquation(equations, values, queries)
    print(equations, values, queries)

    assert result == expected, f"result {result} should be expected: {expected}"