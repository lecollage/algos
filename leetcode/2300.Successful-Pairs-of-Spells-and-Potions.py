from collections import deque
from typing import Optional, List

# @lc code=start
class Solution:
    def do(self, multiplier: int, arr: List[int], target: int) -> int:
        left = 0
        right = len(arr)

        while left < right:
            mid = (left + right)//2

            if multiplier * arr[mid] >= target:
                right = mid
            else:
                left = mid + 1

        print(multiplier,target,left, right)

        return len(arr) - left
    
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort(key=lambda x:x)

        ans = []

        for spell in spells:
            ans.append(self.do(spell, potions, success))

        return ans
# @lc code=end

testCases = [
   [
       [5,1,3],
       [1,2,3,4,5],
       7,
       [4,0,3]
   ],
   [
       [3,1,2],
       [8,5,8],
       16,
       [2,0,2]
   ],
]

for [spells,potions,success,expect] in testCases:
   s = Solution()
   res = s.successfulPairs(spells,potions,success)
   print(res == expect, res)
   print('')
   print('')
   print('')