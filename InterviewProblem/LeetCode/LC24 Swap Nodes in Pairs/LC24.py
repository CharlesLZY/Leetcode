'''
Leetcode 24. Swap Nodes in Pairs

Description:
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
'''

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# @param head ListNode
# @return ListNode

### TC: O(n) and SC: O(1)
class Solution:
    def swapPairs(self, head):
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            prev.next = slow.next
            prev.next.next = slow
            slow.next = fast
            prev = prev.next.next
            slow = fast

        return dummy.next
