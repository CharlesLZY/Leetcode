'''
Leetcode 23. Merge k Sorted Lists

Description:
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
'''

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# @param lists List[ListNode]
# @return ListNode

### TC: O(kn) and SC: O(1)
class Solution:
    def mergeKLists(self, lists):
        k = len(lists)
        temp = ListNode()
        cur = temp
        while True:
            MIN = float("inf")
            MIN_idx = -1
            for i in range(k):
                if lists[i] and lists[i].val < MIN:
                    MIN = lists[i].val
                    MIN_idx = i
            if MIN_idx == -1:
                break
            else:
                lists[MIN_idx] = lists[MIN_idx].next
                cur.next = ListNode(MIN)
                cur = cur.next
        return temp.next

### TC: O(kn) and SC: O(k)
class Solution:
    def mergeKLists(self, lists):
        temp = ListNode()
        cur = temp
        frontier = []
        for l in lists:
            if l:
                frontier.append((l.val, l))
        while frontier:
            frontier.sort(key = lambda x: x[0])
            val, node = frontier.pop(0)
            cur.next = ListNode(val)
            cur = cur.next
            if node.next:
                frontier.append((node.next.val, node.next))
        return temp.next

### Intuitive Sort Solution
### TC: O(nlogn) and SC: O(n)
class Solution:
    def mergeKLists(self, lists):
        nodes = []
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        temp = ListNode()
        cur = temp
        for x in sorted(nodes):
            cur.next = ListNode(x)
            cur = cur.next
        return temp.next