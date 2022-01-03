'''
Leetcode 141. Linked List Cycle

Description:
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# @param head ListNode 
# @return bool

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
    def hasCycle(self, head):
        if head is None: ### corner case
            return False

        slow = head
        fast = head ### to avoid slow == fast
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        ### the code below works when check whether there is a cycle
        ### but it waste time, slow pointer will move extra distance
        ### also, it will fail in finding the entry of the cycle
        '''
        slow = head
        fast = head.next ### to avoid slow == fast
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        '''

        return False
