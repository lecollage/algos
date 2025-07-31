from typing import List

'''
787. Cheapest Flights Within K Stops

No K
'''

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int) -> int:
        distances = [float("inf")] * n

        distances[src] = 0

        # max simple path length by edges
        for _ in range(2):
            for u, v, weight in flights:
                distances[v] = min(distances[v], distances[u]+weight)

        print(distances)

        if distances[dst] == float("inf"):
            return -1

        return distances[dst]



testCases = [
    {
        "flights": [
            [1,3,600],
            [0,1,100],
            [1,2,100],
            [2,0,100],
            [2,3,200]
        ],
        "n": 4,
        "src": 0,
        "dst": 3,
        "expected": 400
    },
    {
        "flights": [
            [0,1,2],
            [1,2,1],
            [2,0,10]
        ],
        "n": 3,
        "src": 1,
        "dst": 2,
        "expected": 1
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
        "expected": 11
    },
]


for testCase in testCases:
    print('')

    flights = testCase["flights"]
    n = testCase["n"]
    src = testCase["src"]
    dst = testCase["dst"]
    expected = testCase["expected"]

    s = Solution()

    result = s.findCheapestPrice(n, flights, src, dst)
    print(n, flights, src, dst,  result)
    assert result == expected, f"result {result} should be expected: {expected}"
