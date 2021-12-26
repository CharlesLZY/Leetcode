'''
JZ52 两个链表的第一个公共结点

描述：
输入两个无环的单向链表，找出它们的第一个公共结点，如果没有公共节点则返回空。
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# @param pHead1 ListNode
# @param pHead2 ListNode
# @return ListNode

'''
The first thing we need to do when we are handing linked list is that check whether there could be a cycle.

     l1
[] - [] - [] 
            \
              [] - [] - []
            /      l0
     [] - []
        l2  

Two pointers move forward until to the end. When they come to end, start from the other's start.
Both pointers will move l1+l2+l0 when they come to the intersection node. 
'''

### TC: O(n) and SC: O(1)
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        p1 = pHead1
        p2 = pHead2
        if p1 is None or p2 is None: ### corner case
            return 
        while p1 != p2:
            if p1:
                p1 = p1.next
            else:
                p1 = pHead2
            if p2:
                p2 = p2.next
            else:
                p2 = pHead1
        return p1

