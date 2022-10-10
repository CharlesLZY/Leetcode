'''
Leetcode 369. Plus One Linked List

Description:
Given a non-negative integer represented as a linked list of digits, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list.
'''

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# @param head ListNode
# @return ListNode

### Intuitive Reverse Solution
### TC: O(n) and SC: O(1)
class Solution:
    def plusOne(self, head):
        def reverse(head):
            dummy = ListNode(-1)
            cur = head
            while cur:
                prev = dummy.next
                dummy.next = cur
                cur = cur.next
                dummy.next.next = prev
            return dummy.next
                
        tail = reverse(head)
        if tail.val != 9:
            tail.val = tail.val + 1
        else:
            carry = 1
            cur = tail
            prev = None
            while cur:
                if carry == 0:
                    break
                prev = cur
                cur.val = (cur.val + carry) % 10
                if cur.val == 0:
                    carry = 1
                else:
                    carry = 0
                cur = cur.next
            if carry == 1:
                prev.next = ListNode(1)

        return reverse(tail)

### Another solution
### 1. find the rightmost not-9 digit and plus one 2. set all the following 9s to 0s
### TC: O(n) and SC: O(1)
class Solution:
    def plusOne(self, head):
        # sentinel head
        sentinel = ListNode(0) ### trick: this sentinel node can be used as the carry bit
        sentinel.next = head
        not_nine = sentinel

        # find the rightmost not-9 digit
        while head:
            if head.val != 9:
                not_nine = head
            head = head.next

        # increase this rightmost not-9 digit by 1
        not_nine.val += 1
        not_nine = not_nine.next

        # set all the following 9s to 0s
        while not_nine:
            not_nine.val = 0
            not_nine = not_nine.next

        return sentinel if sentinel.val else sentinel.next