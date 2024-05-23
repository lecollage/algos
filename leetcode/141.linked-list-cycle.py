from typing import Optional, List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        if head.next == head:
            return True

        slow = head.next
        fast = head.next.next

        while slow != fast and fast is not None:
            if fast.next is None:
                return False

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False

        
        
# @lc code=end

