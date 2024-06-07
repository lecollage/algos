from typing import List, Optional

#
# @lc app=leetcode id=1361 lang=python3
#
# [1361] Validate Binary Tree Nodes
#

# @lc code=start
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        hasParent = set(leftChild + rightChild)
        hasParent.discard(-1)

        if len(hasParent) == n:
            return False
        
        root = -1

        for i in range(len(hasParent)):
            if i not in hasParent:
                root = i
                break

        visited = set()
        def dfs(i: int) -> bool:
            if i == -1:
                return True

            if i in visited:
                return False

            visited.add(i)

            return dfs(leftChild[i]) and dfs(rightChild[i])
        
        return dfs(root) and len(visited) == n
# @lc code=end

inputs = [
    [
        2,
        [-1,0],
        [-1,-1],
        False,
    ]

]

for [n,l,r,expect] in inputs:
    s = Solution()

    res = s.validateBinaryTreeNodes(n,l,r)
    print(res == expect)

'''
 0  1  2   3
[1,-1, 3, -1]
[2,-1,-1, -1]

3


            0
        /       \
       1         2
   -1    -1    3    -1
              / \
            -1  -1

    0
    1

    [l1..l2)

         lvl/2-1
  1  2    0
  2  4    1
  3  8    3
  4  16   7

  2



            0
        -1     -1
      0    -1
'''