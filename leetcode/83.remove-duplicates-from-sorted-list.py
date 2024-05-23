from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)

        '''
        prev
        curr
        next
        '''

        prev = dummy
        curr = head

        while curr:
            next = curr.next

            if prev.val == curr.val:
                prev.next = next
            else:
                prev = curr

            curr = next
        
        return dummy.next


# @lc code=end

