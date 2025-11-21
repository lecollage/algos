from typing import List
from collections import deque

#
# @lc app=leetcode id=1306 lang=python3
#
# 1306. Jump Game III
#

# @lc code=start
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False]*n

        q = deque([start])

        while(len(q) > 0):
            i = q.popleft()

            if arr[i] == 0:
                return True

            nextRightIndx = i + arr[i]

            if nextRightIndx > -1 and nextRightIndx < n and not visited[nextRightIndx]:
                q.append(nextRightIndx)
                visited[nextRightIndx] = True

            nextLeftIndx = i - arr[i]

            if nextLeftIndx > -1 and nextLeftIndx < n and not visited[nextLeftIndx]:
                q.append(nextLeftIndx)
                visited[nextLeftIndx] = True

        return False
# @lc code=end
testCases = [
    [
        [4,2,3,0,3,1,2],
        5,
        True
    ],
    [
        [4,2,3,0,3,1,2],
        0,
        True
    ],
    [
        [3,0,2,1,2],
        2,
        False
    ],
]

for arr, start, expected  in testCases:
    print(arr, start, expected, expected)

    s = Solution()
    result = s.canReach(arr, start)

    assert result == expected, f"result {result} should be expected: {expected}"

    print('')
    print('')
    print('')