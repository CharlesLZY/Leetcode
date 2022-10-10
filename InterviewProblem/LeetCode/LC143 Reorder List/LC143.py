'''
Leetcode 143. Reorder List

Description:
You are given the head of a singly linked-list. The list can be represented as:
L0 -> L1 -> ... -> Ln-1 -> Ln
Reorder the list to be on the following form:
L0 -> Ln -> L1 -> Ln - 1 -> L2 -> Ln-2 -> ...

You may not modify the values in the list's nodes. Only nodes themselves may be changed.
'''

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# @param head ListNode 
# @return None

### Intuitive Solution
### TC: O(n) and SC: O(n)
class Solution:
    def reorderList(self, head):
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        
        lp = 1 ### skip the head
        rp = len(nodes) - 1
        i = 1
        prev = head
        while lp <= rp: ### trick: <=
            cur = nodes[lp] if i % 2 == 0 else nodes[rp] ### from head or tail
            cur.next = None
            prev.next = cur
            prev = cur
            if i % 2 == 0:
                lp += 1
            else:
                rp -= 1
            i += 1

### Better Solution
'''
1. Find the middle
2. Reverse the second part
3. Merge two parts
'''
### TC: O(n) and SC: O(1)
class Solution:
    def reorderList(self, head):
        ### 1. Find the middle
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        middle = slow

        ### 2. Reverse the second part
        cur = middle.next ### head of the second part
        middle.next = None ### cut the list
        idle = ListNode()
        while cur:
            temp = cur.next
            cur.next = idle.next
            idle.next = cur
            cur = temp
        
        ### merge two parts
        p1 = head
        p2 = idle.next
        while p1 and p2:
            temp1 = p1.next
            temp2 = p2.next
            p1.next = p2
            p2.next = temp1
            p1 = temp1
            p2 = temp2
            

