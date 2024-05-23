from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        nums = []

        while curr:
            nums.append(curr.val)
            curr = curr.next

        i = 0
        j = len(nums)-1

        while i <= j:
            if nums[i] != nums[j]:
                return False
        
            i = i + 1
            j = j - 1

        return True


# @lc code=end



def f():
    nums = [1,2,2,1]

    i = 0
    j = len(nums)-1

    while i <= j:
        if nums[i] != nums[j]:
            return False
    
        i = i + 1
        j = j - 1

    return True

print(f())