'''
Leetcode 2. Add Two Numbers

Description:
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit.
 Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# @param l1 ListNode 
# @param l2 ListNode 
# @return ListNode

### TC: O(n) and SC: O(1)
class Solution:
    def addTwoNumbers(self, l1, l2):
        res = ListNode()
        cur = res
        carry = 0 ### addition carry
        while l1 or l2 or carry:
            cur.next = ListNode()
            cur = cur.next

            temp = (l1.val if l1 is not None else 0) + (l2.val if l2 is not None else 0)
            if temp + carry >= 10:
                cur.val = temp + carry -10
                carry = 1
            else:
                cur.val = temp + carry
                carry = 0

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return res.next

