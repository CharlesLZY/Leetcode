'''
Leetcode 83. Remove Duplicates from Sorted List

Description:
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
'''

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# @param head ListNode
# @return ListNode

### TC: O(n) and SC: O(1)
class Solution:
    def deleteDuplicates(self, head):
    	if head is None:
            return None
        prev = head
        cur = head.next 
        while cur:
            while cur and cur.val == prev.val:
                cur = cur.next
            prev.next = cur
            prev = prev.next
            if cur:
                cur = cur.next
        return head
