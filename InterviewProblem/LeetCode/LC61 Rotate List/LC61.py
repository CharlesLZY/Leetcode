'''
Leetcode 61. Rotate List

Description:
Given the head of a linked list, rotate the list to the right by k places.
'''

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# @param head ListNode
# @param k int 
# @return ListNode

### TC: O(n) and SC: O(1)
class Solution:
    def rotateRight(self, head, k):
        if head is None: ### corner case
            return None
        
        dummy = ListNode()
        dummy.next = head

        fast = dummy
        length = 0
        while fast.next:
            length += 1
            fast = fast.next
        ### leetcode定义的旋转次数，每旋转一次把最后一个node放到最前面，(所以可以无限转下去)
        k = k % length ### trick: to avoid repeated iteration

        if k == 0: ### trick: the new head is the same as the old head
            return head

        fast = dummy
        slow = dummy
        i = 0
        while i < k:    
            fast = fast.next ### fast move advance k steps
            i += 1
        
        while fast.next: ### find pivot
            fast = fast.next
            slow = slow.next

        newTail = slow
        newHead = slow.next
        tail = fast

        if newHead == head:
            return head

        newTail.next = None
        tail.next = head 

        return newHead
