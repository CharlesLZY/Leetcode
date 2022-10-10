'''
Leetcode 92. Reverse Linked List II

Description:
Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.

Example:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
'''

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# @param head ListNode
# @param left int
# @param right int
# @return ListNode

### TC: O(n) and SC: O(1)
class Solution:
    def reverseBetween(self, head, left, right):
        
        dummy = ListNode()
        dummy.next = head ### trick: help to generalize all cases

        end = dummy
        i = 0
        while i < right+1:
            end = end.next
            i += 1

        start = dummy
        i = 0
        while i < left-1:
            start = start.next
            i += 1

        cur = start.next
        prev = end
        i = 0
        while i < right - left + 1:
            temp = cur
            start.next = cur
            cur = cur.next
            temp.next = prev
            prev = start.next
            i += 1

        return dummy.next


            
