from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # find a root
        middle = int(len(nums)/2)
        rootNode = TreeNode(nums[middle])

        leftParent = rootNode

        for i in range(middle-1, -1, -1):
            leftParent.left = TreeNode(nums[i])
            leftParent = leftParent.left

        rightParent = rootNode
        for i in range(middle+1, len(nums), 1):
            rightParent.right = TreeNode(nums[i])
            rightParent = rightParent.right

        return rootNode

# @lc code=end

inputs = [
    [
        [-10,-3,0,5,9]
    ]
]

for [arr] in inputs:
    s = Solution()
    root = s.sortedArrayToBST(arr)

    def serializeHelper(node, vals):
        if node:
            vals.append(node.val)
            serializeHelper(node.left, vals)
            serializeHelper(node.right, vals)

    vals = []
    serializeHelper(root, vals)

    print(vals)

