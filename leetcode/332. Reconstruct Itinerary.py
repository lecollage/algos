from collections import deque
from typing import Optional, List

# @lc code=start
class Solution:
    def findItinerary(self, edges: List[List[str]]) -> List[str]:
        
        ...
# @lc code=end

testCases = [
   [
       [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]],
       ["JFK","MUC","LHR","SFO","SJC"],
   ],
   [
       [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]],
       ["JFK","ATL","JFK","SFO","ATL","SFO"],
   ],
]

for [n,arr,source,destination,expect] in testCases:
   s = Solution()
   res = s.leadsToDestination(n, arr, source, destination)
   print(res == expect, res)
   print('')
   print('')
   print('')