from typing import List

#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        queue = [(0,0)]
        results = [[False]*len(heights[0]) for i in heights]

        for i, row in enumerate(heights):
            for j, el in enumerate(row):
                
                

        




# @lc code=end


inputs = [
    [
        [
            [1,2,2,3,5],
            [3,2,3,4,4],
            [2,4,5,3,1],
            [6,7,1,4,5],
            [5,1,1,2,4]
        ],
        [
            [0,4],
            [1,3],
            [1,4],
            [2,2],
            [3,0],
            [3,1],
            [4,0]
        ]
    ]
]

for [list, expected] in inputs:
    s = Solution()
    s.pacificAtlantic(list)




'''
i == 0 || j == 0 -> Pacific
i == len(list)-1 || j == len(len(list[0]))-1 -> Atlantic
'''




'''
        s = set()

        s.add((1,2))
        s.add((1,2))

        print(s)


        if (1,2) in s:
            print('in')



while len(queue):
            i,j = queue.pop(0)

            # print(i,j)

            pacific = False
            atlantic = False

            if i == 0 or j == 0:
                pacific = True

            if i == len(heights)-1 or j == len(heights[-1])-1:
                atlantic = True

            if i > 0:
                queue.append((i-1,j))

            if i < len(heights)-1:
                queue.append((i+1,j))

            if j > 0:
                queue.append((i,j-1))
            
            if j < len(heights[i])-1:
                queue.append((i,j+1))
'''    