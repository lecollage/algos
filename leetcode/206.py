from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            return head

        prev = head
        curr = head.next

        prev.next = None

        while curr:
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next

        return curr

'''
O -> O -> O
prev = head
curr = head.next

next = curr.next
curr.next = prev

prev = curr
curr = next


O <- O <- O


O <- O
'''
