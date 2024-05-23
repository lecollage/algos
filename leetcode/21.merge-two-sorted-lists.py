from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, node1: Optional[ListNode], node2: Optional[ListNode]) -> Optional[ListNode]:
        if node1 is None:
            return node2
        
        if node2 is None:
            return node1

        mergedHead: ListNode

        if node1.val < node2.val:
            mergedHead = ListNode(node1.val)
            node1 = node1.next
        else:
            mergedHead = ListNode(node2.val)
            node2 = node2.next

        mergedNode = mergedHead

        while node1 is not None and node2 is not None:
            if node1.val < node2.val:
                mergedNode.next = ListNode(node1.val)
                node1 = node1.next
            else:
                mergedNode.next = ListNode(node2.val)
                node2 = node2.next
            
            mergedNode = mergedNode.next

        while node1 is not None:
            mergedNode.next = ListNode(node1.val)
            node1 = node1.next
            mergedNode = mergedNode.next

        while node2 is not None:
            mergedNode.next = ListNode(node2.val)
            node2 = node2.next
            mergedNode = mergedNode.next

        return mergedHead

# @lc code=end

