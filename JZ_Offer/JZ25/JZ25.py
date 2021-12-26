'''
JC25 合并两个排序的链表

描述：
输入两个递增的链表，单个链表的长度为n，合并这两个链表并使新链表中的节点仍然是递增排序的。
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# @param pHead1 ListNode 
# @param pHead2 ListNode类
# @return ListNode

### TC: O(n) and SC: O(1)
class Solution:
    def Merge(self, pHead1, pHead2):

        temp = ListNode(None)
        cur = temp

        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                cur.next = pHead1
                pHead1 = pHead1.next
            else:
                cur.next = pHead2
                pHead2 = pHead2.next
            cur = cur.next

        if pHead1:
            cur.next = pHead1
        else:
            cur.next = pHead2

        return temp.next
        

