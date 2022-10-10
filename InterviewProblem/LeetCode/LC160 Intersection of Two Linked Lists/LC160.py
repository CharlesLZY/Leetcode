'''
Leetcode 160. Intersection of Two Linked Lists

Description:
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.
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
    def getIntersectionNode(self, headA, headB):
        ### check cycle first
        fast = headA
        slow = headA
        flag = False ### whether there is cycle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                flag = True
                break
        
        if flag:
            ### find cycle
            fast = headA
            while fast != slow:
                fast = fast.next
                slow = slow.next
            return slow
        else:
            ### normal case
            p1 = headA
            p2 = headB
            while p1 != p2:
                if p1:
                    p1 = p1.next
                else:
                    p1 = headB
                if p2:
                    p2 = p2.next
                else:
                    p2 = headA
            return p1

### Hash Table Solution
### TC: O(n) and SC: O(n)
class Solution:
    def getIntersectionNode(self, headA, headB):
        hashTable = set()
        while headA:
            hashTable.add(id(headA)) ### memory address
            headA = headA.next

        while headB:
            if id(headB) in hashTable:
                return headB
            headB = headB.next
