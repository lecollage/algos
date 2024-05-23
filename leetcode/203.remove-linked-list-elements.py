from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        preHead = ListNode(-1, head)
        node = preHead

        # rem all from the beginning
        while node.next is not None and node.next.val == val:
            if node.next.next is not None:
                node.next = node.next.next
            else:
                node.next = None

        if node.next is None:
            return None
        
        # start from a new position
        head = node.next

        # rem the rest
        while node is not None and node.next is not None:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next

        return head
        
# @lc code=end

