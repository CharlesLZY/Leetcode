'''
Leetcode 19. Remove Nth Node From End of List

Description:
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# @param head ListNode 
# @param n int
# @return ListNode

### TC: O(n) and SC: O(1)
class Solution:
    def removeNthFromEnd(self, head, n):
        temp = ListNode()
        temp.next = head
        fast = head
        for i in range(n):
            fast = fast.next
        slow = head
        prev = temp
        while fast:
            prev, slow = slow, slow.next
            fast = fast.next
        prev.next = slow.next
        return temp.next