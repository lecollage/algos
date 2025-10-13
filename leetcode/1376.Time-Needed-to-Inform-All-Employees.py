from typing import List
from collections import deque

#
# @lc app=leetcode id=1376 lang=python3
#
# 1376. Time Needed to Inform All Employees
#

# @lc code=start
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        tree = [[] for _ in range(n)]

        for i, m in enumerate(manager):
            if m != -1:
                tree[m].append(i)

        q = deque()

        q.append((headID, 0)) # node, distance

        maxDistance = 0

        while len(q) > 0:
            node, distance = q.popleft()

            if len(tree[node]) == 0:
                maxDistance = max(maxDistance, distance)

            for neigbour in tree[node]:
                q.append((neigbour, distance + informTime[node]))


        return maxDistance
# @lc code=end


testCases = [
    {
        "n": 1,
        "headID": 0,
        "manager": [-1],
        "informTime": [0],
        "expected": 0
    },
    {
        "n": 6,
        "headID": 2,
        "manager": [2,2,-1,2,2,2],
        "informTime": [0,0,1,0,0,0],
        "expected": 1
    },
]

for testCase in testCases:
    print('')

    n = testCase["n"]
    headID = testCase["headID"]
    manager = testCase["manager"]
    informTime = testCase["informTime"]
    expected = testCase["expected"]

    s = Solution()

    result = s.numOfMinutes(n, headID, manager, informTime)
    print(n, headID, manager, informTime, result)
    assert result == expected, f"result {result} should be expected: {expected}"
