'''
JZ35 复杂链表的复制

描述：
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针random指向一个随机节点），请对此链表进行深拷贝，并返回拷贝后的头结点。
'''

# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

# @param pHead RandomListNode 
# @return RandomListNode 


### Hash Table solution
### TC: O(n) and SC: O(n)
class Solution:
    def Clone(self, pHead):
        if pHead is None: ### corner case: empty input
            return None

        hashTable = {}

        newHead = RandomListNode(None)
        node = newHead

        cur = pHead
        while cur:
            
            newNode = RandomListNode(cur.label)
            newNode.random = cur.random
            hashTable[cur.label] = newNode
            node.next = newNode

            node = node.next
            cur = cur.next

        node = newHead.next
        while node:
            if node.random:
                node.random = hashTable[node.random.label]
            node = node.next

        return newHead.next


'''
[] represents old node and () represents new node
[] - () - [] - () - []-  ()
We don't need to maintain a hashtable.
old->next is new, we can use old.random to redirect

'''
### TC: O(n) and SC: O(1)
class Solution:
    def Clone(self, pHead):
        if pHead is None: ### corner case: empty input
            return None

        ### assemble the linked list
        cur = pHead
        while cur:
            newNode = RandomListNode(cur.label)
            newNode.next = cur.next
            cur.next = newNode
            cur = newNode.next

        newHead = pHead.next ### store new head

        ### set random link
        cur = pHead
        while cur:
            newNode = cur.next
            newNode.random = cur.random.next if cur.random else None
            cur = cur.next.next

        ### seperate old and new linked list
        cur = pHead
        while cur:
            newNode = cur.next
            cur.next = newNode.next
            newNode.next = cur.next.next if cur.next else None
            cur = cur.next

        return newHead






