'''
Leetcode 25. Reverse Nodes in k-Group

Description:
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
'''

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# @param head ListNode
# @param k int
# @return ListNode

### Intuitive Recursive Solution
### TC: O(n) and SC: O(n)
class Solution:
    def reverseKGroup(self, head, k):
        tail = head
        count = 0
        while count < k:
            if tail is None:
                return head
            else:
                tail = tail.next
                count += 1

        dummy = ListNode()
        prev = reverseKGroup(tail, k)
        cur = head
        count = 0
        while count < k:
            dummy.next = cur
            cur = cur.next
            dummy.next.next = prev
            prev = dummy.next
            count += 1
        return dummy.next


### Iterative Solution
### TC: O(n) and SC: O(1)
class Solution:
    def reverseKGroup(self, head, k):
        dummpy = ListNode()
        prevTail = dummy
        curHead = head

        while True:
            count = 0
            cur = curHead
            while count < k:
                if cur is None:
                    prevTail.next = curHead
                    break
                else:
                    cur = cur.next
                    count += 1

            if count == k: ### devided into several sub-problem reverse linked list
                nextHead = cur
                count = 0
                cur = curHead
                prev = None
                while count < k:
                    prevTail.next = cur
                    cur = cur.next
                    prevTail.next.next = prev
                    prev = prevTail.next
                    count += 1

                prevTail = curHead
                curHead = nextHead
            else:
                break

        return dummy.next