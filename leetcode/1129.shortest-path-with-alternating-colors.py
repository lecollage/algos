from typing import List
from queue import Queue

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]

        for u, v in redEdges:
            graph[u].append((v, 'R'))

        for u, v in blueEdges:
            graph[u].append((v, 'B'))

        distances = [-1] * n

        distances[0] = 0

        colors = [{'R': 0, 'B': 0} for _ in range(n)] # R, B
        visited = [False] * n

        # print(graph)
        # print(distances)
        # print(colors)
        # print(visited)

        queue = Queue()

        queue.put((0, 0)) # node, distance
        
        while not queue.empty():
            node, distance = queue.get()
            neighbours = graph[node]

            # print(f"neighbour: {neighbour}; newDistance: {newDistance}; color: {color}")

            for neighbour, color in neighbours:
                if not visited[neighbour]:
                    newDistance = distance + 1
                    queue.put((neighbour, newDistance))
                    visited[neighbour] = True
                    distances[neighbour] = newDistance

                    if color == 'R':
                        colors[neighbour]['R'] = colors[node]['R'] + 1
                        colors[neighbour]['B'] = colors[node]['B']
                    elif color == 'B':
                        colors[neighbour]['R'] = colors[node]['R']
                        colors[neighbour]['B'] = colors[node]['B'] + 1

                    
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
