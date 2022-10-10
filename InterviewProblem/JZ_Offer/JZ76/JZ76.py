'''
### JZ76 删除链表中重复的结点

描述：
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表 1->2->3->3->4->4->5  处理后为 1->2->5
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# @param pHead ListNode 
# @return ListNode

### TC: O(n) and SC: O(1)
class Solution:
    def deleteDuplication(self, pHead):
        temp = ListNode(None)
        temp.next = pHead
        cur = pHead
        prev = temp
        while cur:
            if cur.next and cur.next.val == cur.val:
                while cur.next:
                    if cur.next.val == cur.val:
                        cur.next = cur.next.next
                    else:
                        break
                prev.next = cur.next
                cur = prev.next
            else:
                prev = cur
                cur = cur.next
        return temp.next