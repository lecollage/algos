from typing import List
from queue import Queue

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        graphRed = [[] for _ in range(n)]
        graphBlue = [[] for _ in range(n)]

        for u, v in redEdges:
            graphRed[u].append(v)

            if not v in graph[u]:
                graph[u].append(v)
            

        for u, v in blueEdges:
            graphBlue[u].append(v)

            if not v in graph[u]:
                graph[u].append(v)

        distances = [-1] * n
        distances[0] = 0
        colors = [{'R': 0, 'B': 0} for _ in range(n)] # R, B

        visited = [False] * n
        visited[0] = True

        # print(graph)
        # print(graphRed)
        # print(graphBlue)
        # print(distances)
        # print(colors)
        # print(visited)

        queue = Queue()

        queue.put((0, 0)) # node, distance
        
        while not queue.empty():
            node, distance = queue.get()
            neighbours = graph[node]

            # print(f"neighbour: {neighbour}; newDistance: {newDistance}; color: {color}")

            for neighbour in neighbours:
                if not visited[neighbour]:
                    newDistance = distance + 1
                    queue.put((neighbour, newDistance))
                    visited[neighbour] = True

                    distances[neighbour] = newDistance

                    colors[neighbour]['B'] = colors[node]['B']
                    colors[neighbour]['R'] = colors[node]['R']

                    # take the Blue edge for node and neighbour
                    if neighbour in graphBlue[node]:
                        colors[neighbour]['B'] += 1

                    if neighbour in graphRed[node]:
                        colors[neighbour]['R'] += 1
                    

        # print(distances)
        # print(colors)

        for i in range(n):
            color = colors[i]

            if distances[i] > 1 and (color['R'] == 0 or color['B'] == 0):
                distances[i] = -1

        return distances


testCases = [
    {
        "redEdges": [[0,1],[1,2]],
        "blueEdges": [],
        "n": 3,
        "expected": [0,1,-1]
    },
    {
        "redEdges": [[0,1]],
        "blueEdges": [[2,1]],
        "n": 3,
        "expected": [0,1,-1]
    },
    {
        "redEdges": [[0,1], [3,4], [1,5]],
        "blueEdges": [[1,3], [1,2]],
        "n": 6,
        "expected": [0,1,2,2,3,-1]
    },
    {
        "redEdges": [[0,1],[0,2]],
        "blueEdges": [[1,0]],
        "n": 3,
        "expected": [0,1,1]
    },
    {
        "redEdges": [[0,1],[1,2],[2,3],[3,4]],
        "blueEdges": [[1,2],[2,3],[3,1]],
        "n": 5,
        "expected": [0,1,2,3,7]
    },
]

for testCase in testCases:
    print('')

    redEdges = testCase["redEdges"]
    blueEdges = testCase["blueEdges"]
    n = testCase["n"]
    expected = testCase["expected"]

    s = Solution()

    result = s.shortestAlternatingPaths(n, redEdges, blueEdges)
    print(n, redEdges, blueEdges, result)
    assert result == expected, f"result {result} should be expected: {expected}"
