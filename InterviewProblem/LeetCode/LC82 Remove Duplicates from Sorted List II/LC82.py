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
        idle = ListNode() ### trick: idle head can bring a lot of convenience
        prev = idle
        cur = head
        while cur:
            if cur.next and cur.next.val == cur.val:
                ### in this branch, we will not add any node to the result, we only skip the duplicated nodes
                while cur.next and cur.next.val == cur.val:
                    # temp = cur.next
                    cur.next = cur.next.next
                    # del temp ### C/C++ style
                prev.next = cur.next ### trick
                # del cur
                cur = cur.next
            else:
                ### why we do not need to update prev.next?
                ### 因为本来就是连着的，我们要做的只是把连续重复的给跳过了
                cur = cur.next
                prev = prev.next

        return idle.next


class Solution:
    def deleteDuplicates(self, head):
        idle = ListNode()
        prev = idle
        cur = head
        while cur:
            if cur.next and cur.next.val == cur.val:
                while cur.next and cur.next.val == cur.val:
                    cur = cur.next
                prev.next = cur.next
                cur = cur.next
            else:
                prev.next = cur
                prev = prev.next
                cur = cur.next
        return idle.next

