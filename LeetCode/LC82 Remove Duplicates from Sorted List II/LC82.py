'''
Leetcode 82. Remove Duplicates from Sorted List II

Description:
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. Return the linked list sorted as well.
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
        dummy = ListNode(next=head) ### trick: dummy head can bring a lot of convenience
        prev = dummy
        while head:
            if head.next and head.next.val == head.val:
                while head.next and head.next.val == head.val:
                    temp = head.next
                    head.next = head.next.next
                    del temp ### C/C++
                prev.next = head.next
                del head
                head = prev.next
            else:
                head = head.next
                prev = prev.next

        return dummy.next

class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(next=head) ### trick
        prev = dummy
        while head:
            if head.next and head.val == head.next.val:
                # move till the end of duplicates sublist
                while head.next and head.val == head.next.val:
                    head = head.next
                # skip all duplicates
                prev.next = head.next
            else:
                prev = prev.next

            head = prev.next
            
        return dummy.next
