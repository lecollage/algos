from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        elements = []

        while curr:
            elements.append(curr)
            curr = curr.next

        return elements[int(len(elements)/2)]

# @lc code=end



# print(int(6/2))
# print(int(5/2))