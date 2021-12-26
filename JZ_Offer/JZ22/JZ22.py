'''
JZ22 链表中倒数最后k个结点

描述：
输入一个长度为 n 的链表，返回该链表中倒数第k个节点。
如果该链表长度小于k，请返回一个长度为 0 的链表。
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# @param pHead ListNode 
# @param k int 
# @return ListNode

### Intuitive Stack Solution
### TC: O(n) and SC: O(n)
class Solution:
    def FindKthToTail(self, pHead, k):
        stack = []
        cur = pHead
        while cur:
            stack.append(cur)
            cur = cur.next
        if len(stack) < k or k == 0: ### corner cases
            return None
        else:
            return stack[-k]

### Fast and Slow Pointer Solution
### TC: O(n) and SC: O(1)
class Solution:
    def FindKthToTail(self, pHead, k):
        if k == 0 or not pHead: ### corner case
            return None

        fast = pHead
        for i in range(k):
            if not fast:
                return None
            fast = fast.next

        slow = pHead
        while fast:
            slow = slow.next
            fast = fast.next

        return slow

