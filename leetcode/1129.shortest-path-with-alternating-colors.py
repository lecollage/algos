from typing import List
from queue import Queue

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graphRed = [[] for _ in range(n)]
        graphBlue = [[] for _ in range(n)]

        for u, v in redEdges:
            graphRed[u].append(v)
            
        for u, v in blueEdges:
            graphBlue[u].append(v)

        # print(graphRed)
        # print(graphBlue)

        graph = (
            graphBlue,
            graphRed
        )

        # B - 0
        # R - 1

        distances = (
            [-1] * n, # B
            [-1] * n  # R
        )

        distances[0][0] = 0
        distances[1][0] = 0

        # print(distances)

        queue = Queue()

        queue.put((0, 0)) # node, color
        queue.put((0, 1)) # node, color

        # [0, 1, 0, 0, 0, -1]

        while not queue.empty():
            node, color = queue.get()
            parentDistance = distances[color][node]

            nextColor = (color + 1) % 2
            neighbors = graph[nextColor][node]

            for neighbor in neighbors:
                distance = distances[nextColor][neighbor]
                
                # if not visited
                if distance != -1:
                    continue

                distances[nextColor][neighbor] = parentDistance + 1
                queue.put((neighbor, nextColor))

        resultDistances = [-1] * n
        resultDistances[0] = 0

        for i in range(n):
            blueDistance = distances[0][i]
            redDistance = distances[1][i]

            if blueDistance == -1 and redDistance != -1:
                resultDistances[i] = redDistance
            elif blueDistance != -1 and redDistance == -1:
                resultDistances[i] = blueDistance
            elif blueDistance != -1 and redDistance != -1:
                resultDistances[i] = min(redDistance, blueDistance)

        return resultDistances

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

'''




'''

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
