from typing import List
from queue import PriorityQueue


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
            graph[u] = (v, price)

        print(graph)

        visited = [False] * n
        queue = PriorityQueue()

        k += 1
        queue.put((0, src, 0))

        while not queue.empty():
            distance, node, edgeCount = queue.get()

            if node == dst:
                return distance

            for neighbour, weight in graph[node]:
                if not visited[neighbour] and edgeCount < k:
                    queue.put((distance + weight, neighbour, edgeCount + 1))

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
        "src": 2,
        "dst": 2,
        "k": 2,
        "expected": 700
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
