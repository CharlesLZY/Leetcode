'''
JZ24 反转链表

描述：
给定一个单链表的头结点pHead，长度为n，反转该链表后，返回新链表的表头。
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# @param head ListNode 
# @return ListNode

### TC: O(n) and SC: O(1)
class Solution:
    def ReverseList(self, head):
        temp = ListNode(None)
        prev = None
        cur = head
        while cur:
            temp.next = cur
            cur = cur.next
            temp.next.next = prev
            prev = temp.next
        return temp.next