'''
JZ18 删除链表的节点

描述：
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。返回删除后的链表的头节点。链表中节点的值互不相同。
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# @param head ListNode
# @param val int 
# @return ListNode

class Solution:
    def deleteNode(self, head, val):
        if head.val == val: ### corner case
            return head.next
        prev = head
        cur = head.next
        while cur:
            if cur.val == val:
                prev.next = cur.next
                del cur ### c/c++ style
                break
            prev = cur
            cur = cur.next
        return head