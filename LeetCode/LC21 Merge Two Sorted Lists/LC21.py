'''
Leetcode 21. Merge Two Sorted Lists

Description:
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
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
    def mergeTwoLists(self, l1, l2):
        temp = ListNode()
        cur = temp
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return temp.next