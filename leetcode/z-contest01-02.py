from typing import List
from collections import deque


'''
Q2. Maximum Balanced Shipments
Medium
5 pt.
You are given an integer array weight of length n, representing the weights of n parcels arranged in a straight line. A shipment is defined as a contiguous subarray of parcels. A shipment is considered balanced if the weight of the last parcel is strictly less than the maximum weight among all parcels in that shipment.

Select a set of non-overlapping, contiguous, balanced shipments such that each parcel appears in at most one shipment (parcels may remain unshipped).

Return the maximum possible number of balanced shipments that can be formed.

 ©leetcode
'''

# @lc code=start
class Solution:
    def maxBalancedShipments(self, weights: List[int]) -> int:
        if len(weights) < 2:
            return 0

        n = len(weights)
        shipments = 0

        i = 0
        j = 1
        maxW = weights[0]

        while j < n:
            maxW = max(weights[i], weights[j])

            if weights[j] < maxW:
                shipments += 1

                i = j+1
                j = i+1
            else:
                i += 1
                j += 1

        return shipments
        
# @lc code=end


testCases = [
    {
        "arr": [2,5,1,4,3],
        "expected": 2
    },
    {
        "arr": [1,3,5,4,2,6],
        "expected": 1
    },
    {
        "arr": [2,1,3],
        "expected": 1
    },
    {
        "arr": [4,4],
        "expected": 0
    },
    {
        "arr": [4],
        "expected": 0
    },
    {
        "arr": [4, 1, 2, 3],
        "expected": 1
    },
    {
        "arr": [1, 2, 2, 2],
        "expected": 0
    },
    {
        "arr": [1, 2, 2, 2, 3],
        "expected": 0
    },
    {
        "arr": [1, 2, 2, 2, 1],
        "expected": 1
    },
]

for testCase in testCases:
    print('')

    arr = testCase["arr"]
    expected = testCase["expected"]

    s = Solution()

    result = s.maxBalancedShipments(arr)
    print(arr, result)
    assert result == expected, f"result {result} should be expected: {expected}"

