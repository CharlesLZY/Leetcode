'''
Leetcode 142. Linked List Cycle II

Description:
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). 
It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# @param head ListNode 
# @return ListNode

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

### Floyd's Cycle Finding Algorithm
### TC: O(n) and SC: O(1)
class Solution:
    def detectCycle(self, head):
        if head is None:
            return None

        hasCycle = False
        slow = head
        fast = head ### must be like this
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                hasCycle = True
                break

        if hasCycle:
            fast = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
            return fast
        else:
            return None

### Another Version
class Solution:
    def detectCycle(self, head):
        if head is None:
            return None

        hasCycle = False
        slow = head
        fast = head.next ### must be like this
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                hasCycle = True
                break

        if hasCycle:
            slow = slow.next ### trick
            fast = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
            return fast
        else:
            return None
