from typing import List

'''
787. Cheapest Flights Within K Stops

There are n cities connected by some number of flights.
You are given an array flights where flights[i] = [fromi, toi, pricei]
indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops.
If there is no such route, return -1.
'''

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, max_stops: int) -> int:
        dp = [[float("inf") for _ in range(n)] for _ in range(max_stops+1)]

        for u,v,weight in flights:
            if u == src:
                dp[0][v] = weight

        for k in range(1,max_stops+1,1):
            for u,v,weight in flights:
                dp[k][v] = min(dp[k-1][u] + weight, dp[k-1][v], dp[k][v])

        # print(dp)

        if dp[max_stops][dst] == float("inf"):
            return -1

        return dp[max_stops][dst]


testCases = [
    {
        "flights": [
            [3,0,8],
            [1,4,1],
            [1,0,4],
            [1,3,3],
            [3,4,1],
            [2,3,3],
            [2,0,10]
        ],
        "n": 5,
        "src": 1,
        "dst": 4,
        "k": 4,
        "expected": 1
    },    
    {
        "flights": [
            [0,1,2]
        ],
        "n": 2,
        "src": 1,
        "dst": 0,
        "k": 0,
        "expected": -1
    },
    {
        "flights": [
            [1,0,5]
        ],
        "n": 2,
        "src": 0,
        "dst": 1,
        "k": 1,
        "expected": -1
    },
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
    {
        "flights": [
            [0,1,2],
            [1,2,1],
            [2,0,10]
        ],
        "n": 3,
        "src": 1,
        "dst": 2,
        "k": 1,
        "expected": 1
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
