#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

from typing import Optional, List

# @lc code=start
class Solution:
    count = 0

    def findContentChildren(self, children: List[int], cookies: List[int]) -> int:
        if len(cookies) == 0:
            return 0

        children.sort()
        cookies.sort()

        i = 0

        def findCookie(i: int, child: int) -> int:
            while i < len(cookies):
                cookie = cookies[i]

                i = i+1

                if cookie >= child:
                    self.count = self.count + 1 
                    break

            return i
                
        for child in children:
            i = findCookie(i, child)

        return self.count
                
        
# @lc code=end

inputs = [
    [
        [1,2,3], 
        [1,1],
        1
    ],
    [
        [1,2,3], 
        [1,2],
        2
    ],
    [
        [1], 
        [],
        0
    ],
    [
        [1], 
        [1],
        1
    ],
    [
        [2], 
        [1],
        0
    ],
    [
        [1], 
        [2],
        1
    ],
    [
        [10,9,8,7],
        [5,6,7,8],
        2
    ]
]

for [g, s, expected] in inputs:
    solution = Solution()
    res = solution.findContentChildren(g, s)
    print(res == expected, res, g, s)