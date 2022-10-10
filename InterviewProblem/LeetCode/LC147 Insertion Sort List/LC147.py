'''
Leetcode 147. Insertion Sort List

Description:
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.
The steps of the insertion sort algorithm:
1. Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
2. At each iteration, insertion sort removes one element from the input data, 
   finds the location it belongs within the sorted list and inserts it there.
3. It repeats until no input elements remain.

The following is a graphical example of the insertion sort algorithm. 
The partially sorted list (black) initially contains only the first element in the list. 
One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.
'''

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# @param head ListNode
# @return ListNode

### TC: O(n^2) and SC: O(1)
class Solution:
    def insertionSortList(self, head):
        idle = ListNode()
        node = head
        while node:
            cur = idle
            while cur.next:
                if node.val > cur.next.val:
                    cur = cur.next
                else:
                    break
            temp = cur.next
            cur.next = node
            node = node.next
            cur.next.next = temp
        return idle.next

        