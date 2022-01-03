'''
Leetcode 206. Reverse Linked List

Description:
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# @param head ListNode 
# @return ListNode

### TC: O(n) and SC: O(1)
class Solution:
    def reverseList(self, head):
        dummy = ListNode()
        cur = head
        while cur:
            temp = cur.next
            cur.next = dummy.next
            dummy.next = cur
            cur = temp
        return dummy.next