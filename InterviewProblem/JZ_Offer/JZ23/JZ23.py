'''
JZ23 链表中环的入口结点

描述：
给一个长度为n链表，若其中包含环，请找出该链表的环的入口结点，否则，返回null。
'''

'''
If the purpose of using the fast & slow pointer is to find the cycle in a linked list, it is very intuitive to set the stride of fast pointer as 2.
S1 = a + b + x*cycle
S2 = v2/v1 * S1 = a + b + y*cycle
(v2/v1 - 1)*S1 = (y-x)*cycle
We don't want to waste resource. So, the x should be 0. To ensure the divisibility, v2/v1 - 1 should be 1.

Stop as the same node and catch up and then surpass both can prove two pointers meet.
But surpassing case need extra space to record the nodes pointers visit each stride.

        a                b
        
-[ ] - [ ] - [ ] - [ ] - [ ] - [ ] 
                    |           |
                   [ ]         [ ]
                    |           |
                   [ ] - [ ] - [ ]

'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# @param pHead ListNode
# @return ListNode

### TC: O(n) and SC: O(1)
class Solution:
    def EntryNodeOfLoop(self, pHead):
        slow = pHead
        fast = pHead
        hasCycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                hasCycle = True
                break
        if hasCycle:
            fast = pHead
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return fast
        else:
            return None