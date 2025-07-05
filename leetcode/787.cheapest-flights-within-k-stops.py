from typing import List
from queue import PriorityQueue, Queue
import math



'''
787. Cheapest Flights Within K Stops

There are n cities connected by some number of flights.
You are given an array flights where flights[i] = [fromi, toi, pricei]
indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops.
If there is no such route, return -1.
'''

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]

        for u, v, price in flights:
            graph[u].append((v, price))

        # print(graph)

        k += 1

        queue = PriorityQueue()

        queue.put((0, src, 0))

        minNodeEdges = [float("inf")] * n

        while not queue.empty():
            current_distance, current_node, current_edges = queue.get()

            if current_node == dst: 
                return current_distance

            if current_edges > minNodeEdges[current_node]:
                continue

            minNodeEdges[current_node] = current_edges

            for neighbour, weight in graph[current_node]:
                nextDistance = current_distance + weight
                nextEdges = current_edges + 1

                if nextEdges <= k:
                    queue.put((nextDistance, neighbour, nextEdges))

        return -1


testCases = [
    {
        "flights": [
            [0,1,100],
            [1,2,100],
            [2,0,100],
            [1,3,600],
            [2,3,200]
        ],
        "n": 4,
        "src": 0,
        "dst": 3,
        "k": 1,
        "expected": 700
    },
    {
        "flights": [
            [0,1,1],
            [0,2,5],
            [1,2,1],
            [2,3,1]
        ],
        "n": 4,
        "src": 0,
        "dst": 3,
        "k": 1,
        "expected": 6
    },
    {
        "flights": [
            [0,1,1],
            [0,2,5],
            [1,2,1],
            [2,3,1],
            [1,3,4],
        ],
        "n": 4,
        "src": 0,
        "dst": 3,
        "k": 1,
        "expected": 5
    },
    {
        "flights": [
            [0,1,100],
            [1,2,100],
            [0,2,500]
        ],
        "n": 3,
        "src": 0,
        "dst": 2,
        "k": 1,
        "expected": 200
    },
    {
        "flights": [
            [0,3,3],
            [3,4,3],
            [4,1,3],
            [0,5,1],
            [5,1,100],
            [0,6,2],
            [6,1,100],
            [0,7,1],
            [7,8,1],
            [8,9,1],
            [9,1,1],
            [1,10,1],
            [10,2,1],
            [1,2,100]
        ],
        "n": 11,
        "src": 0,
        "dst": 2,
        "k": 4,
        "expected": 11
    },
]


for testCase in testCases:
    print('')

    flights = testCase["flights"]
    n = testCase["n"]
    k = testCase["k"]
    src = testCase["src"]
    dst = testCase["dst"]
    expected = testCase["expected"]

    s = Solution()

    result = s.findCheapestPrice(n, flights, src, dst, k)
    print(n, flights, src, dst, k, result)
    assert result == expected, f"result {result} should be expected: {expected}"
