'''
Leetcode 138. Copy List with Random Pointers

Description:
A linked list of length n is given such that each node contains an additional random pointer, 
which could point to any node in the list, or null.
Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, 
where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, 
then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. 
Each node is represented as a pair of [val, random_index] where:
- val: an integer representing Node.val
- random_index: the index of the node (range from 0 to n-1) that the random pointer points to, 
  or null if it does not point to any node.
Your code will only be given the head of the original linked list.
'''

# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random

# @param head Node 
# @return Node

### Hash Table Solution
### TC: O(n) and SC: O(n)
class Solution:
    def copyRandomList(self, head):
        if head is None:
            return None

        hashTable = {}

        idle = Node(-1)

        prev = idle
        cur = head

        ### build hashtable and set next pointer during this while loop
        while cur:
            newNode = Node(cur.val)
            newNode.random = cur.random
            hashTable[cur] = newNode
            prev.next = newNode

            prev = prev.next
            cur = cur.next

        cur = idle.next
        while cur:
            if cur.random:
                cur.random = hashTable[cur.random]
            cur = cur.next

        return idle.next

'''
[] represents old node and () represents new node
[] - () - [] - () - []-  ()
We don't need to maintain a hashtable.
old->next is new, we can use old.random to redirect

'''
### TC: O(n) and SC: O(1)
class Solution:
    def copyRandomList(self, head):
        if head is None:
            return None

        ### assemble the linked list
        cur = head
        while cur:
            newNode = Node(cur.val)
            newNode.next = cur.next
            cur.next = newNode ### place the new node after the old node
            cur = newNode.next

        newHead = head.next ### store new head to return

        ### set random link
        cur = head 
        while cur:
            newNode = cur.next
            newNode.random = cur.random.next if cur.random else None
            cur = cur.next.next ### move to next node

        ### seperate the new nodes from the old nodes
        cur = head
        while cur:
            newNode = cur.next
            cur.next = newNode.next
            newNode.next = cur.next.next if cur.next else None
            cur = cur.next

        return newHead













        