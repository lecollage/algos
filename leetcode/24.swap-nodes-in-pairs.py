from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        if head.next is None:
            return head

        dummy = ListNode(None, head)
        prev = dummy
        curr = head
        nxt = curr.next

        while curr and curr.next:
            prev.next = curr.next

            if nxt is not None:
                curr.next = nxt.next
                nxt.next = curr
            else:
                curr.next = None

            prev = curr
            curr = curr.next
            nxt = curr.next if curr is not None else None

        return dummy.next

# @lc code=end

