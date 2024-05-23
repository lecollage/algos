from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dictA = {}
        dictB = {}

        currA = headA

        while currA:
            dictA[currA] = currA.val
            currA = currA.next

        currB = headB

        while currB:
            if currB in dictA:
                return currB

            dictB[currB] = currB.val
            currB = currB.next

        return None

# @lc code=end

