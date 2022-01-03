'''
Leetcode 148. Sort List

Description:
Given the head of a linked list, return the list after sorting it in ascending order.
'''

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# @param head ListNode
# @return ListNode

### Merge Sort Solution
### TC: O(nlogn) and SC: O(n)
class Solution:
    def sortList(self, head):
        def merge(l1, l2):
            dummy = ListNode()
            cur = dummy
            while l1 and l2:
                if l1.val > l2.val:
                    cur.next = l2
                    l2 = l2.next
                else:
                    cur.next=l1
                    l1=l1.next
                cur = cur.next
            if l1:
                cur.next=l1
            if l2:
                cur.next=l2
            return dummy.next

        def mergeSort(head):
            if head and head.next:
                ### find middle point
                slow = head
                fast = head
                prev = None
                while fast and fast.next:
                    prev = slow
                    fast = fast.next.next
                    slow = slow.next
                prev.next = None ### trick: must cut the whole list into two lists
                return merge(mergeSort(head), mergeSort(slow))

            else: ### the length of the linked list <= 1
                return head 

        return mergeSort(head)